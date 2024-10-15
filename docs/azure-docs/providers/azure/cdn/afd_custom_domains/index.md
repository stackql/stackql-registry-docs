---
title: afd_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_custom_domains
  - cdn
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>afd_custom_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>afd_custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_custom_domains" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_afd_custom_domains', value: 'view', },
        { label: 'afd_custom_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azure_dns_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="customDomainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_validation_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="pre_validated_custom_domain_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tls_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="validation_properties" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties of the domain to create. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing AzureFrontDoor domains. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Creates a new domain within the specified profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing domain within a profile. |
| <CopyableCode code="refresh_validation_token" /> | `EXEC` | <CopyableCode code="customDomainName, profileName, resourceGroupName, subscriptionId" /> | Updates the domain validation token. |

## `SELECT` examples

Lists existing AzureFrontDoor domains.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_afd_custom_domains', value: 'view', },
        { label: 'afd_custom_domains', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azure_dns_zone,
customDomainName,
deployment_status,
domain_validation_state,
extended_properties,
host_name,
pre_validated_custom_domain_resource_id,
profileName,
profile_name,
provisioning_state,
resourceGroupName,
subscriptionId,
tls_settings,
validation_properties
FROM azure.cdn.vw_afd_custom_domains
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.afd_custom_domains
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>afd_custom_domains</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.cdn.afd_custom_domains (
customDomainName,
profileName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ customDomainName }}',
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: profileName
          value: string
        - name: tlsSettings
          value:
            - name: certificateType
              value: string
            - name: minimumTlsVersion
              value: string
            - name: secret
              value:
                - name: id
                  value: string
        - name: provisioningState
          value: string
        - name: deploymentStatus
          value: string
        - name: domainValidationState
          value: string
        - name: hostName
          value: string
        - name: extendedProperties
          value: object
        - name: validationProperties
          value:
            - name: validationToken
              value: string
            - name: expirationDate
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>afd_custom_domains</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.afd_custom_domains
SET 
properties = '{{ properties }}'
WHERE 
customDomainName = '{{ customDomainName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>afd_custom_domains</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.afd_custom_domains
WHERE customDomainName = '{{ customDomainName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

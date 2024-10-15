---
title: enterprise_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprise_policies
  - power_platform
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

Creates, updates, deletes, gets or lists a <code>enterprise_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enterprise_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.power_platform.enterprise_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_enterprise_policies', value: 'view', },
        { label: 'enterprise_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="enterprisePolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The identity of the EnterprisePolicy. |
| <CopyableCode code="kind" /> | `text` | The Kind (type) of Enterprise Policy |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="lockbox" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_injection" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The identity of the EnterprisePolicy. |
| <CopyableCode code="kind" /> | `string` | The Kind (type) of Enterprise Policy |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties that define configuration for the enterprise policy. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="enterprisePolicyName, resourceGroupName, subscriptionId" /> | Get information about an EnterprisePolicy |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve a list of EnterprisePolicies within a given resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieve a list of EnterprisePolicies within a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="enterprisePolicyName, resourceGroupName, subscriptionId, data__kind" /> | Creates an EnterprisePolicy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="enterprisePolicyName, resourceGroupName, subscriptionId" /> | Delete an EnterprisePolicy |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="enterprisePolicyName, resourceGroupName, subscriptionId" /> | Updates an EnterprisePolicy |

## `SELECT` examples

Retrieve a list of EnterprisePolicies within a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_enterprise_policies', value: 'view', },
        { label: 'enterprise_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
encryption,
enterprisePolicyName,
health_status,
identity,
kind,
location,
lockbox,
network_injection,
resourceGroupName,
subscriptionId,
system_data,
system_id,
tags
FROM azure_extras.power_platform.vw_enterprise_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
location,
properties,
systemData,
tags
FROM azure_extras.power_platform.enterprise_policies
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>enterprise_policies</code> resource.

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
INSERT INTO azure_extras.power_platform.enterprise_policies (
enterprisePolicyName,
resourceGroupName,
subscriptionId,
data__kind,
tags,
location,
identity,
kind,
properties,
systemData
)
SELECT 
'{{ enterprisePolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ kind }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: identity
      value:
        - name: systemAssignedIdentityPrincipalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: kind
      value: []
    - name: properties
      value:
        - name: systemId
          value: string
        - name: lockbox
          value:
            - name: state
              value: []
        - name: encryption
          value:
            - name: keyVault
              value:
                - name: keyIdentifier
                  value: string
                - name: identity
                  value: string
        - name: networkInjection
          value:
            - name: virtualNetworks
              value:
                - name: value
                  value:
                    - - name: id
                        value: string
                      - name: subnet
                        value:
                          - name: name
                            value: string
                - name: nextLink
                  value: string
        - name: healthStatus
          value: []
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>enterprise_policies</code> resource.

```sql
/*+ update */
UPDATE azure_extras.power_platform.enterprise_policies
SET 
tags = '{{ tags }}',
location = '{{ location }}',
identity = '{{ identity }}',
kind = '{{ kind }}',
properties = '{{ properties }}',
systemData = '{{ systemData }}'
WHERE 
enterprisePolicyName = '{{ enterprisePolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>enterprise_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.power_platform.enterprise_policies
WHERE enterprisePolicyName = '{{ enterprisePolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

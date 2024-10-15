---
title: afd_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_endpoints
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

Creates, updates, deletes, gets or lists a <code>afd_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>afd_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_afd_endpoints', value: 'view', },
        { label: 'afd_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_generated_domain_name_label_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create an endpoint. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing AzureFrontDoor endpoints. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Creates a new AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update domains, use the Update Custom Domain operation. |
| <CopyableCode code="purge_content" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__contentPaths" /> | Removes a content from AzureFrontDoor. |
| <CopyableCode code="validate_custom_domain" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__hostName" /> | Validates the custom domain mapping to ensure it maps to the correct Azure Front Door endpoint in DNS. |

## `SELECT` examples

Lists existing AzureFrontDoor endpoints.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_afd_endpoints', value: 'view', },
        { label: 'afd_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_generated_domain_name_label_scope,
deployment_status,
enabled_state,
endpointName,
host_name,
location,
profileName,
profile_name,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.cdn.vw_afd_endpoints
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.cdn.afd_endpoints
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>afd_endpoints</code> resource.

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
INSERT INTO azure.cdn.afd_endpoints (
endpointName,
profileName,
resourceGroupName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ endpointName }}',
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: profileName
          value: string
        - name: enabledState
          value: string
        - name: provisioningState
          value: string
        - name: deploymentStatus
          value: string
        - name: hostName
          value: string
        - name: autoGeneratedDomainNameLabelScope
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>afd_endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.afd_endpoints
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>afd_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.afd_endpoints
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

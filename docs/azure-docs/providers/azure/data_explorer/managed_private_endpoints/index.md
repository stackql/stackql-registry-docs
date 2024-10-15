---
title: managed_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_private_endpoints
  - data_explorer
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

Creates, updates, deletes, gets or lists a <code>managed_private_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.managed_private_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_private_endpoints', value: 'view', },
        { label: 'managed_private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedPrivateEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_region" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class representing the properties of a managed private endpoint object. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId" /> | Gets a managed private endpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Returns the list of managed private endpoints. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId" /> | Creates a managed private endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId" /> | Deletes a managed private endpoint. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="clusterName, managedPrivateEndpointName, resourceGroupName, subscriptionId" /> | Updates a managed private endpoint. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__name, data__type" /> | Checks that the managed private endpoints resource name is valid and is not already in use. |

## `SELECT` examples

Returns the list of managed private endpoints.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_private_endpoints', value: 'view', },
        { label: 'managed_private_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
group_id,
managedPrivateEndpointName,
private_link_resource_id,
private_link_resource_region,
provisioning_state,
request_message,
resourceGroupName,
subscriptionId,
system_data
FROM azure.data_explorer.vw_managed_private_endpoints
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.data_explorer.managed_private_endpoints
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_private_endpoints</code> resource.

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
INSERT INTO azure.data_explorer.managed_private_endpoints (
clusterName,
managedPrivateEndpointName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ clusterName }}',
'{{ managedPrivateEndpointName }}',
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
        - name: privateLinkResourceId
          value: string
        - name: privateLinkResourceRegion
          value: string
        - name: groupId
          value: string
        - name: requestMessage
          value: string
        - name: provisioningState
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

Updates a <code>managed_private_endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.data_explorer.managed_private_endpoints
SET 
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND managedPrivateEndpointName = '{{ managedPrivateEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>managed_private_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_explorer.managed_private_endpoints
WHERE clusterName = '{{ clusterName }}'
AND managedPrivateEndpointName = '{{ managedPrivateEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

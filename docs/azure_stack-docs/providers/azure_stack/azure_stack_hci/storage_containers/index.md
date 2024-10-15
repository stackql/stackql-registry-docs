---
title: storage_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_containers
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>storage_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.storage_containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_containers', value: 'view', },
        { label: 'storage_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="path" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageContainerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties under the storage container resource |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageContainerName, subscriptionId" /> | Gets a storage container |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the storage containers in the specified resource group. Use the nextLink property in the response to get the next page of storage containers. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the storage containers in the specified subscription. Use the nextLink property in the response to get the next page of storage containers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, storageContainerName, subscriptionId" /> | The operation to create or update a storage container. Please note some properties can be set only during storage container creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, storageContainerName, subscriptionId" /> | The operation to delete a storage container. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, storageContainerName, subscriptionId" /> | The operation to update a storage container. |

## `SELECT` examples

Lists all of the storage containers in the specified subscription. Use the nextLink property in the response to get the next page of storage containers.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_storage_containers', value: 'view', },
        { label: 'storage_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
extended_location,
location,
path,
provisioning_state,
resourceGroupName,
status,
storageContainerName,
subscriptionId,
tags
FROM azure_stack.azure_stack_hci.vw_storage_containers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure_stack.azure_stack_hci.storage_containers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_containers</code> resource.

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
INSERT INTO azure_stack.azure_stack_hci.storage_containers (
resourceGroupName,
storageContainerName,
subscriptionId,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ storageContainerName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: path
          value: string
        - name: provisioningState
          value: string
        - name: status
          value:
            - name: errorCode
              value: string
            - name: errorMessage
              value: string
            - name: availableSizeMB
              value: integer
            - name: containerSizeMB
              value: integer
            - name: provisioningStatus
              value:
                - name: operationId
                  value: string
                - name: status
                  value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>storage_containers</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack_hci.storage_containers
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND storageContainerName = '{{ storageContainerName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>storage_containers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.storage_containers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageContainerName = '{{ storageContainerName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

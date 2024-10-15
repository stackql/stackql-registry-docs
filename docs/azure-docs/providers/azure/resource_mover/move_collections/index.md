---
title: move_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - move_collections
  - resource_mover
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

Creates, updates, deletes, gets or lists a <code>move_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>move_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_mover.move_collections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_move_collections', value: 'view', },
        { label: 'move_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource Id for the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The etag of the resource. |
| <CopyableCode code="identity" /> | `text` | Defines the MSI properties of the Move Collection. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives. |
| <CopyableCode code="moveCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="move_region" /> | `text` | field from the `properties` object |
| <CopyableCode code="move_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_region" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="target_region" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource Id for the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="etag" /> | `string` | The etag of the resource. |
| <CopyableCode code="identity" /> | `object` | Defines the MSI properties of the Move Collection. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives. |
| <CopyableCode code="properties" /> | `object` | Defines the move collection properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId" /> | Gets the move collection. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId" /> | Creates or updates a move collection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId" /> | Deletes a move collection. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId" /> | Updates a move collection. |
| <CopyableCode code="bulk_remove" /> | `EXEC` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId" /> | Removes the set of move resources included in the request body from move collection. The orchestration is done by service. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId, data__moveResources" /> | Commits the set of resources included in the request body. The commit operation is triggered on the moveResources in the moveState 'CommitPending' or 'CommitFailed', on a successful completion the moveResource moveState do a transition to Committed. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| <CopyableCode code="discard" /> | `EXEC` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId, data__moveResources" /> | Discards the set of resources included in the request body. The discard operation is triggered on the moveResources in the moveState 'CommitPending' or 'DiscardFailed', on a successful completion the moveResource moveState do a transition to MovePending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| <CopyableCode code="initiate_move" /> | `EXEC` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId, data__moveResources" /> | Moves the set of resources included in the request body. The move operation is triggered after the moveResources are in the moveState 'MovePending' or 'MoveFailed', on a successful completion the moveResource moveState do a transition to CommitPending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| <CopyableCode code="prepare" /> | `EXEC` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId, data__moveResources" /> | Initiates prepare for the set of resources included in the request body. The prepare operation is on the moveResources that are in the moveState 'PreparePending' or 'PrepareFailed', on a successful completion the moveResource moveState do a transition to MovePending. To aid the user to prerequisite the operation the client can call operation with validateOnly property set to true. |
| <CopyableCode code="resolve_dependencies" /> | `EXEC` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId" /> | Computes, resolves and validate the dependencies of the moveResources in the move collection. |

## `SELECT` examples

Gets the move collection.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_move_collections', value: 'view', },
        { label: 'move_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
errors,
etag,
identity,
location,
moveCollectionName,
move_region,
move_type,
provisioning_state,
resourceGroupName,
source_region,
subscriptionId,
system_data,
tags,
target_region,
type,
version
FROM azure.resource_mover.vw_move_collections
WHERE moveCollectionName = '{{ moveCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
location,
properties,
systemData,
tags,
type
FROM azure.resource_mover.move_collections
WHERE moveCollectionName = '{{ moveCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>move_collections</code> resource.

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
INSERT INTO azure.resource_mover.move_collections (
moveCollectionName,
resourceGroupName,
subscriptionId,
tags,
location,
identity,
properties
)
SELECT 
'{{ moveCollectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: tags
      value: object
    - name: location
      value: string
    - name: identity
      value:
        - name: type
          value: []
        - name: principalId
          value: string
        - name: tenantId
          value: string
    - name: properties
      value:
        - name: sourceRegion
          value: string
        - name: targetRegion
          value: string
        - name: moveRegion
          value: string
        - name: provisioningState
          value: []
        - name: version
          value: string
        - name: moveType
          value: []
        - name: errors
          value: string
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

Updates a <code>move_collections</code> resource.

```sql
/*+ update */
UPDATE azure.resource_mover.move_collections
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
moveCollectionName = '{{ moveCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>move_collections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.resource_mover.move_collections
WHERE moveCollectionName = '{{ moveCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

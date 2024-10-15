---
title: move_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - move_resources
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

Creates, updates, deletes, gets or lists a <code>move_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>move_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_mover.move_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_move_resources', value: 'view', },
        { label: 'move_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource Id for the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="depends_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="depends_on_overrides" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="existing_target_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_resolve_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="moveCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="moveResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="move_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_resource_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource Id for the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Defines the move resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="moveCollectionName, moveResourceName, resourceGroupName, subscriptionId" /> | Gets the Move Resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="moveCollectionName, resourceGroupName, subscriptionId" /> | Lists the Move Resources in the move collection. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="moveCollectionName, moveResourceName, resourceGroupName, subscriptionId" /> | Creates or updates a Move Resource in the move collection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="moveCollectionName, moveResourceName, resourceGroupName, subscriptionId" /> | Deletes a Move Resource from the move collection. |

## `SELECT` examples

Lists the Move Resources in the move collection.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_move_resources', value: 'view', },
        { label: 'move_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
depends_on,
depends_on_overrides,
errors,
existing_target_id,
is_resolve_required,
moveCollectionName,
moveResourceName,
move_status,
provisioning_state,
resourceGroupName,
resource_settings,
source_id,
source_resource_settings,
subscriptionId,
system_data,
target_id,
type
FROM azure.resource_mover.vw_move_resources
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
properties,
systemData,
type
FROM azure.resource_mover.move_resources
WHERE moveCollectionName = '{{ moveCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>move_resources</code> resource.

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
INSERT INTO azure.resource_mover.move_resources (
moveCollectionName,
moveResourceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ moveCollectionName }}',
'{{ moveResourceName }}',
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: sourceId
          value: string
        - name: targetId
          value: string
        - name: existingTargetId
          value: string
        - name: resourceSettings
          value:
            - name: resourceType
              value: string
            - name: targetResourceName
              value: string
            - name: targetResourceGroupName
              value: string
        - name: moveStatus
          value: string
        - name: dependsOn
          value:
            - - name: id
                value: string
              - name: resolutionStatus
                value: string
              - name: resolutionType
                value: []
              - name: dependencyType
                value: []
              - name: manualResolution
                value:
                  - name: targetId
                    value: string
              - name: automaticResolution
                value:
                  - name: moveResourceId
                    value: string
              - name: isOptional
                value: string
        - name: dependsOnOverrides
          value:
            - - name: id
                value: string
              - name: targetId
                value: string
        - name: isResolveRequired
          value: boolean
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

## `DELETE` example

Deletes the specified <code>move_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.resource_mover.move_resources
WHERE moveCollectionName = '{{ moveCollectionName }}'
AND moveResourceName = '{{ moveResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

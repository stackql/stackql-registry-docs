---
title: proximity_placement_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - proximity_placement_groups
  - compute
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

Creates, updates, deletes, gets or lists a <code>proximity_placement_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>proximity_placement_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.proximity_placement_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_proximity_placement_groups', value: 'view', },
        { label: 'proximity_placement_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="availability_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="colocation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="intent" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="proximityPlacementGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="proximity_placement_group_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="virtual_machine_scale_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machines" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | Specifies the Availability Zone where virtual machine, virtual machine scale set or availability set associated with the  proximity placement group can be created. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Proximity Placement Group. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | Specifies the Availability Zone where virtual machine, virtual machine scale set or availability set associated with the  proximity placement group can be created. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="proximityPlacementGroupName, resourceGroupName, subscriptionId" /> | Retrieves information about a proximity placement group . |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all proximity placement groups in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all proximity placement groups in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="proximityPlacementGroupName, resourceGroupName, subscriptionId" /> | Create or update a proximity placement group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="proximityPlacementGroupName, resourceGroupName, subscriptionId" /> | Delete a proximity placement group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="proximityPlacementGroupName, resourceGroupName, subscriptionId" /> | Update a proximity placement group. |

## `SELECT` examples

Lists all proximity placement groups in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_proximity_placement_groups', value: 'view', },
        { label: 'proximity_placement_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
availability_sets,
colocation_status,
intent,
location,
proximityPlacementGroupName,
proximity_placement_group_type,
resourceGroupName,
subscriptionId,
tags,
type,
virtual_machine_scale_sets,
virtual_machines,
zones
FROM azure.compute.vw_proximity_placement_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type,
zones
FROM azure.compute.proximity_placement_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>proximity_placement_groups</code> resource.

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
INSERT INTO azure.compute.proximity_placement_groups (
proximityPlacementGroupName,
resourceGroupName,
subscriptionId,
properties,
zones,
location,
tags
)
SELECT 
'{{ proximityPlacementGroupName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ zones }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: proximityPlacementGroupType
          value: string
        - name: virtualMachines
          value:
            - - name: id
                value: string
              - name: colocationStatus
                value:
                  - name: code
                    value: string
                  - name: level
                    value: string
                  - name: displayStatus
                    value: string
                  - name: message
                    value: string
                  - name: time
                    value: string
        - name: virtualMachineScaleSets
          value:
            - - name: id
                value: string
        - name: availabilitySets
          value:
            - - name: id
                value: string
        - name: intent
          value:
            - name: vmSizes
              value:
                - string
    - name: zones
      value:
        - string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>proximity_placement_groups</code> resource.

```sql
/*+ update */
UPDATE azure.compute.proximity_placement_groups
SET 
tags = '{{ tags }}'
WHERE 
proximityPlacementGroupName = '{{ proximityPlacementGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>proximity_placement_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.proximity_placement_groups
WHERE proximityPlacementGroupName = '{{ proximityPlacementGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

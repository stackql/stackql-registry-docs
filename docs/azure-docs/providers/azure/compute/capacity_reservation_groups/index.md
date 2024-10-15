---
title: capacity_reservation_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservation_groups
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

Creates, updates, deletes, gets or lists a <code>capacity_reservation_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservation_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.capacity_reservation_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_capacity_reservation_groups', value: 'view', },
        { label: 'capacity_reservation_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="capacityReservationGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_reservations" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sharing_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="virtual_machines_associated" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | Availability Zones to use for this capacity reservation group. The zones can be assigned only during creation. If not provided, the group supports only regional resources in the region. If provided, enforces each capacity reservation in the group to be in one of the zones. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | capacity reservation group Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | Availability Zones to use for this capacity reservation group. The zones can be assigned only during creation. If not provided, the group supports only regional resources in the region. If provided, enforces each capacity reservation in the group to be in one of the zones. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="capacityReservationGroupName, resourceGroupName, subscriptionId" /> | The operation that retrieves information about a capacity reservation group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the capacity reservation groups in the specified resource group. Use the nextLink property in the response to get the next page of capacity reservation groups. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the capacity reservation groups in the subscription. Use the nextLink property in the response to get the next page of capacity reservation groups. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="capacityReservationGroupName, resourceGroupName, subscriptionId" /> | The operation to create or update a capacity reservation group. When updating a capacity reservation group, only tags and sharing profile may be modified. Please refer to https://aka.ms/CapacityReservation for more details. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="capacityReservationGroupName, resourceGroupName, subscriptionId" /> | The operation to delete a capacity reservation group. This operation is allowed only if all the associated resources are disassociated from the reservation group and all capacity reservations under the reservation group have also been deleted. Please refer to https://aka.ms/CapacityReservation for more details. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="capacityReservationGroupName, resourceGroupName, subscriptionId" /> | The operation to update a capacity reservation group. When updating a capacity reservation group, only tags and sharing profile may be modified. |

## `SELECT` examples

Lists all of the capacity reservation groups in the subscription. Use the nextLink property in the response to get the next page of capacity reservation groups.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_capacity_reservation_groups', value: 'view', },
        { label: 'capacity_reservation_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
capacityReservationGroupName,
capacity_reservations,
instance_view,
location,
resourceGroupName,
sharing_profile,
subscriptionId,
tags,
type,
virtual_machines_associated,
zones
FROM azure.compute.vw_capacity_reservation_groups
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
FROM azure.compute.capacity_reservation_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>capacity_reservation_groups</code> resource.

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
INSERT INTO azure.compute.capacity_reservation_groups (
capacityReservationGroupName,
resourceGroupName,
subscriptionId,
properties,
zones,
location,
tags
)
SELECT 
'{{ capacityReservationGroupName }}',
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
        - name: capacityReservations
          value:
            - - name: id
                value: string
        - name: virtualMachinesAssociated
          value:
            - - name: id
                value: string
        - name: instanceView
          value:
            - name: capacityReservations
              value:
                - - name: name
                    value: string
                  - name: utilizationInfo
                    value:
                      - name: currentCapacity
                        value: integer
                      - name: virtualMachinesAllocated
                        value:
                          - - name: id
                              value: string
                  - name: statuses
                    value:
                      - - name: code
                          value: string
                        - name: level
                          value: string
                        - name: displayStatus
                          value: string
                        - name: message
                          value: string
                        - name: time
                          value: string
            - name: sharedSubscriptionIds
              value:
                - - name: id
                    value: string
        - name: sharingProfile
          value:
            - name: subscriptionIds
              value:
                - - name: id
                    value: string
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

Updates a <code>capacity_reservation_groups</code> resource.

```sql
/*+ update */
UPDATE azure.compute.capacity_reservation_groups
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
capacityReservationGroupName = '{{ capacityReservationGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>capacity_reservation_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.capacity_reservation_groups
WHERE capacityReservationGroupName = '{{ capacityReservationGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

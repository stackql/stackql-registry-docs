---
title: capacity_reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - capacity_reservations
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

Creates, updates, deletes, gets or lists a <code>capacity_reservations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capacity_reservations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.capacity_reservations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_capacity_reservations', value: 'view', },
        { label: 'capacity_reservations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="capacityReservationGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacityReservationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="platform_fault_domain_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="reservation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="virtual_machines_associated" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | Availability Zone to use for this capacity reservation. The zone has to be single value and also should be part for the list of zones specified during the capacity reservation group creation. The zone can be assigned only during creation. If not provided, the reservation supports only non-zonal deployments. If provided, enforces VM/VMSS using this capacity reservation to be in same zone. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the Capacity reservation. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | Availability Zone to use for this capacity reservation. The zone has to be single value and also should be part for the list of zones specified during the capacity reservation group creation. The zone can be assigned only during creation. If not provided, the reservation supports only non-zonal deployments. If provided, enforces VM/VMSS using this capacity reservation to be in same zone. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="capacityReservationGroupName, capacityReservationName, resourceGroupName, subscriptionId" /> | The operation that retrieves information about the capacity reservation. |
| <CopyableCode code="list_by_capacity_reservation_group" /> | `SELECT` | <CopyableCode code="capacityReservationGroupName, resourceGroupName, subscriptionId" /> | Lists all of the capacity reservations in the specified capacity reservation group. Use the nextLink property in the response to get the next page of capacity reservations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="capacityReservationGroupName, capacityReservationName, resourceGroupName, subscriptionId, data__sku" /> | The operation to create or update a capacity reservation. Please note some properties can be set only during capacity reservation creation. Please refer to https://aka.ms/CapacityReservation for more details. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="capacityReservationGroupName, capacityReservationName, resourceGroupName, subscriptionId" /> | The operation to delete a capacity reservation. This operation is allowed only when all the associated resources are disassociated from the capacity reservation. Please refer to https://aka.ms/CapacityReservation for more details. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="capacityReservationGroupName, capacityReservationName, resourceGroupName, subscriptionId" /> | The operation to update a capacity reservation. |

## `SELECT` examples

Lists all of the capacity reservations in the specified capacity reservation group. Use the nextLink property in the response to get the next page of capacity reservations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_capacity_reservations', value: 'view', },
        { label: 'capacity_reservations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
capacityReservationGroupName,
capacityReservationName,
instance_view,
location,
platform_fault_domain_count,
provisioning_state,
provisioning_time,
reservation_id,
resourceGroupName,
sku,
subscriptionId,
tags,
time_created,
type,
virtual_machines_associated,
zones
FROM azure.compute.vw_capacity_reservations
WHERE capacityReservationGroupName = '{{ capacityReservationGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
sku,
tags,
type,
zones
FROM azure.compute.capacity_reservations
WHERE capacityReservationGroupName = '{{ capacityReservationGroupName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>capacity_reservations</code> resource.

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
INSERT INTO azure.compute.capacity_reservations (
capacityReservationGroupName,
capacityReservationName,
resourceGroupName,
subscriptionId,
data__sku,
properties,
sku,
zones,
location,
tags
)
SELECT 
'{{ capacityReservationGroupName }}',
'{{ capacityReservationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__sku }}',
'{{ properties }}',
'{{ sku }}',
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
        - name: reservationId
          value: string
        - name: platformFaultDomainCount
          value: integer
        - name: virtualMachinesAssociated
          value:
            - - name: id
                value: string
        - name: provisioningTime
          value: string
        - name: provisioningState
          value: string
        - name: instanceView
          value:
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
        - name: timeCreated
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer
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

Updates a <code>capacity_reservations</code> resource.

```sql
/*+ update */
UPDATE azure.compute.capacity_reservations
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
capacityReservationGroupName = '{{ capacityReservationGroupName }}'
AND capacityReservationName = '{{ capacityReservationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>capacity_reservations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.capacity_reservations
WHERE capacityReservationGroupName = '{{ capacityReservationGroupName }}'
AND capacityReservationName = '{{ capacityReservationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: availability_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_sets
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

Creates, updates, deletes, gets or lists a <code>availability_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>availability_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.availability_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_availability_sets', value: 'view', },
        { label: 'availability_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="availabilitySetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="platform_fault_domain_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="platform_update_domain_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="proximity_placement_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_events_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="statuses" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="virtual_machines" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The instance view of a resource. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availabilitySetName, resourceGroupName, subscriptionId" /> | Retrieves information about an availability set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all availability sets in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all availability sets in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="availabilitySetName, resourceGroupName, subscriptionId" /> | Create or update an availability set. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="availabilitySetName, resourceGroupName, subscriptionId" /> | Delete an availability set. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="availabilitySetName, resourceGroupName, subscriptionId" /> | Update an availability set. |

## `SELECT` examples

Lists all availability sets in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_availability_sets', value: 'view', },
        { label: 'availability_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
availabilitySetName,
location,
platform_fault_domain_count,
platform_update_domain_count,
proximity_placement_group,
resourceGroupName,
scheduled_events_policy,
sku,
statuses,
subscriptionId,
tags,
type,
virtual_machines
FROM azure.compute.vw_availability_sets
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
sku,
tags,
type
FROM azure.compute.availability_sets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>availability_sets</code> resource.

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
INSERT INTO azure.compute.availability_sets (
availabilitySetName,
resourceGroupName,
subscriptionId,
properties,
sku,
location,
tags
)
SELECT 
'{{ availabilitySetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ sku }}',
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
        - name: platformUpdateDomainCount
          value: integer
        - name: platformFaultDomainCount
          value: integer
        - name: virtualMachines
          value:
            - - name: id
                value: string
        - name: proximityPlacementGroup
          value:
            - name: id
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
        - name: scheduledEventsPolicy
          value:
            - name: userInitiatedRedeploy
              value:
                - name: automaticallyApprove
                  value: boolean
            - name: userInitiatedReboot
              value:
                - name: automaticallyApprove
                  value: boolean
            - name: scheduledEventsAdditionalPublishingTargets
              value:
                - name: eventGridAndResourceGraph
                  value:
                    - name: enable
                      value: boolean
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer
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

Updates a <code>availability_sets</code> resource.

```sql
/*+ update */
UPDATE azure.compute.availability_sets
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
availabilitySetName = '{{ availabilitySetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>availability_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.availability_sets
WHERE availabilitySetName = '{{ availabilitySetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

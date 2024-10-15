---
title: virtual_machine_scale_set_vms
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vms
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_set_vms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_set_vms" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_scale_set_vms', value: 'view', },
        { label: 'virtual_machine_scale_set_vms', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="additional_capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag is property returned in Update/Get response of the VMSS VM, so that customer can supply it in the header to ensure optimistic updates. |
| <CopyableCode code="hardware_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the virtual machine. |
| <CopyableCode code="instanceId" /> | `text` | The virtual machine instance ID. |
| <CopyableCode code="instance_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="latest_model_applied" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="model_definition_applied" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**. |
| <CopyableCode code="protection_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resources" /> | `text` | The virtual machine child extension resources. |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="user_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualMachineScaleSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmScaleSetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | The virtual machine zones. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Etag is property returned in Update/Get response of the VMSS VM, so that customer can supply it in the header to ensure optimistic updates. |
| <CopyableCode code="identity" /> | `object` | Identity for the virtual machine. |
| <CopyableCode code="instanceId" /> | `string` | The virtual machine instance ID. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="plan" /> | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started ->**. Enter any required information and then click **Save**. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a virtual machine scale set virtual machine. |
| <CopyableCode code="resources" /> | `array` | The virtual machine child extension resources. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | The virtual machine zones. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Gets a virtual machine from a VM scale set. |
| <CopyableCode code="get_instance_view" /> | `SELECT` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Gets the status of a virtual machine from a VM scale set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineScaleSetName" /> | Gets a list of all virtual machines in a VM scale sets. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Deletes a virtual machine from a VM scale set. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Updates a virtual machine of a VM scale set. |
| <CopyableCode code="approve_rolling_upgrade" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Approve upgrade on deferred rolling upgrade for OS disk on a VM scale set instance. |
| <CopyableCode code="attach_detach_data_disks" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Attach and detach data disks to/from a virtual machine in a VM scale set. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Deallocates a specific virtual machine in a VM scale set. Shuts down the virtual machine and releases the compute resources it uses. You are not billed for the compute resources of this virtual machine once it is deallocated. |
| <CopyableCode code="perform_maintenance" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Performs maintenance on a virtual machine in a VM scale set. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Power off (stop) a virtual machine in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges. |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Shuts down the virtual machine in the virtual machine scale set, moves it to a new node, and powers it back on. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Reimages (upgrade the operating system) a specific virtual machine in a VM scale set. |
| <CopyableCode code="reimage_all" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Allows you to re-image all the disks ( including data disks ) in the a VM scale set instance. This operation is only supported for managed disks. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Restarts a virtual machine in a VM scale set. |
| <CopyableCode code="retrieve_boot_diagnostics_data" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | The operation to retrieve SAS URIs of boot diagnostic logs for a virtual machine in a VM scale set. |
| <CopyableCode code="run_command" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName, data__commandId" /> | Run command on a virtual machine in a VM scale set. |
| <CopyableCode code="simulate_eviction" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | The operation to simulate the eviction of spot virtual machine in a VM scale set. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Starts a virtual machine in a VM scale set. |

## `SELECT` examples

Gets a virtual machine from a VM scale set.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_scale_set_vms', value: 'view', },
        { label: 'virtual_machine_scale_set_vms', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
additional_capabilities,
availability_set,
diagnostics_profile,
etag,
hardware_profile,
identity,
instanceId,
instance_id,
instance_view,
latest_model_applied,
license_type,
location,
model_definition_applied,
network_profile,
network_profile_configuration,
os_profile,
plan,
protection_policy,
provisioning_state,
resourceGroupName,
resources,
security_profile,
sku,
storage_profile,
subscriptionId,
tags,
time_created,
type,
user_data,
virtualMachineScaleSetName,
vmScaleSetName,
vm_id,
zones
FROM azure.compute.vw_virtual_machine_scale_set_vms
WHERE instanceId = '{{ instanceId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
identity,
instanceId,
location,
plan,
properties,
resources,
sku,
tags,
type,
zones
FROM azure.compute.virtual_machine_scale_set_vms
WHERE instanceId = '{{ instanceId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>virtual_machine_scale_set_vms</code> resource.

```sql
/*+ update */
REPLACE azure.compute.virtual_machine_scale_set_vms
SET 
properties = '{{ properties }}',
plan = '{{ plan }}',
identity = '{{ identity }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
instanceId = '{{ instanceId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_scale_set_vms</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.virtual_machine_scale_set_vms
WHERE instanceId = '{{ instanceId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```

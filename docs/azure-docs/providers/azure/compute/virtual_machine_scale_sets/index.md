---
title: virtual_machine_scale_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_sets
  - compute
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `etag` | `string` | Etag is property returned in Create/Update/Get response of the VMSS, so that customer can supply it in the header to ensure optimistic updates |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `identity` | `object` | Identity for the virtual machine scale set. |
| `location` | `string` | Resource location |
| `plan` | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**. |
| `properties` | `object` | Describes the properties of a Virtual Machine Scale Set. |
| `sku` | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `zones` | `array` | The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vmScaleSetName` | Display information about a virtual machine scale set. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of all VM scale sets under a resource group. |
| `list_by_location` | `SELECT` | `location, subscriptionId` | Gets all the VM scale sets under the specified subscription for the specified location. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, vmScaleSetName` | Create or update a VM scale set. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vmScaleSetName` | Deletes a VM scale set. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of all VM scale sets under a resource group. |
| `_list_by_location` | `EXEC` | `location, subscriptionId` | Gets all the VM scale sets under the specified subscription for the specified location. |
| `approve_rolling_upgrade` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Approve upgrade on deferred rolling upgrades for OS disks in the virtual machines in a VM scale set. |
| `convert_to_single_placement_group` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Converts SinglePlacementGroup property to false for a existing virtual machine scale set. |
| `deallocate` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Deallocates specific virtual machines in a VM scale set. Shuts down the virtual machines and releases the compute resources. You are not billed for the compute resources that this virtual machine scale set deallocates. |
| `force_recovery_service_fabric_platform_update_domain_walk` | `EXEC` | `platformUpdateDomain, resourceGroupName, subscriptionId, vmScaleSetName` | Manual platform update domain walk to update virtual machines in a service fabric virtual machine scale set. |
| `perform_maintenance` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Perform maintenance on one or more virtual machines in a VM scale set. Operation on instances which are not eligible for perform maintenance will be failed. Please refer to best practices for more details: https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-maintenance-notifications |
| `power_off` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Power off (stop) one or more virtual machines in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges. |
| `reapply` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Reapplies the Virtual Machine Scale Set Virtual Machine Profile to the Virtual Machine Instances |
| `redeploy` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, and powers them back on. |
| `reimage` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Reimages (upgrade the operating system) one or more virtual machines in a VM scale set which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state. |
| `reimage_all` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This operation is only supported for managed disks. |
| `restart` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Restarts one or more virtual machines in a VM scale set. |
| `set_orchestration_service_state` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName, data__action, data__serviceName` | Changes ServiceState property for a given service |
| `start` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Starts one or more virtual machines in a VM scale set. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, vmScaleSetName` | Update a VM scale set. |

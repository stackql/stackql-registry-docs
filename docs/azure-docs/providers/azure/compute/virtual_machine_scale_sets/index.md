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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Etag is property returned in Create/Update/Get response of the VMSS, so that customer can supply it in the header to ensure optimistic updates |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Identity for the virtual machine scale set. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="plan" /> | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Scale Set. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | The virtual machine scale set zones. NOTE: Availability zones can only be set when you create the scale set |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Display information about a virtual machine scale set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of all VM scale sets under a resource group. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets all the VM scale sets under the specified subscription for the specified location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Create or update a VM scale set. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Deletes a VM scale set. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of all VM scale sets under a resource group. |
| <CopyableCode code="_list_by_location" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Gets all the VM scale sets under the specified subscription for the specified location. |
| <CopyableCode code="approve_rolling_upgrade" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Approve upgrade on deferred rolling upgrades for OS disks in the virtual machines in a VM scale set. |
| <CopyableCode code="convert_to_single_placement_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Converts SinglePlacementGroup property to false for a existing virtual machine scale set. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Deallocates specific virtual machines in a VM scale set. Shuts down the virtual machines and releases the compute resources. You are not billed for the compute resources that this virtual machine scale set deallocates. |
| <CopyableCode code="force_recovery_service_fabric_platform_update_domain_walk" /> | `EXEC` | <CopyableCode code="platformUpdateDomain, resourceGroupName, subscriptionId, vmScaleSetName" /> | Manual platform update domain walk to update virtual machines in a service fabric virtual machine scale set. |
| <CopyableCode code="perform_maintenance" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Perform maintenance on one or more virtual machines in a VM scale set. Operation on instances which are not eligible for perform maintenance will be failed. Please refer to best practices for more details: https://docs.microsoft.com/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-maintenance-notifications |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Power off (stop) one or more virtual machines in a VM scale set. Note that resources are still attached and you are getting charged for the resources. Instead, use deallocate to release resources and avoid charges. |
| <CopyableCode code="reapply" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Reapplies the Virtual Machine Scale Set Virtual Machine Profile to the Virtual Machine Instances |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, and powers them back on. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Reimages (upgrade the operating system) one or more virtual machines in a VM scale set which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state. |
| <CopyableCode code="reimage_all" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set. This operation is only supported for managed disks. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Restarts one or more virtual machines in a VM scale set. |
| <CopyableCode code="set_orchestration_service_state" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName, data__action, data__serviceName" /> | Changes ServiceState property for a given service |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Starts one or more virtual machines in a VM scale set. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmScaleSetName" /> | Update a VM scale set. |

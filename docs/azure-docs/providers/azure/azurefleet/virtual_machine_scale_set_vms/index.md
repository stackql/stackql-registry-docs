---
title: virtual_machine_scale_set_vms
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vms
  - azurefleet
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azurefleet.virtual_machine_scale_set_vms" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Etag is property returned in Update/Get response of the VMSS VM, so that customer can supply it in the header to ensure optimistic updates. |
| <CopyableCode code="identity" /> | `object` | Identity for the virtual machine. |
| <CopyableCode code="instanceId" /> | `string` | The virtual machine instance ID. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="plan" /> | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a virtual machine scale set virtual machine. |
| <CopyableCode code="resources" /> | `array` | The virtual machine child extension resources. |
| <CopyableCode code="sku" /> | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | The virtual machine zones. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Gets a virtual machine from a VM scale set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineScaleSetName" /> | Gets a list of all virtual machines in a VM scale sets. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Deletes a virtual machine from a VM scale set. |
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
| <CopyableCode code="simulate_eviction" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | The operation to simulate the eviction of spot virtual machine in a VM scale set. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Starts a virtual machine in a VM scale set. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | Updates a virtual machine of a VM scale set. |

---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azurefleet.virtual_machines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="etag" /> | `string` | Etag is property returned in Create/Update/Get response of the VM, so that customer can supply it in the header to ensure optimistic updates. |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Identity for the virtual machine. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="managedBy" /> | `string` | ManagedBy is set to Virtual Machine Scale Set(VMSS) flex ARM resourceID, if the VM is part of the VMSS. This property is used by platform for internal resource group delete optimization. |
| <CopyableCode code="plan" /> | `object` | Specifies information about the marketplace image used to create the virtual machine. This element is only used for marketplace images. Before you can use a marketplace image from an API, you must enable the image for programmatic use.  In the Azure portal, find the marketplace image that you want to use and then click **Want to deploy programmatically, Get Started -&gt;**. Enter any required information and then click **Save**. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine. |
| <CopyableCode code="resources" /> | `array` | The virtual machine child extension resources. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
| <CopyableCode code="zones" /> | `array` | The virtual machine zones. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Retrieves information about the model view or the instance view of a virtual machine. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the virtual machines in the specified resource group. Use the nextLink property in the response to get the next page of virtual machines. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets all the virtual machines under the specified subscription for the specified location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to create or update a virtual machine. Please note some properties can be set only during virtual machine creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to delete a virtual machine. |
| <CopyableCode code="assess_patches" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Assess patches on the VM. |
| <CopyableCode code="attach_detach_data_disks" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Attach and detach data disks to/from the virtual machine. |
| <CopyableCode code="capture" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName, data__destinationContainerName, data__overwriteVhds, data__vhdPrefix" /> | Captures the VM by copying virtual hard disks of the VM and outputs a template that can be used to create similar VMs. |
| <CopyableCode code="convert_to_managed_disks" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Converts virtual machine disks from blob-based to managed disks. Virtual machine must be stop-deallocated before invoking this operation. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Shuts down the virtual machine and releases the compute resources. You are not billed for the compute resources that this virtual machine uses. |
| <CopyableCode code="generalize" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Sets the OS state of the virtual machine to generalized. It is recommended to sysprep the virtual machine before performing this operation. For Windows, please refer to [Create a managed image of a generalized VM in Azure](https://docs.microsoft.com/azure/virtual-machines/windows/capture-image-resource). For Linux, please refer to [How to create an image of a virtual machine or VHD](https://docs.microsoft.com/azure/virtual-machines/linux/capture-image). |
| <CopyableCode code="install_patches" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName, data__rebootSetting" /> | Installs patches on the VM. |
| <CopyableCode code="instance_view" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Retrieves information about the run-time state of a virtual machine. |
| <CopyableCode code="perform_maintenance" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to perform maintenance on a virtual machine. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to power off (stop) a virtual machine. The virtual machine can be restarted with the same provisioned resources. You are still charged for this virtual machine. |
| <CopyableCode code="reapply" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to reapply a virtual machine's state. |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Shuts down the virtual machine, moves it to a new node, and powers it back on. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Reimages (upgrade the operating system) a virtual machine which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state. NOTE: The retaining of old OS disk depends on the value of deleteOption of OS disk. If deleteOption is detach, the old OS disk will be preserved after reimage. If deleteOption is delete, the old OS disk will be deleted after reimage. The deleteOption of the OS disk should be updated accordingly before performing the reimage. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to restart a virtual machine. |
| <CopyableCode code="retrieve_boot_diagnostics_data" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to retrieve SAS URIs for a virtual machine's boot diagnostic logs. |
| <CopyableCode code="simulate_eviction" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to simulate the eviction of spot virtual machine. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to start a virtual machine. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to update a virtual machine. |

---
title: virtual_machine
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine
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
<tr><td><b>Name</b></td><td><code>virtual_machine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assignedHost" /> | `string` | Resource id of the dedicated host, on which the virtual machine is allocated through automatic placement, when the virtual machine is associated with a dedicated host group that has automatic placement enabled. Minimum api-version: 2020-06-01. |
| <CopyableCode code="bootDiagnostics" /> | `object` | The instance view of a virtual machine boot diagnostics. |
| <CopyableCode code="computerName" /> | `string` | The computer name assigned to the virtual machine. |
| <CopyableCode code="disks" /> | `array` | The virtual machine disk information. |
| <CopyableCode code="extensions" /> | `array` | The extensions information. |
| <CopyableCode code="hyperVGeneration" /> | `string` | Specifies the HyperVGeneration Type associated with a resource |
| <CopyableCode code="isVMInStandbyPool" /> | `boolean` | [Preview Feature] Specifies whether the VM is currently in or out of the Standby Pool. |
| <CopyableCode code="maintenanceRedeployStatus" /> | `object` | Maintenance Operation Status. |
| <CopyableCode code="osName" /> | `string` | The Operating System running on the virtual machine. |
| <CopyableCode code="osVersion" /> | `string` | The version of Operating System running on the virtual machine. |
| <CopyableCode code="patchStatus" /> | `object` | The status of virtual machine patch operations. |
| <CopyableCode code="platformFaultDomain" /> | `integer` | Specifies the fault domain of the virtual machine. |
| <CopyableCode code="platformUpdateDomain" /> | `integer` | Specifies the update domain of the virtual machine. |
| <CopyableCode code="rdpThumbPrint" /> | `string` | The Remote desktop certificate thumbprint. |
| <CopyableCode code="statuses" /> | `array` | The resource status information. |
| <CopyableCode code="vmAgent" /> | `object` | The instance view of the VM Agent running on the virtual machine. |
| <CopyableCode code="vmHealth" /> | `object` | The health status of the VM. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Retrieves information about the run-time state of a virtual machine. |
| <CopyableCode code="assess_patches" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Assess patches on the VM. |
| <CopyableCode code="attach_detach_data_disks" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Attach and detach data disks to/from the virtual machine. |
| <CopyableCode code="capture" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName, data__destinationContainerName, data__overwriteVhds, data__vhdPrefix" /> | Captures the VM by copying virtual hard disks of the VM and outputs a template that can be used to create similar VMs. |
| <CopyableCode code="convert_to_managed_disks" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Converts virtual machine disks from blob-based to managed disks. Virtual machine must be stop-deallocated before invoking this operation. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Shuts down the virtual machine and releases the compute resources. You are not billed for the compute resources that this virtual machine uses. |
| <CopyableCode code="generalize" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Sets the OS state of the virtual machine to generalized. It is recommended to sysprep the virtual machine before performing this operation. For Windows, please refer to [Create a managed image of a generalized VM in Azure](https://docs.microsoft.com/azure/virtual-machines/windows/capture-image-resource). For Linux, please refer to [How to create an image of a virtual machine or VHD](https://docs.microsoft.com/azure/virtual-machines/linux/capture-image). |
| <CopyableCode code="install_patches" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName, data__rebootSetting" /> | Installs patches on the VM. |
| <CopyableCode code="perform_maintenance" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to perform maintenance on a virtual machine. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to power off (stop) a virtual machine. The virtual machine can be restarted with the same provisioned resources. You are still charged for this virtual machine. |
| <CopyableCode code="reapply" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to reapply a virtual machine's state. |
| <CopyableCode code="redeploy" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Shuts down the virtual machine, moves it to a new node, and powers it back on. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Reimages (upgrade the operating system) a virtual machine which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state. NOTE: The retaining of old OS disk depends on the value of deleteOption of OS disk. If deleteOption is detach, the old OS disk will be preserved after reimage. If deleteOption is delete, the old OS disk will be deleted after reimage. The deleteOption of the OS disk should be updated accordingly before performing the reimage. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to restart a virtual machine. |
| <CopyableCode code="retrieve_boot_diagnostics_data" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to retrieve SAS URIs for a virtual machine's boot diagnostic logs. |
| <CopyableCode code="run_command" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName, data__commandId" /> | Run command on the VM. |
| <CopyableCode code="simulate_eviction" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to simulate the eviction of spot virtual machine. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to start a virtual machine. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | The operation to update a virtual machine. |

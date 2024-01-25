---
title: virtual_machine_scale_set_vms_instance_view
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vms_instance_view
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
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vms_instance_view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_scale_set_vms_instance_view</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `assignedHost` | `string` | Resource id of the dedicated host, on which the virtual machine is allocated through automatic placement, when the virtual machine is associated with a dedicated host group that has automatic placement enabled. Minimum api-version: 2020-06-01. |
| `bootDiagnostics` | `object` | The instance view of a virtual machine boot diagnostics. |
| `computerName` | `string` | Specifies the host OS name of the virtual machine. &lt;br&gt;&lt;br&gt; This name cannot be updated after the VM is created. &lt;br&gt;&lt;br&gt; **Max-length (Windows):** 15 characters &lt;br&gt;&lt;br&gt; **Max-length (Linux):** 64 characters. &lt;br&gt;&lt;br&gt; For naming conventions and restrictions see [Azure infrastructure services implementation guidelines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-infrastructure-subscription-accounts-guidelines?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json#1-naming-conventions). |
| `disks` | `array` | The disks information. |
| `extensions` | `array` | The extensions information. |
| `hyperVGeneration` | `string` | The hypervisor generation of the Virtual Machine [V1, V2] |
| `maintenanceRedeployStatus` | `object` | Maintenance Operation Status. |
| `osName` | `string` | The Operating System running on the hybrid machine. |
| `osVersion` | `string` | The version of Operating System running on the hybrid machine. |
| `placementGroupId` | `string` | The placement group in which the VM is running. If the VM is deallocated it will not have a placementGroupId. |
| `platformFaultDomain` | `integer` | The Fault Domain count. |
| `platformUpdateDomain` | `integer` | The Update Domain count. |
| `rdpThumbPrint` | `string` | The Remote desktop certificate thumbprint. |
| `statuses` | `array` | The resource status information. |
| `vmAgent` | `object` | The instance view of the VM Agent running on the virtual machine. |
| `vmHealth` | `object` | The health status of the VM. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `instanceId, resourceGroupName, subscriptionId, vmScaleSetName` |

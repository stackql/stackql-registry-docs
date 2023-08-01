---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - dev_test_labs
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.virtual_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | Properties of a virtual machine. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachines_Get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId` | Get virtual machine. |
| `VirtualMachines_List` | `SELECT` | `api-version, labName, resourceGroupName, subscriptionId` | List virtual machines in a given lab. |
| `VirtualMachines_CreateOrUpdate` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId, data__properties` | Create or replace an existing virtual machine. This operation can take a while to complete. |
| `VirtualMachines_Delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId` | Delete virtual machine. This operation can take a while to complete. |
| `VirtualMachines_AddDataDisk` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Attach a new or existing data disk to virtual machine. This operation can take a while to complete. |
| `VirtualMachines_ApplyArtifacts` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Apply artifacts to virtual machine. This operation can take a while to complete. |
| `VirtualMachines_Claim` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Take ownership of an existing virtual machine This operation can take a while to complete. |
| `VirtualMachines_DetachDataDisk` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Detach the specified disk from the virtual machine. This operation can take a while to complete. |
| `VirtualMachines_GetRdpFileContents` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Gets a string that represents the contents of the RDP file for the virtual machine |
| `VirtualMachines_ListApplicableSchedules` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Lists the applicable start/stop schedules, if any. |
| `VirtualMachines_Redeploy` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Redeploy a virtual machine This operation can take a while to complete. |
| `VirtualMachines_Resize` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Resize Virtual Machine. This operation can take a while to complete. |
| `VirtualMachines_Restart` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Restart a virtual machine. This operation can take a while to complete. |
| `VirtualMachines_Start` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Start a virtual machine. This operation can take a while to complete. |
| `VirtualMachines_Stop` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Stop a virtual machine This operation can take a while to complete. |
| `VirtualMachines_TransferDisks` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Transfers all data disks attached to the virtual machine to be owned by the current user. This operation can take a while to complete. |
| `VirtualMachines_UnClaim` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Release ownership of an existing virtual machine This operation can take a while to complete. |
| `VirtualMachines_Update` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Allows modifying tags of virtual machines. All other properties will be ignored. |

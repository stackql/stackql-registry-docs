---
title: virtual_machine_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_schedules
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
<tr><td><b>Name</b></td><td><code>virtual_machine_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.virtual_machine_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a schedule. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachineSchedules_Get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId, virtualMachineName` | Get schedule. |
| `VirtualMachineSchedules_List` | `SELECT` | `api-version, labName, resourceGroupName, subscriptionId, virtualMachineName` | List schedules in a given virtual machine. |
| `VirtualMachineSchedules_CreateOrUpdate` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId, virtualMachineName, data__properties` | Create or replace an existing schedule. |
| `VirtualMachineSchedules_Delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId, virtualMachineName` | Delete schedule. |
| `VirtualMachineSchedules_Execute` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, virtualMachineName` | Execute a schedule. This operation can take a while to complete. |
| `VirtualMachineSchedules_Update` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, virtualMachineName` | Allows modifying tags of schedules. All other properties will be ignored. |

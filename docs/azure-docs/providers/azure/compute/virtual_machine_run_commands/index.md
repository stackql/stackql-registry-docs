---
title: virtual_machine_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_run_commands
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
<tr><td><b>Name</b></td><td><code>virtual_machine_run_commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.virtual_machine_run_commands</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The VM run command id. |
| `description` | `string` | The VM run command description. |
| `$schema` | `string` | The VM run command schema. |
| `label` | `string` | The VM run command label. |
| `osType` | `string` | The Operating System type. |
| `parameters` | `array` | The parameters used by the script. |
| `script` | `array` | The script to be executed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `commandId, location, subscriptionId` | Gets specific run command for a subscription in a location. |
| `list` | `SELECT` | `location, subscriptionId` | Lists all available run commands for a subscription in a location. |
| `list_by_virtual_machine` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | The operation to get all run commands of a Virtual Machine. |
| `create_or_update` | `INSERT` | `resourceGroupName, runCommandName, subscriptionId, vmName` | The operation to create or update the run command. |
| `delete` | `DELETE` | `resourceGroupName, runCommandName, subscriptionId, vmName` | The operation to delete the run command. |
| `_list` | `EXEC` | `location, subscriptionId` | Lists all available run commands for a subscription in a location. |
| `_list_by_virtual_machine` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | The operation to get all run commands of a Virtual Machine. |
| `get_by_virtual_machine` | `EXEC` | `resourceGroupName, runCommandName, subscriptionId, vmName` | The operation to get the run command. |
| `update` | `EXEC` | `resourceGroupName, runCommandName, subscriptionId, vmName` | The operation to update the run command. |

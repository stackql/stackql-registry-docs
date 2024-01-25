---
title: machine_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_run_commands
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>machine_run_commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.machine_run_commands</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of a run command. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `machineName, resourceGroupName, runCommandName, subscriptionId` | The operation to get a run command. |
| `list` | `SELECT` | `machineName, resourceGroupName, subscriptionId` | The operation to get all the run commands of a non-Azure machine. |
| `create_or_update` | `INSERT` | `machineName, resourceGroupName, runCommandName, subscriptionId` | The operation to create or update a run command. |
| `delete` | `DELETE` | `machineName, resourceGroupName, runCommandName, subscriptionId` | The operation to delete a run command. |
| `_list` | `EXEC` | `machineName, resourceGroupName, subscriptionId` | The operation to get all the run commands of a non-Azure machine. |
| `update` | `EXEC` | `machineName, resourceGroupName, runCommandName, subscriptionId` | The operation to update the run command. |

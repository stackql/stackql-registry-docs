---
title: bare_metal_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_machines
  - nexus
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
<tr><td><b>Name</b></td><td><code>bare_metal_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.nexus.bare_metal_machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Get properties of the provided bare metal machine. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get a list of bare metal machines in the provided resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get a list of bare metal machines in the provided subscription. |
| `create_or_update` | `INSERT` | `bareMetalMachineName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties` | Create a new bare metal machine or update the properties of the existing one.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| `delete` | `DELETE` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Delete the provided bare metal machine.<br />All customer initiated requests will be rejected as the life cycle of this resource is managed by the system. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get a list of bare metal machines in the provided resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get a list of bare metal machines in the provided subscription. |
| `cordon` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Cordon the provided bare metal machine's Kubernetes node. |
| `power_off` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Power off the provided bare metal machine. |
| `reimage` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Reimage the provided bare metal machine. |
| `replace` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Replace the provided bare metal machine. |
| `restart` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Restart the provided bare metal machine. |
| `run_command` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId, data__limitTimeSeconds, data__script` | Run the command or the script on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available. |
| `run_data_extracts` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId, data__commands, data__limitTimeSeconds` | Run one or more data extractions on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available. |
| `run_read_commands` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId, data__commands, data__limitTimeSeconds` | Run one or more read-only commands on the provided bare metal machine. The URL to storage account with the command execution results and the command exit code can be retrieved from the operation status API once available. |
| `start` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Start the provided bare metal machine. |
| `uncordon` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Uncordon the provided bare metal machine's Kubernetes node. |
| `update` | `EXEC` | `bareMetalMachineName, resourceGroupName, subscriptionId` | Patch properties of the provided bare metal machine, or update tags associated with the bare metal machine. Properties and tag updates can be done independently. |

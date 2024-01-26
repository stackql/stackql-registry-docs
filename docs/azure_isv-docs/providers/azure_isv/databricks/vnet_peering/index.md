---
title: vnet_peering
hide_title: false
hide_table_of_contents: false
keywords:
  - vnet_peering
  - databricks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>vnet_peering</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.databricks.vnet_peering</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the virtual network peering resource |
| `properties` | `object` | Properties of the virtual network peering. |
| `type` | `string` | type of the virtual network peering resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `peeringName, resourceGroupName, subscriptionId, workspaceName` | Gets the workspace vNet Peering. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Lists the workspace vNet Peerings. |
| `create_or_update` | `INSERT` | `peeringName, resourceGroupName, subscriptionId, workspaceName, data__properties` | Creates vNet Peering for workspace. |
| `delete` | `DELETE` | `peeringName, resourceGroupName, subscriptionId, workspaceName` | Deletes the workspace vNetPeering. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Lists the workspace vNet Peerings. |

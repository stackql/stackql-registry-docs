---
title: network_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_functions
  - mpc_network_function
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
<tr><td><b>Name</b></td><td><code>network_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mpc_network_function.network_functions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network Function Properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkFunctionName, resourceGroupName, subscriptionId` | Get a NetworkFunctionResource |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List NetworkFunctionResource resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List NetworkFunctionResource resources by subscription ID |
| `create_or_update` | `INSERT` | `networkFunctionName, resourceGroupName, subscriptionId` | Create a NetworkFunctionResource |
| `delete` | `DELETE` | `networkFunctionName, resourceGroupName, subscriptionId` | Delete a NetworkFunctionResource |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List NetworkFunctionResource resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List NetworkFunctionResource resources by subscription ID |

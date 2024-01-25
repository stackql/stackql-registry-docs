---
title: network_function_definition_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - network_function_definition_groups
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>network_function_definition_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.network_function_definition_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network function definition group properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkFunctionDefinitionGroupName, publisherName, resourceGroupName, subscriptionId` | Gets information about the specified networkFunctionDefinition group. |
| `list_by_publisher` | `SELECT` | `publisherName, resourceGroupName, subscriptionId` | Gets information of the network function definition groups under a publisher. |
| `create_or_update` | `INSERT` | `networkFunctionDefinitionGroupName, publisherName, resourceGroupName, subscriptionId` | Creates or updates a network function definition group. |
| `delete` | `DELETE` | `networkFunctionDefinitionGroupName, publisherName, resourceGroupName, subscriptionId` | Deletes a specified network function definition group. |
| `_list_by_publisher` | `EXEC` | `publisherName, resourceGroupName, subscriptionId` | Gets information of the network function definition groups under a publisher. |
| `update` | `EXEC` | `networkFunctionDefinitionGroupName, publisherName, resourceGroupName, subscriptionId` | Updates a network function definition group resource. |

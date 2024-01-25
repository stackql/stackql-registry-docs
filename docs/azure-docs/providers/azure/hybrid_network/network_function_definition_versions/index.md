---
title: network_function_definition_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_function_definition_versions
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
<tr><td><b>Name</b></td><td><code>network_function_definition_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.network_function_definition_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network function definition version properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId` | Gets information about a network function definition version. |
| `list_by_network_function_definition_group` | `SELECT` | `networkFunctionDefinitionGroupName, publisherName, resourceGroupName, subscriptionId` | Gets information about a list of network function definition versions under a network function definition group. |
| `create_or_update` | `INSERT` | `networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId` | Creates or updates a network function definition version. |
| `delete` | `DELETE` | `networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId` | Deletes the specified network function definition version. |
| `_list_by_network_function_definition_group` | `EXEC` | `networkFunctionDefinitionGroupName, publisherName, resourceGroupName, subscriptionId` | Gets information about a list of network function definition versions under a network function definition group. |
| `update` | `EXEC` | `networkFunctionDefinitionGroupName, networkFunctionDefinitionVersionName, publisherName, resourceGroupName, subscriptionId` | Updates a network function definition version resource. |

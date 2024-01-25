---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - ml_experimentation
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_experimentation.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
| `properties` | `object` | The properties of a machine learning team account. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the properties of the specified machine learning team account. |
| `list` | `SELECT` | `subscriptionId` | Lists all the available machine learning team accounts under the specified subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the available machine learning team accounts under the specified resource group. |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates a team account with the specified parameters. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes a machine learning team account. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the available machine learning team accounts under the specified subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the available machine learning team accounts under the specified resource group. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates a machine learning team account with the specified parameters. |

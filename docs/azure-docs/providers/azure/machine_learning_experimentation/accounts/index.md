---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - machine_learning_experimentation
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
<tr><td><b>Id</b></td><td><code>azure.machine_learning_experimentation.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | The properties of a machine learning team account. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the properties of the specified machine learning team account. |
| `Accounts_List` | `SELECT` | `subscriptionId` | Lists all the available machine learning team accounts under the specified subscription. |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the available machine learning team accounts under the specified resource group. |
| `Accounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates a team account with the specified parameters. |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes a machine learning team account. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates a machine learning team account with the specified parameters. |

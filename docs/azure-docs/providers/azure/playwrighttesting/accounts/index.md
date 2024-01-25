---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - playwrighttesting
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
<tr><td><b>Id</b></td><td><code>azure.playwrighttesting.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Account properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Get a Account |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List Account resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Account resources by subscription ID |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId` | Create a Account |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Delete a Account |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List Account resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Account resources by subscription ID |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Update a Account |

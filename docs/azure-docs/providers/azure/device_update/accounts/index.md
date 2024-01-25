---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - device_update
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
<tr><td><b>Id</b></td><td><code>azure.device_update.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Device Update account properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Returns account details for the given account name. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of Accounts. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Returns list of Accounts. |
| `create` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates Account. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes account. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns list of Accounts. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Returns list of Accounts. |
| `head` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Checks whether account exists. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates account's patchable properties |

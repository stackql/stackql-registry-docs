---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - purview
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
<tr><td><b>Id</b></td><td><code>azure.purview.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the identifier. |
| `name` | `string` | Gets or sets the name. |
| `identity` | `object` | The Managed Identity of the resource |
| `location` | `string` | Gets or sets the location. |
| `properties` | `object` | The account properties |
| `sku` | `object` | Gets or sets the Sku. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Tags on the azure resource. |
| `type` | `string` | Gets or sets the type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Get an account |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List accounts in ResourceGroup |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | List accounts in Subscription |
| `create_or_update` | `INSERT` | `accountName, api-version, resourceGroupName, subscriptionId` | Creates or updates an account |
| `delete` | `DELETE` | `accountName, api-version, resourceGroupName, subscriptionId` | Deletes an account resource |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | List accounts in ResourceGroup |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | List accounts in Subscription |
| `add_root_collection_admin` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Add the administrator for root collection associated with this account. |
| `check_name_availability` | `EXEC` | `api-version, subscriptionId` | Checks if account name is available. |
| `update` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Updates an account |

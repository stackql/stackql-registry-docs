---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - data_share
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
<tr><td><b>Id</b></td><td><code>azure.data_share.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity of resource |
| `location` | `string` | Location of the azure resource. |
| `properties` | `object` | Account property bag. |
| `tags` | `object` | Tags on the azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Get an account |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List Accounts in ResourceGroup |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | List Accounts in Subscription |
| `create` | `INSERT` | `accountName, api-version, resourceGroupName, subscriptionId, data__identity` | Create an account |
| `delete` | `DELETE` | `accountName, api-version, resourceGroupName, subscriptionId` | DeleteAccount |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | List Accounts in ResourceGroup |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | List Accounts in Subscription |
| `update` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Patch an account |

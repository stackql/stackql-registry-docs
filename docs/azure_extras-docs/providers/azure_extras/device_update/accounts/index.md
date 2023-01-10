---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - device_update
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.device_update.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Device Update account properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Returns account details for the given account name. |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of Accounts. |
| `Accounts_ListBySubscription` | `SELECT` | `subscriptionId` | Returns list of Accounts. |
| `Accounts_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates Account. |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes account. |
| `Accounts_Head` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Checks whether account exists. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates account's patchable properties |

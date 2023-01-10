---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - data_share
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
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Account property bag. |
| `tags` | `object` | Tags on the azure resource. |
| `identity` | `object` | Identity of resource |
| `location` | `string` | Location of the azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_Get` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Get an account |
| `Accounts_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List Accounts in ResourceGroup |
| `Accounts_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | List Accounts in Subscription |
| `Accounts_Create` | `INSERT` | `accountName, api-version, resourceGroupName, subscriptionId, data__identity` | Create an account |
| `Accounts_Delete` | `DELETE` | `accountName, api-version, resourceGroupName, subscriptionId` | DeleteAccount |
| `Accounts_Update` | `EXEC` | `accountName, api-version, resourceGroupName, subscriptionId` | Patch an account |

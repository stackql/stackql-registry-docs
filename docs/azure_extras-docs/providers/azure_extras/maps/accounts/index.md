---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - maps
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
<tr><td><b>Id</b></td><td><code>azure_extras.maps.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | The Kind of the Maps Account. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Additional Map account properties |
| `sku` | `object` | The SKU of the Maps Account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Get a Maps Account. |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all Maps Accounts in a Resource Group |
| `Accounts_ListBySubscription` | `SELECT` | `subscriptionId` | Get all Maps Accounts in a Subscription |
| `Accounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__sku` | Create or update a Maps Account. A Maps Account holds the keys which allow access to the Maps REST APIs. |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete a Maps Account. |
| `Accounts_ListKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Get the keys to use with the Maps APIs. A key is used to authenticate and authorize access to the Maps REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration. |
| `Accounts_ListSas` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__expiry, data__maxRatePerSecond, data__principalId, data__signingKey, data__start` | Create and list an account shared access signature token. Use this SAS token for authentication to Azure Maps REST APIs through various Azure Maps SDKs. As prerequisite to create a SAS Token. <br /><br />Prerequisites:<br />1. Create or have an existing User Assigned Managed Identity in the same Azure region as the account. <br />2. Create or update an Azure Map account with the same Azure region as the User Assigned Managed Identity is placed. |
| `Accounts_RegenerateKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyType` | Regenerate either the primary or secondary key for use with the Maps APIs. The old key will stop working immediately. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates a Maps Account. Only a subset of the parameters may be updated after creation, such as Sku, Tags, Properties. |

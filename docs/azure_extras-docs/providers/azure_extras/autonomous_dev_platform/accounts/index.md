---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - autonomous_dev_platform
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
<tr><td><b>Id</b></td><td><code>azure_extras.autonomous_dev_platform.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | ADP account properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the properties of an ADP account |
| `Accounts_List` | `SELECT` | `subscriptionId` | List all ADP accounts available under the subscription |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all ADP accounts available under the resource group |
| `Accounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates an ADP account |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes an ADP account |
| `Accounts_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the account name is valid and is not already in use |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the properties of an existing ADP account |

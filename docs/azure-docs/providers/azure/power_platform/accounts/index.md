---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - power_platform
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
<tr><td><b>Id</b></td><td><code>azure.power_platform.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The properties that define configuration for the account. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Get information about an account. |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve a list of accounts within a given resource group. |
| `Accounts_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieve a list of accounts within a subscription. |
| `Accounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates an account. |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete an account. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates an account. |

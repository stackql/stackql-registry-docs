---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - data_lake_analytics
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
<tr><td><b>Id</b></td><td><code>azure.data_lake_analytics.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `type` | `string` | The resource type. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The account specific properties that are associated with an underlying Data Lake Analytics account. Returned only when retrieving a specific account. |
| `tags` | `object` | The resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Accounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets details of the specified Data Lake Analytics account. |
| `Accounts_List` | `SELECT` | `subscriptionId` | Gets the first page of Data Lake Analytics accounts, if any, within the current subscription. This includes a link to the next page, if any. |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the first page of Data Lake Analytics accounts, if any, within a specific resource group. This includes a link to the next page, if any. |
| `Accounts_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__location, data__properties` | Creates the specified Data Lake Analytics account. This supplies the user with computation services for Data Lake Analytics workloads. |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Begins the delete process for the Data Lake Analytics account object specified by the account name. |
| `Accounts_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks whether the specified account name is available or taken. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the Data Lake Analytics account object specified by the accountName with the contents of the account object. |

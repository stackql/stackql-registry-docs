---
title: data_lake_store_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lake_store_accounts
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
<tr><td><b>Name</b></td><td><code>data_lake_store_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_lake_analytics.data_lake_store_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The Data Lake Store account properties. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataLakeStoreAccounts_Get` | `SELECT` | `accountName, dataLakeStoreAccountName, resourceGroupName, subscriptionId` | Gets the specified Data Lake Store account details in the specified Data Lake Analytics account. |
| `DataLakeStoreAccounts_ListByAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the first page of Data Lake Store accounts linked to the specified Data Lake Analytics account. The response includes a link to the next page, if any. |
| `DataLakeStoreAccounts_Add` | `INSERT` | `accountName, dataLakeStoreAccountName, resourceGroupName, subscriptionId` | Updates the specified Data Lake Analytics account to include the additional Data Lake Store account. |
| `DataLakeStoreAccounts_Delete` | `DELETE` | `accountName, dataLakeStoreAccountName, resourceGroupName, subscriptionId` | Updates the Data Lake Analytics account specified to remove the specified Data Lake Store account. |

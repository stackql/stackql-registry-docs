---
title: storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_accounts
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
<tr><td><b>Name</b></td><td><code>storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_lake_analytics.storage_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The Azure Storage account properties. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, storageAccountName, subscriptionId` | Gets the specified Azure Storage account linked to the given Data Lake Analytics account. |
| `list_by_account` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the first page of Azure Storage accounts, if any, linked to the specified Data Lake Analytics account. The response includes a link to the next page, if any. |
| `add` | `INSERT` | `accountName, resourceGroupName, storageAccountName, subscriptionId, data__properties` | Updates the specified Data Lake Analytics account to add an Azure Storage account. |
| `delete` | `DELETE` | `accountName, resourceGroupName, storageAccountName, subscriptionId` | Updates the specified Data Lake Analytics account to remove an Azure Storage account. |
| `_list_by_account` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets the first page of Azure Storage accounts, if any, linked to the specified Data Lake Analytics account. The response includes a link to the next page, if any. |
| `update` | `EXEC` | `accountName, resourceGroupName, storageAccountName, subscriptionId` | Updates the Data Lake Analytics account to replace Azure Storage blob account details, such as the access key and/or suffix. |

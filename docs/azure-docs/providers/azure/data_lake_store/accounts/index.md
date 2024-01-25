---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - data_lake_store
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
<tr><td><b>Id</b></td><td><code>azure.data_lake_store.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `identity` | `object` | The encryption identity properties. |
| `location` | `string` | The resource location. |
| `properties` | `object` | Data Lake Store account properties information. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the specified Data Lake Store account. |
| `list` | `SELECT` | `subscriptionId` | Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any. |
| `create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__location` | Creates the specified Data Lake Store account. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes the specified Data Lake Store account. |
| `_list` | `EXEC` | `subscriptionId` | Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any. |
| `check_name_availability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks whether the specified account name is available or taken. |
| `enable_key_vault` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Attempts to enable a user managed Key Vault for encryption of the specified Data Lake Store account. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the specified Data Lake Store account information. |

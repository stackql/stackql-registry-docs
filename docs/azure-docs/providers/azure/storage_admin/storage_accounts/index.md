---
title: storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_accounts
  - storage_admin
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
<tr><td><b>Id</b></td><td><code>azure.storage_admin.storage_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource Name. |
| `properties` | `object` | Properties of a storage account. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource Type. |
| `kind` | `string` | The kind of storage account |
| `location` | `string` | Resource Location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageAccounts_Get` | `SELECT` | `accountId, location, subscriptionId` | Returns the requested storage account. |
| `StorageAccounts_List` | `SELECT` | `location, subscriptionId` | Returns a list of storage accounts. |
| `StorageAccounts_ReclaimStorageCapacity` | `EXEC` | `location, subscriptionId` | Start reclaim storage capacity on deleted storage objects. |
| `StorageAccounts_Undelete` | `EXEC` | `accountId, location, subscriptionId` | Undelete a deleted storage account with new account name if the a new name is provided. |

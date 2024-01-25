---
title: storage_account_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_account_credentials
  - storsimple_8000_series
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
<tr><td><b>Name</b></td><td><code>storage_account_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.storage_account_credentials</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `properties` | `object` | The storage account credential properties. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managerName, resourceGroupName, storageAccountCredentialName, subscriptionId` | Gets the properties of the specified storage account credential name. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Gets all the storage account credentials in a manager. |
| `create_or_update` | `INSERT` | `managerName, resourceGroupName, storageAccountCredentialName, subscriptionId, data__properties` | Creates or updates the storage account credential. |
| `delete` | `DELETE` | `managerName, resourceGroupName, storageAccountCredentialName, subscriptionId` | Deletes the storage account credential. |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Gets all the storage account credentials in a manager. |

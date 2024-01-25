---
title: storage_account_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_account_credentials
  - storsimple_1200_series
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
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.storage_account_credentials</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | Storage account properties |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `credentialName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified storage account credential name. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the storage account credentials in a manager. |
| `create_or_update` | `INSERT` | `credentialName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the storage account credential |
| `delete` | `DELETE` | `credentialName, managerName, resourceGroupName, subscriptionId` | Deletes the storage account credential |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the storage account credentials in a manager. |

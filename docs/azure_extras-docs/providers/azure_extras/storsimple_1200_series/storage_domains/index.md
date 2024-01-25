---
title: storage_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_domains
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
<tr><td><b>Name</b></td><td><code>storage_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.storage_domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | The storage domain properties. |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managerName, resourceGroupName, storageDomainName, subscriptionId` | Returns the properties of the specified storage domain name. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the storage domains in a manager. |
| `create_or_update` | `INSERT` | `managerName, resourceGroupName, storageDomainName, subscriptionId, data__properties` | Creates or updates the storage domain. |
| `delete` | `DELETE` | `managerName, resourceGroupName, storageDomainName, subscriptionId` | Deletes the storage domain. |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the storage domains in a manager. |

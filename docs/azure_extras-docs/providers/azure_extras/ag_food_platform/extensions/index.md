---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - ag_food_platform
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ag_food_platform.extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eTag` | `string` | The ETag value to implement optimistic concurrency. |
| `properties` | `object` | Extension resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataManagerForAgricultureResourceName, extensionId, resourceGroupName, subscriptionId` | Get installed extension details by extension id. |
| `list_by_data_manager_for_agriculture` | `SELECT` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Get installed extensions details. |
| `create_or_update` | `INSERT` | `dataManagerForAgricultureResourceName, extensionId, resourceGroupName, subscriptionId` | Install or Update extension. Additional Api Properties are merged patch and if the extension is updated to a new version then the obsolete entries will be auto deleted from Additional Api Properties. |
| `delete` | `DELETE` | `dataManagerForAgricultureResourceName, extensionId, resourceGroupName, subscriptionId` | Uninstall extension. |
| `_list_by_data_manager_for_agriculture` | `EXEC` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Get installed extensions details. |

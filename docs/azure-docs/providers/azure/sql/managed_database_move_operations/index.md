---
title: managed_database_move_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_move_operations
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_database_move_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_move_operations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationName, operationId, resourceGroupName, subscriptionId` | Gets a managed database move operation. |
| `list_by_location` | `SELECT` | `locationName, resourceGroupName, subscriptionId` | Lists managed database move operations. |
| `_list_by_location` | `EXEC` | `locationName, resourceGroupName, subscriptionId` | Lists managed database move operations. |

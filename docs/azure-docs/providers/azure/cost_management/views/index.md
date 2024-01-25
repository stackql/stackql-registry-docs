---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - cost_management
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
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `eTag` | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| `properties` | `object` | The properties of the view. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `viewName` | Gets the view by view name. |
| `list` | `SELECT` |  | Lists all views by tenant and object. |
| `list_by_scope` | `SELECT` | `scope` | Lists all views at the given scope. |
| `create_or_update` | `INSERT` | `viewName` | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| `delete` | `DELETE` | `viewName` | The operation to delete a view. |
| `delete_by_scope` | `DELETE` | `scope, viewName` | The operation to delete a view. |
| `_list` | `EXEC` |  | Lists all views by tenant and object. |
| `_list_by_scope` | `EXEC` | `scope` | Lists all views at the given scope. |
| `create_or_update_by_scope` | `EXEC` | `scope, viewName` | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| `get_by_scope` | `EXEC` | `scope, viewName` | Gets the view for the defined scope by view name. |

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
| `properties` | `object` | The properties of the view. |
| `type` | `string` | Resource type. |
| `eTag` | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Views_Get` | `SELECT` | `viewName` | Gets the view by view name. |
| `Views_List` | `SELECT` |  | Lists all views by tenant and object. |
| `Views_ListByScope` | `SELECT` | `scope` | Lists all views at the given scope. |
| `Views_CreateOrUpdate` | `INSERT` | `viewName` | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| `Views_Delete` | `DELETE` | `viewName` | The operation to delete a view. |
| `Views_DeleteByScope` | `DELETE` | `scope, viewName` | The operation to delete a view. |
| `Views_CreateOrUpdateByScope` | `EXEC` | `scope, viewName` | The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| `Views_GetByScope` | `EXEC` | `scope, viewName` | Gets the view for the defined scope by view name. |

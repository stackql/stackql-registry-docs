---
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
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
<tr><td><b>Name</b></td><td><code>exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.exports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource name. |
| `eTag` | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| `identity` | `object` | Managed service identity (either system assigned, or none) |
| `location` | `string` | The location of the Export's managed identity. Only required when utilizing managed identity. |
| `properties` | `object` | The properties of the export. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `exportName, scope` | The operation to get the export for the defined scope by export name. |
| `list` | `SELECT` | `scope` | The operation to list all exports at the given scope. |
| `create_or_update` | `INSERT` | `exportName, scope` | The operation to create or update a export. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag. |
| `delete` | `DELETE` | `exportName, scope` | The operation to delete a export. |
| `_list` | `EXEC` | `scope` | The operation to list all exports at the given scope. |
| `execute` | `EXEC` | `exportName, scope` | The operation to run an export. |

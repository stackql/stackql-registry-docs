---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - quota
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.quota.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The resource name. |
| `properties` | `object` | Usage properties for the specified resource. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceName, scope` | Get the current usage of a resource. |
| `list` | `SELECT` | `scope` | Get a list of current usage for all resources for the scope specified. |
| `_list` | `EXEC` | `scope` | Get a list of current usage for all resources for the scope specified. |

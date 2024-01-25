---
title: dev_box_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_box_definitions
  - dev_center
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
<tr><td><b>Name</b></td><td><code>dev_box_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_center.dev_box_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of a Dev Box definition. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Gets a Dev Box definition |
| `list_by_dev_center` | `SELECT` |  | List Dev Box definitions for a devcenter. |
| `list_by_project` | `SELECT` |  | List Dev Box definitions configured for a project. |
| `create_or_update` | `INSERT` |  | Creates or updates a Dev Box definition. |
| `delete` | `DELETE` |  | Deletes a Dev Box definition |
| `_list_by_dev_center` | `EXEC` |  | List Dev Box definitions for a devcenter. |
| `_list_by_project` | `EXEC` |  | List Dev Box definitions configured for a project. |
| `get_by_project` | `EXEC` |  | Gets a Dev Box definition configured for a project |
| `update` | `EXEC` |  | Partially updates a Dev Box definition. |

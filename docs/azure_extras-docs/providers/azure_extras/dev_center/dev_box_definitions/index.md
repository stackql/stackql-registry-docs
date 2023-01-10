---
title: dev_box_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_box_definitions
  - dev_center
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
<tr><td><b>Name</b></td><td><code>dev_box_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.dev_box_definitions</code></td></tr>
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
| `DevBoxDefinitions_Get` | `SELECT` |  | Gets a Dev Box definition |
| `DevBoxDefinitions_ListByDevCenter` | `SELECT` |  | List Dev Box definitions for a devcenter. |
| `DevBoxDefinitions_ListByProject` | `SELECT` |  | List Dev Box definitions configured for a project. |
| `DevBoxDefinitions_CreateOrUpdate` | `INSERT` |  | Creates or updates a Dev Box definition. |
| `DevBoxDefinitions_Delete` | `DELETE` |  | Deletes a Dev Box definition |
| `DevBoxDefinitions_GetByProject` | `EXEC` |  | Gets a Dev Box definition configured for a project |
| `DevBoxDefinitions_Update` | `EXEC` |  | Partially updates a Dev Box definition. |

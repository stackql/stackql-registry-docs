---
title: incident_todos
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_todos
  - incidents
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>incident_todos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.incidents.incident_todos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The incident todo's ID. |
| `attributes` | `object` | Incident todo's attributes. |
| `relationships` | `object` | The incident's relationships from a response. |
| `type` | `string` | Todo resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_todo` | `SELECT` | `incident_id, todo_id, dd_site` | Get incident todo details. |
| `list_incident_todos` | `SELECT` | `incident_id, dd_site` | Get all todos for an incident. |
| `create_incident_todo` | `INSERT` | `incident_id, data__data, dd_site` | Create an incident todo. |
| `delete_incident_todo` | `DELETE` | `incident_id, todo_id, dd_site` | Delete an incident todo. |
| `_get_incident_todo` | `EXEC` | `incident_id, todo_id, dd_site` | Get incident todo details. |
| `_list_incident_todos` | `EXEC` | `incident_id, dd_site` | Get all todos for an incident. |
| `update_incident_todo` | `EXEC` | `incident_id, todo_id, data__data, dd_site` | Update an incident todo. |

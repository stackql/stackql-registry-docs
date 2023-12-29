---
title: incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents
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
<tr><td><b>Name</b></td><td><code>incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.incidents.incidents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The incident's ID. |
| `attributes` | `object` | The incident's attributes from a response. |
| `relationships` | `object` | The incident's relationships from a response. |
| `type` | `string` | Incident resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident` | `SELECT` | `incident_id, dd_site` | Get the details of an incident by `incident_id`. |
| `list_incidents` | `SELECT` | `dd_site` | Get all incidents for the user's organization. |
| `search_incidents` | `SELECT` | `query, dd_site` | Search for incidents matching a certain query. |
| `create_incident` | `INSERT` | `data__data, dd_site` | Create an incident. |
| `delete_incident` | `DELETE` | `incident_id, dd_site` | Deletes an existing incident from the users organization. |
| `_get_incident` | `EXEC` | `incident_id, dd_site` | Get the details of an incident by `incident_id`. |
| `_list_incidents` | `EXEC` | `dd_site` | Get all incidents for the user's organization. |
| `_search_incidents` | `EXEC` | `query, dd_site` | Search for incidents matching a certain query. |
| `update_incident` | `EXEC` | `incident_id, data__data, dd_site` | Updates an incident. Provide only the attributes that should be updated as this request is a partial update. |

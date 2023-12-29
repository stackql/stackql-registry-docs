---
title: incident_services
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_services
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
<tr><td><b>Name</b></td><td><code>incident_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.incidents.incident_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The incident service's ID. |
| `attributes` | `object` | The incident service's attributes from a response. |
| `relationships` | `object` | The incident service's relationships. |
| `type` | `string` | Incident service resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_service` | `SELECT` | `service_id, dd_site` | Get details of an incident service. If the `include[users]` query parameter is provided,<br />the included attribute will contain the users related to these incident services. |
| `list_incident_services` | `SELECT` | `dd_site` | Get all incident services uploaded for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services. |
| `create_incident_service` | `INSERT` | `data__data, dd_site` | Creates a new incident service. |
| `delete_incident_service` | `DELETE` | `service_id, dd_site` | Deletes an existing incident service. |
| `_get_incident_service` | `EXEC` | `service_id, dd_site` | Get details of an incident service. If the `include[users]` query parameter is provided,<br />the included attribute will contain the users related to these incident services. |
| `_list_incident_services` | `EXEC` | `dd_site` | Get all incident services uploaded for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident services. |
| `update_incident_service` | `EXEC` | `service_id, data__data, dd_site` | Updates an existing incident service. Only provide the attributes which should be updated as this request is a partial update. |

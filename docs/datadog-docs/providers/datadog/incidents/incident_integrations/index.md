---
title: incident_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_integrations
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
<tr><td><b>Name</b></td><td><code>incident_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.incidents.incident_integrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The incident integration metadata's ID. |
| `attributes` | `object` | Incident integration metadata's attributes for a create request. |
| `relationships` | `object` | The incident's integration relationships from a response. |
| `type` | `string` | Integration metadata resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_integration` | `SELECT` | `incident_id, integration_metadata_id, dd_site` | Get incident integration metadata details. |
| `list_incident_integrations` | `SELECT` | `incident_id, dd_site` | Get all integration metadata for an incident. |
| `create_incident_integration` | `INSERT` | `incident_id, data__data, dd_site` | Create an incident integration metadata. |
| `delete_incident_integration` | `DELETE` | `incident_id, integration_metadata_id, dd_site` | Delete an incident integration metadata. |
| `_get_incident_integration` | `EXEC` | `incident_id, integration_metadata_id, dd_site` | Get incident integration metadata details. |
| `_list_incident_integrations` | `EXEC` | `incident_id, dd_site` | Get all integration metadata for an incident. |
| `update_incident_integration` | `EXEC` | `incident_id, integration_metadata_id, data__data, dd_site` | Update an existing incident integration metadata. |

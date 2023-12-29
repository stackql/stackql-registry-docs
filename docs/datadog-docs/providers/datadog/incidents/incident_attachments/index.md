---
title: incident_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_attachments
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
<tr><td><b>Name</b></td><td><code>incident_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.incidents.incident_attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique identifier that represents the incident attachment. |
| `attributes` | `` | The attributes object for an attachment. |
| `relationships` | `object` | The incident attachment's relationships. |
| `type` | `string` | The incident attachment resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_incident_attachments` | `SELECT` | `incident_id, dd_site` | Get all attachments for a given incident. |
| `_list_incident_attachments` | `EXEC` | `incident_id, dd_site` | Get all attachments for a given incident. |
| `update_incident_attachments` | `EXEC` | `incident_id, data__data, dd_site` | The bulk update endpoint for creating, updating, and deleting attachments for a given incident. |

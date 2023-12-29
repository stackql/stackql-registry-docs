---
title: opsgenie_services
hide_title: false
hide_table_of_contents: false
keywords:
  - opsgenie_services
  - opsgenie_integration
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
<tr><td><b>Name</b></td><td><code>opsgenie_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.opsgenie_integration.opsgenie_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the Opsgenie service. |
| `attributes` | `object` | The attributes from an Opsgenie service response. |
| `type` | `string` | Opsgenie service resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_opsgenie_service` | `SELECT` | `integration_service_id, dd_site` | Get a single service from the Datadog Opsgenie integration. |
| `list_opsgenie_services` | `SELECT` | `dd_site` | Get a list of all services from the Datadog Opsgenie integration. |
| `create_opsgenie_service` | `INSERT` | `data__data, dd_site` | Create a new service object in the Opsgenie integration. |
| `delete_opsgenie_service` | `DELETE` | `integration_service_id, dd_site` | Delete a single service object in the Datadog Opsgenie integration. |
| `_get_opsgenie_service` | `EXEC` | `integration_service_id, dd_site` | Get a single service from the Datadog Opsgenie integration. |
| `_list_opsgenie_services` | `EXEC` | `dd_site` | Get a list of all services from the Datadog Opsgenie integration. |
| `update_opsgenie_service` | `EXEC` | `integration_service_id, data__data, dd_site` | Update a single service object in the Datadog Opsgenie integration. |

---
title: service_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - service_definitions
  - service_definition
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
<tr><td><b>Name</b></td><td><code>service_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.service_definition.service_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Service definition id. |
| `attributes` | `object` | Service definition attributes. |
| `type` | `string` | Service definition type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_service_definition` | `SELECT` | `service_name, dd_site` | Get a single service definition from the Datadog Service Catalog. |
| `list_service_definitions` | `SELECT` | `dd_site` | Get a list of all service definitions from the Datadog Service Catalog. |
| `create_or_update_service_definitions` | `INSERT` | `dd_site` | Create or update service definition in the Datadog Service Catalog. |
| `delete_service_definition` | `DELETE` | `service_name, dd_site` | Delete a single service definition in the Datadog Service Catalog. |
| `_get_service_definition` | `EXEC` | `service_name, dd_site` | Get a single service definition from the Datadog Service Catalog. |
| `_list_service_definitions` | `EXEC` | `dd_site` | Get a list of all service definitions from the Datadog Service Catalog. |

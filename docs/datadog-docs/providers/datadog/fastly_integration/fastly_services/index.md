---
title: fastly_services
hide_title: false
hide_table_of_contents: false
keywords:
  - fastly_services
  - fastly_integration
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
<tr><td><b>Name</b></td><td><code>fastly_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.fastly_integration.fastly_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the Fastly service. |
| `attributes` | `object` | Attributes object for Fastly service requests. |
| `type` | `string` | The JSON:API type for this API. Should always be `fastly-services`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_fastly_service` | `SELECT` | `account_id, service_id, dd_site` | Get a Fastly service for an account. |
| `list_fastly_services` | `SELECT` | `account_id, dd_site` | List Fastly services for an account. |
| `create_fastly_service` | `INSERT` | `account_id, data__data, dd_site` | Create a Fastly service for an account. |
| `delete_fastly_service` | `DELETE` | `account_id, service_id, dd_site` | Delete a Fastly service for an account. |
| `_get_fastly_service` | `EXEC` | `account_id, service_id, dd_site` | Get a Fastly service for an account. |
| `_list_fastly_services` | `EXEC` | `account_id, dd_site` | List Fastly services for an account. |
| `update_fastly_service` | `EXEC` | `account_id, service_id, data__data, dd_site` | Update a Fastly service for an account. |

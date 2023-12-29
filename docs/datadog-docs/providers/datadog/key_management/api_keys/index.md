---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
  - key_management
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
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.key_management.api_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the API key. |
| `attributes` | `object` | Attributes of a full API key. |
| `relationships` | `object` | Resources related to the API key. |
| `type` | `string` | API Keys resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_api_key` | `SELECT` | `api_key_id, dd_site` | Get an API key. |
| `list_api_keys` | `SELECT` | `dd_site` | List all API keys available for your account. |
| `create_api_key` | `INSERT` | `data__data, dd_site` | Create an API key. |
| `delete_api_key` | `DELETE` | `api_key_id, dd_site` | Delete an API key. |
| `_get_api_key` | `EXEC` | `api_key_id, dd_site` | Get an API key. |
| `_list_api_keys` | `EXEC` | `dd_site` | List all API keys available for your account. |
| `update_api_key` | `EXEC` | `api_key_id, data__data, dd_site` | Update an API key. |

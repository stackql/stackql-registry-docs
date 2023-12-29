---
title: current_user_application_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - current_user_application_keys
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
<tr><td><b>Name</b></td><td><code>current_user_application_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.key_management.current_user_application_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the application key. |
| `attributes` | `object` | Attributes of a full application key. |
| `relationships` | `object` | Resources related to the application key. |
| `type` | `string` | Application Keys resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_current_user_application_key` | `SELECT` | `app_key_id, dd_site` | Get an application key owned by current user |
| `list_current_user_application_keys` | `SELECT` | `dd_site` | List all application keys available for current user |
| `create_current_user_application_key` | `INSERT` | `data__data, dd_site` | Create an application key for current user |
| `delete_current_user_application_key` | `DELETE` | `app_key_id, dd_site` | Delete an application key owned by current user |
| `_get_current_user_application_key` | `EXEC` | `app_key_id, dd_site` | Get an application key owned by current user |
| `_list_current_user_application_keys` | `EXEC` | `dd_site` | List all application keys available for current user |
| `update_current_user_application_key` | `EXEC` | `app_key_id, data__data, dd_site` | Edit an application key owned by current user |

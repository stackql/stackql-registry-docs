---
title: service_account_application_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - service_account_application_keys
  - service_accounts
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
<tr><td><b>Name</b></td><td><code>service_account_application_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.service_accounts.service_account_application_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the application key. |
| `attributes` | `object` | Attributes of a partial application key. |
| `relationships` | `object` | Resources related to the application key. |
| `type` | `string` | Application Keys resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_service_account_application_key` | `SELECT` | `app_key_id, service_account_id, dd_site` | Get an application key owned by this service account. |
| `list_service_account_application_keys` | `SELECT` | `service_account_id, dd_site` | List all application keys available for this service account. |
| `create_service_account_application_key` | `INSERT` | `service_account_id, data__data, dd_site` | Create an application key for this service account. |
| `delete_service_account_application_key` | `DELETE` | `app_key_id, service_account_id, dd_site` | Delete an application key owned by this service account. |
| `_get_service_account_application_key` | `EXEC` | `app_key_id, service_account_id, dd_site` | Get an application key owned by this service account. |
| `_list_service_account_application_keys` | `EXEC` | `service_account_id, dd_site` | List all application keys available for this service account. |
| `update_service_account_application_key` | `EXEC` | `app_key_id, service_account_id, data__data, dd_site` | Edit an application key owned by this service account. |

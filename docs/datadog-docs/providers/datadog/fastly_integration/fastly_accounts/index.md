---
title: fastly_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - fastly_accounts
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
<tr><td><b>Name</b></td><td><code>fastly_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.fastly_integration.fastly_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the Fastly account, a hash of the account name. |
| `attributes` | `object` | Attributes object of a Fastly account. |
| `type` | `string` | The JSON:API type for this API. Should always be `fastly-accounts`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_fastly_account` | `SELECT` | `account_id, dd_site` | Get a Fastly account. |
| `list_fastly_accounts` | `SELECT` | `dd_site` | List Fastly accounts. |
| `create_fastly_account` | `INSERT` | `data__data, dd_site` | Create a Fastly account. |
| `delete_fastly_account` | `DELETE` | `account_id, dd_site` | Delete a Fastly account. |
| `_get_fastly_account` | `EXEC` | `account_id, dd_site` | Get a Fastly account. |
| `_list_fastly_accounts` | `EXEC` | `dd_site` | List Fastly accounts. |
| `update_fastly_account` | `EXEC` | `account_id, data__data, dd_site` | Update a Fastly account. |

---
title: okta_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - okta_accounts
  - okta_integration
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
<tr><td><b>Name</b></td><td><code>okta_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.okta_integration.okta_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the Okta account, a UUID hash of the account name. |
| `attributes` | `object` | Attributes object for an Okta account. |
| `type` | `string` | Account type for an Okta account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_okta_account` | `SELECT` | `account_id, dd_site` | Get an Okta account. |
| `list_okta_accounts` | `SELECT` | `dd_site` | List Okta accounts. |
| `create_okta_account` | `INSERT` | `data__data, dd_site` | Create an Okta account. |
| `delete_okta_account` | `DELETE` | `account_id, dd_site` | Delete an Okta account. |
| `_get_okta_account` | `EXEC` | `account_id, dd_site` | Get an Okta account. |
| `_list_okta_accounts` | `EXEC` | `dd_site` | List Okta accounts. |
| `update_okta_account` | `EXEC` | `account_id, data__data, dd_site` | Update an Okta account. |

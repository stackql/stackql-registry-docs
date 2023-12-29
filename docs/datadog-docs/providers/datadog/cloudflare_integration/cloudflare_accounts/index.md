---
title: cloudflare_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - cloudflare_accounts
  - cloudflare_integration
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
<tr><td><b>Name</b></td><td><code>cloudflare_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.cloudflare_integration.cloudflare_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the Cloudflare account, a hash of the account name. |
| `attributes` | `object` | Attributes object of a Cloudflare account. |
| `type` | `string` | The JSON:API type for this API. Should always be `cloudflare-accounts`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_cloudflare_account` | `SELECT` | `account_id, dd_site` | Get a Cloudflare account. |
| `list_cloudflare_accounts` | `SELECT` | `dd_site` | List Cloudflare accounts. |
| `create_cloudflare_account` | `INSERT` | `data__data, dd_site` | Create a Cloudflare account. |
| `delete_cloudflare_account` | `DELETE` | `account_id, dd_site` | Delete a Cloudflare account. |
| `_get_cloudflare_account` | `EXEC` | `account_id, dd_site` | Get a Cloudflare account. |
| `_list_cloudflare_accounts` | `EXEC` | `dd_site` | List Cloudflare accounts. |
| `update_cloudflare_account` | `EXEC` | `account_id, data__data, dd_site` | Update a Cloudflare account. |

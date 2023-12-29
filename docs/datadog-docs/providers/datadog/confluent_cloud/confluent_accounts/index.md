---
title: confluent_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - confluent_accounts
  - confluent_cloud
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
<tr><td><b>Name</b></td><td><code>confluent_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.confluent_cloud.confluent_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A randomly generated ID associated with a Confluent account. |
| `attributes` | `object` | The attributes of a Confluent account. |
| `type` | `string` | The JSON:API type for this API. Should always be `confluent-cloud-accounts`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_confluent_account` | `SELECT` | `account_id, dd_site` | Get the Confluent account with the provided account ID. |
| `list_confluent_account` | `SELECT` | `dd_site` | List Confluent accounts. |
| `create_confluent_account` | `INSERT` | `data__data, dd_site` | Create a Confluent account. |
| `delete_confluent_account` | `DELETE` | `account_id, dd_site` | Delete a Confluent account with the provided account ID. |
| `_get_confluent_account` | `EXEC` | `account_id, dd_site` | Get the Confluent account with the provided account ID. |
| `_list_confluent_account` | `EXEC` | `dd_site` | List Confluent accounts. |
| `update_confluent_account` | `EXEC` | `account_id, data__data, dd_site` | Update the Confluent account with the provided account ID. |

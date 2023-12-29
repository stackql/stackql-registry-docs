---
title: confluent_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - confluent_resources
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
<tr><td><b>Name</b></td><td><code>confluent_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.confluent_cloud.confluent_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID associated with the Confluent resource. |
| `attributes` | `object` | Model representation of a Confluent Cloud resource. |
| `type` | `string` | The JSON:API type for this request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_confluent_resource` | `SELECT` | `account_id, resource_id, dd_site` | Get a Confluent resource with the provided resource id for the account associated with the provided account ID. |
| `list_confluent_resource` | `SELECT` | `account_id, dd_site` | Get a Confluent resource for the account associated with the provided ID. |
| `create_confluent_resource` | `INSERT` | `account_id, data__data, dd_site` | Create a Confluent resource for the account associated with the provided ID. |
| `delete_confluent_resource` | `DELETE` | `account_id, resource_id, dd_site` | Delete a Confluent resource with the provided resource id for the account associated with the provided account ID. |
| `_get_confluent_resource` | `EXEC` | `account_id, resource_id, dd_site` | Get a Confluent resource with the provided resource id for the account associated with the provided account ID. |
| `_list_confluent_resource` | `EXEC` | `account_id, dd_site` | Get a Confluent resource for the account associated with the provided ID. |
| `update_confluent_resource` | `EXEC` | `account_id, resource_id, data__data, dd_site` | Update a Confluent resource with the provided resource id for the account associated with the provided account ID. |

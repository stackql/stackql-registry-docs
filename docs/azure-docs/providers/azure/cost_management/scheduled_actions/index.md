---
title: scheduled_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions
  - cost_management
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cost_management.scheduled_actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eTag` | `string` | Resource Etag. For update calls, eTag is optional and can be specified to achieve optimistic concurrency. Fetch the resource's eTag by doing a 'GET' call first and then including the latest eTag as part of the request body or 'If-Match' header while performing the update. For create calls, eTag is not required. |
| `kind` | `string` | Kind of the scheduled action. |
| `properties` | `object` | The properties of the scheduled action. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name` | Get the private scheduled action by name. |
| `list` | `SELECT` |  | List all private scheduled actions. |
| `list_by_scope` | `SELECT` | `scope` | List all shared scheduled actions within the given scope. |
| `create_or_update` | `INSERT` | `name` | Create or update a private scheduled action. |
| `delete` | `DELETE` | `name` | Delete a private scheduled action. |
| `delete_by_scope` | `DELETE` | `name, scope` | Delete a scheduled action within the given scope. |
| `_list` | `EXEC` |  | List all private scheduled actions. |
| `_list_by_scope` | `EXEC` | `scope` | List all shared scheduled actions within the given scope. |
| `check_name_availability` | `EXEC` |  | Checks availability and correctness of the name for a scheduled action. |
| `check_name_availability_by_scope` | `EXEC` | `scope` | Checks availability and correctness of the name for a scheduled action within the given scope. |
| `create_or_update_by_scope` | `EXEC` | `name, scope` | Create or update a shared scheduled action within the given scope. |
| `get_by_scope` | `EXEC` | `name, scope` | Get the shared scheduled action from the given scope by name. |
| `run` | `EXEC` | `name` | Processes a private scheduled action. |
| `run_by_scope` | `EXEC` | `name, scope` | Runs a shared scheduled action within the given scope. |

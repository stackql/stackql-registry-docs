---
title: namespace_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - namespace_triggers
  - functions
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespace_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.functions.namespace_triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The trigger's unique name within the namespace. |
| `namespace` | `string` | A unique string format of UUID with a prefix fn-. |
| `scheduled_details` | `object` | Trigger details for SCHEDULED type, where body is optional.<br /> |
| `function` | `string` | Name of function(action) that exists in the given namespace. |
| `type` | `string` | String which indicates the type of trigger source like SCHEDULED. |
| `is_enabled` | `boolean` | Indicates weather the trigger is paused or unpaused. |
| `updated_at` | `string` | UTC time string. |
| `created_at` | `string` | UTC time string. |
| `scheduled_runs` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_trigger` | `SELECT` | `namespace_id, trigger_name` | Gets the trigger details. To get the trigger details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`. |
| `list_triggers` | `SELECT` | `namespace_id` | Returns a list of triggers associated with the current user and namespace. To get all triggers, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers`. |
| `create_trigger` | `INSERT` | `namespace_id, data__function, data__is_enabled, data__name, data__scheduled_details, data__type` | Creates a new trigger for a given function in a namespace. To create a trigger, send a POST request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers` with the `name`, `function`, `type`, `is_enabled` and `scheduled_details` properties. |
| `delete_trigger` | `DELETE` | `namespace_id, trigger_name` | Deletes the given trigger.<br />To delete trigger, send a DELETE request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`.<br />A successful deletion returns a 204 response. |
| `_get_trigger` | `EXEC` | `namespace_id, trigger_name` | Gets the trigger details. To get the trigger details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`. |
| `_list_triggers` | `EXEC` | `namespace_id` | Returns a list of triggers associated with the current user and namespace. To get all triggers, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers`. |
| `update_trigger` | `EXEC` | `namespace_id, trigger_name` | Updates the details of the given trigger. To update a trigger, send a PUT request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME` with new values for the `is_enabled ` or `scheduled_details` properties. |

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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespace_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.functions.namespace_triggers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The trigger's unique name within the namespace. |
| <CopyableCode code="created_at" /> | `string` | UTC time string. |
| <CopyableCode code="function" /> | `string` | Name of function(action) that exists in the given namespace. |
| <CopyableCode code="is_enabled" /> | `boolean` | Indicates weather the trigger is paused or unpaused. |
| <CopyableCode code="namespace" /> | `string` | A unique string format of UUID with a prefix fn-. |
| <CopyableCode code="scheduled_details" /> | `object` | Trigger details for SCHEDULED type, where body is optional.<br /> |
| <CopyableCode code="scheduled_runs" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | String which indicates the type of trigger source like SCHEDULED. |
| <CopyableCode code="updated_at" /> | `string` | UTC time string. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_trigger" /> | `SELECT` | <CopyableCode code="namespace_id, trigger_name" /> | Gets the trigger details. To get the trigger details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`. |
| <CopyableCode code="list_triggers" /> | `SELECT` | <CopyableCode code="namespace_id" /> | Returns a list of triggers associated with the current user and namespace. To get all triggers, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers`. |
| <CopyableCode code="create_trigger" /> | `INSERT` | <CopyableCode code="namespace_id, data__function, data__is_enabled, data__name, data__scheduled_details, data__type" /> | Creates a new trigger for a given function in a namespace. To create a trigger, send a POST request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers` with the `name`, `function`, `type`, `is_enabled` and `scheduled_details` properties. |
| <CopyableCode code="delete_trigger" /> | `DELETE` | <CopyableCode code="namespace_id, trigger_name" /> | Deletes the given trigger.<br />To delete trigger, send a DELETE request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`.<br />A successful deletion returns a 204 response. |
| <CopyableCode code="_get_trigger" /> | `EXEC` | <CopyableCode code="namespace_id, trigger_name" /> | Gets the trigger details. To get the trigger details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`. |
| <CopyableCode code="_list_triggers" /> | `EXEC` | <CopyableCode code="namespace_id" /> | Returns a list of triggers associated with the current user and namespace. To get all triggers, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers`. |
| <CopyableCode code="update_trigger" /> | `EXEC` | <CopyableCode code="namespace_id, trigger_name" /> | Updates the details of the given trigger. To update a trigger, send a PUT request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME` with new values for the `is_enabled ` or `scheduled_details` properties. |

---
title: namespaces_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_triggers
  - functions
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>namespaces_triggers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.functions.namespaces_triggers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The trigger's unique name within the namespace. |
| <CopyableCode code="created_at" /> | `string` | UTC time string. |
| <CopyableCode code="function" /> | `string` | Name of function(action) that exists in the given namespace. |
| <CopyableCode code="is_enabled" /> | `boolean` | Indicates weather the trigger is paused or unpaused. |
| <CopyableCode code="namespace" /> | `string` | A unique string format of UUID with a prefix fn-. |
| <CopyableCode code="scheduled_details" /> | `object` | Trigger details for SCHEDULED type, where body is optional. |
| <CopyableCode code="scheduled_runs" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | String which indicates the type of trigger source like SCHEDULED. |
| <CopyableCode code="updated_at" /> | `string` | UTC time string. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="functions_get_trigger" /> | `SELECT` | <CopyableCode code="namespace_id, trigger_name" /> | Gets the trigger details. To get the trigger details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`. |
| <CopyableCode code="functions_list_triggers" /> | `SELECT` | <CopyableCode code="namespace_id" /> | Returns a list of triggers associated with the current user and namespace. To get all triggers, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers`. |
| <CopyableCode code="functions_create_trigger" /> | `INSERT` | <CopyableCode code="namespace_id, data__function, data__is_enabled, data__name, data__scheduled_details, data__type" /> | Creates a new trigger for a given function in a namespace. To create a trigger, send a POST request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers` with the `name`, `function`, `type`, `is_enabled` and `scheduled_details` properties. |
| <CopyableCode code="functions_delete_trigger" /> | `DELETE` | <CopyableCode code="namespace_id, trigger_name" /> | Deletes the given trigger. To delete trigger, send a DELETE request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`. A successful deletion returns a 204 response. |
| <CopyableCode code="functions_update_trigger" /> | `EXEC` | <CopyableCode code="namespace_id, trigger_name" /> | Updates the details of the given trigger. To update a trigger, send a PUT request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME` with new values for the `is_enabled ` or `scheduled_details` properties. |

## `SELECT` examples

Returns a list of triggers associated with the current user and namespace. To get all triggers, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers`.


```sql
SELECT
name,
created_at,
function,
is_enabled,
namespace,
scheduled_details,
scheduled_runs,
type,
updated_at
FROM digitalocean.functions.namespaces_triggers
WHERE namespace_id = '{{ namespace_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>namespaces_triggers</code> resource.

<Tabs
    defaultValue="all"
    values={[
        
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.functions.namespaces_triggers (
data__name,
data__function,
data__type,
data__is_enabled,
data__scheduled_details,
namespace_id
)
SELECT 
'{{ name }}',
'{{ function }}',
'{{ type }}',
'{{ is_enabled }}',
'{{ scheduled_details }}',
'{{ namespace_id }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: namespaces_triggers
  props:
    - name: namespace_id
      value: string
    - name: data__function
      value: string
    - name: data__is_enabled
      value: string
    - name: data__name
      value: string
    - name: data__scheduled_details
      value: string
    - name: data__type
      value: string
    - name: name
      value: string
    - name: function
      value: string
    - name: type
      value: string
    - name: is_enabled
      value: boolean
    - name: scheduled_details
      props:
        - name: cron
          value: string
        - name: body
          props:
            - name: name
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>namespaces_triggers</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.functions.namespaces_triggers
WHERE namespace_id = '{{ namespace_id }}'
AND trigger_name = '{{ trigger_name }}';
```

---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - alert
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.alert.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the alert |
| <CopyableCode code="action" /> | `string` | The SQL statement to execute when the alert is triggered |
| <CopyableCode code="comment" /> | `string` | user comment associated to an object in the dictionary |
| <CopyableCode code="condition" /> | `string` | The SQL statement that must be evaluated to determine whether to trigger the alert |
| <CopyableCode code="created_on" /> | `string` | Date and time when the alert was created. |
| <CopyableCode code="database_name" /> | `string` | Database in which the alert is stored |
| <CopyableCode code="owner" /> | `string` | Role that owns the alert |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the alert |
| <CopyableCode code="schedule" /> | `object` |  |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the alert is stored |
| <CopyableCode code="state" /> | `string` | The current state of the alert |
| <CopyableCode code="warehouse" /> | `string` | The warehouse the alert runs in |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_alert" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Fetch an alert |
| <CopyableCode code="list_alerts" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | List alerts |
| <CopyableCode code="create_alert" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__action, data__condition, data__name, data__schedule, endpoint" /> | Create an alert |
| <CopyableCode code="delete_alert" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Delete an alert |
| <CopyableCode code="clone_alert" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetDatabase, targetSchema, data__name, endpoint" /> | Create a new alert by cloning from the specified resource |
| <CopyableCode code="execute_alert" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | Execute an alert |

## `SELECT` examples

List alerts


```sql
SELECT
name,
action,
comment,
condition,
created_on,
database_name,
owner,
owner_role_type,
schedule,
schema_name,
state,
warehouse
FROM snowflake.alert.alerts
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>alerts</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.alert.alerts (
data__name,
data__comment,
data__schedule,
data__warehouse,
data__condition,
data__action,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ comment }}',
'{{ schedule }}',
'{{ warehouse }}',
'{{ condition }}',
'{{ action }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.alert.alerts (
data__name,
data__schedule,
data__condition,
data__action,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ schedule }}',
'{{ condition }}',
'{{ action }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: alerts
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__action
      value: string
    - name: data__condition
      value: string
    - name: data__name
      value: string
    - name: data__schedule
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: comment
      value: string
    - name: schedule
      props:
        - name: schedule_type
          value: string
    - name: warehouse
      value: string
    - name: condition
      value: string
    - name: action
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>alerts</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.alert.alerts
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```

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
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_alert" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetch an alert |
| <CopyableCode code="list_alerts" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" /> | List alerts |
| <CopyableCode code="create_alert" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__action, data__condition, data__name, data__schedule, endpoint" /> | <CopyableCode code="createMode" /> | Create an alert |
| <CopyableCode code="delete_alert" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete an alert |
| <CopyableCode code="clone_alert" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetDatabase, targetSchema, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create a new alert by cloning from the specified resource |
| <CopyableCode code="execute_alert" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Execute an alert |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_alerts"
    values={[
        { label: 'list_alerts', value: 'list_alerts' },
        { label: 'fetch_alert', value: 'fetch_alert' }
    ]
}>
<TabItem value="list_alerts">

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
</TabItem>
<TabItem value="fetch_alert">

Fetch an alert

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
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

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
# Description fields below are for documentation purposes only and are not required in the manifest
- name: alerts
  props:
    - name: database_name
      value: string
      description: Required parameter for the alerts resource.
    - name: schema_name
      value: string
      description: Required parameter for the alerts resource.
    - name: endpoint
      value: string
      description: Required parameter for the alerts resource.
    - name: name
      value: string
      description: Name of the alert (Required parameter for the alerts resource.)
    - name: comment
      value: string
      description: user comment associated to an object in the dictionary
    - name: schedule
      value:
        schedule_type: string
      description: Required parameter for the alerts resource.
    - name: warehouse
      value: string
      description: The warehouse the alert runs in
    - name: condition
      value: string
      description: >-
        The SQL statement that must be evaluated to determine whether to trigger
        the alert (Required parameter for the alerts resource.)
    - name: action
      value: string
      description: >-
        The SQL statement to execute when the alert is triggered (Required
        parameter for the alerts resource.)
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

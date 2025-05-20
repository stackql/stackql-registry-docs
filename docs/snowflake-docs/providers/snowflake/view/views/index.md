---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - view
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

Creates, updates, deletes, gets or lists a <code>views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.view.views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the view |
| <CopyableCode code="columns" /> | `array` | The columns of the view |
| <CopyableCode code="comment" /> | `string` | user comment associated to an object in the dictionary |
| <CopyableCode code="created_on" /> | `string` | Date and time when the view was created. |
| <CopyableCode code="database_name" /> | `string` | Database in which the view is stored |
| <CopyableCode code="kind" /> | `string` | Kind of the view, permanent (default) or temporary |
| <CopyableCode code="owner" /> | `string` | Role that owns the view |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the view |
| <CopyableCode code="query" /> | `string` | Query used to create the view |
| <CopyableCode code="recursive" /> | `boolean` | Whether or not this view can refer to itself using recursive syntax withot requiring a CTE (common table expression) |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the view is stored |
| <CopyableCode code="secure" /> | `boolean` | Whether or not this view is secure |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_view" /> | `SELECT` | <CopyableCode code="database, name, schema, endpoint" /> | Fetch a view |
| <CopyableCode code="list_views" /> | `SELECT` | <CopyableCode code="database, schema, endpoint" /> | List views |
| <CopyableCode code="create_view" /> | `INSERT` | <CopyableCode code="database, schema, data__columns, data__name, data__query, endpoint" /> | Create a view |
| <CopyableCode code="delete_view" /> | `DELETE` | <CopyableCode code="database, name, schema, endpoint" /> | Delete a view |

## `SELECT` examples

List views


```sql
SELECT
name,
columns,
comment,
created_on,
database_name,
kind,
owner,
owner_role_type,
query,
recursive,
schema_name,
secure
FROM snowflake.view.views
WHERE database = '{{ database }}' AND schema = '{{ schema }}' AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>views</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.view.views (
data__query,
data__name,
endpoint,
schema,
database,
data__columns
)
SELECT 
'{ database }',
'{ query }',
'{ endpoint }',
'{ schema }',
'{ name }',
'{ columns }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: views
  props:
  - name: database
    value: string
  - name: schema
    value: string
  - name: data__columns
    value: string
  - name: data__name
    value: string
  - name: data__query
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>views</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.view.views
WHERE database = '{ database }' AND name = '{ name }' AND schema = '{ schema }' AND endpoint = '{ endpoint }';
```

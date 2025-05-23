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
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_view" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetch a view |
| <CopyableCode code="list_views" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | [`like`](#like), [`startsWith`](#startsWith), [`showLimit`](#showLimit), [`fromName`](#fromName), [`deep`](#deep) | List views |
| <CopyableCode code="create_view" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__columns, data__name, data__query, endpoint" /> | [`createMode`](#createMode), [`copyGrants`](#copyGrants) | Create a view |
| <CopyableCode code="delete_view" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | [`ifExists`](#ifExists) | Delete a view |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="copyGrants" id="copyGrants" /> | Query parameter to enable copy grants when creating the object. | `boolean` | `false` |
| <CopyableCode code="createMode" id="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="deep" id="deep" /> | Optionally includes dependency information of the view. | `boolean` | `-` |
| <CopyableCode code="fromName" id="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="ifExists" id="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" id="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" id="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" id="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |

</details>

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
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>views</code> resource.

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
INSERT INTO snowflake.view.views (
data__name,
data__secure,
data__kind,
data__recursive,
data__columns,
data__comment,
data__query,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ secure }}',
'{{ kind }}',
'{{ recursive }}',
'{{ columns }}',
'{{ comment }}',
'{{ query }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.view.views (
data__name,
data__columns,
data__query,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ columns }}',
'{{ query }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: views
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__columns
      value: string
    - name: data__name
      value: string
    - name: data__query
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: secure
      value: boolean
    - name: kind
      value: string
    - name: recursive
      value: boolean
    - name: columns
      value:
        - name: name
          value: string
        - name: comment
          value: string
    - name: comment
      value: string
    - name: query
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>views</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.view.views
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```

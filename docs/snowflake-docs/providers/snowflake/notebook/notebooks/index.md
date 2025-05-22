---
title: notebooks
hide_title: false
hide_table_of_contents: false
keywords:
  - notebooks
  - notebook
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

Creates, updates, deletes, gets or lists a <code>notebooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.notebook.notebooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the notebook |
| <CopyableCode code="budget" /> | `string` | Name of the budget if the notebook is monitored by a budget |
| <CopyableCode code="comment" /> | `string` | user comment associated to an object in the dictionary |
| <CopyableCode code="compute_pool" /> | `string` | Compute pool name where the snowservice runs |
| <CopyableCode code="created_on" /> | `string` | Date and time when the notebook was created. |
| <CopyableCode code="database_name" /> | `string` | Database in which the notebook is stored |
| <CopyableCode code="default_packages" /> | `string` | Default packages of the notebook |
| <CopyableCode code="default_version" /> | `string` | The default version name of a file based entity. |
| <CopyableCode code="default_version_details" /> | `object` | The version details of a file based entity |
| <CopyableCode code="external_access_integrations" /> | `array` | List of external access integrations attached to this function |
| <CopyableCode code="external_access_secrets" /> | `string` | Secrets to be used with this function for external access |
| <CopyableCode code="fromLocation" /> | `string` | Location to copy the file from. This must be a Snowflake stage location. |
| <CopyableCode code="idle_auto_shutdown_time_seconds" /> | `integer` | Sets the time in seconds for when to shutdown an idle Notebook. |
| <CopyableCode code="import_urls" /> | `array` | List of urls |
| <CopyableCode code="last_version_details" /> | `object` | The version details of a file based entity |
| <CopyableCode code="live_version_location_uri" /> | `string` | The current version location |
| <CopyableCode code="main_file" /> | `string` | Name + path of the file for the Notebook |
| <CopyableCode code="owner" /> | `string` | Role that owns the notebook |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the notebook |
| <CopyableCode code="query_warehouse" /> | `string` | Warehouse against which the queries issued by the Streamlit app are run against |
| <CopyableCode code="runtime_name" /> | `string` | The runtime to run the Streamlit or Notebook on. If this is not set, the warehouse is assumed |
| <CopyableCode code="schema_name" /> | `string` | Schema in which the notebook is stored |
| <CopyableCode code="title" /> | `string` | User facing title of the Streamlit app or an Organization Profile |
| <CopyableCode code="url_id" /> | `string` | Unique ID associated with the notebook object. |
| <CopyableCode code="user_packages" /> | `string` | User packages of the notebook |
| <CopyableCode code="version" /> | `string` | User specified version alias |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_notebook" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetch a notebook |
| <CopyableCode code="list_notebooks" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" /> | List notebooks |
| <CopyableCode code="create_notebook" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create a notebook |
| <CopyableCode code="delete_notebook" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a notebook |
| <CopyableCode code="add_live_version_notebook" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="fromLast" />, <CopyableCode code="comment" /> | Adds a LIVE version to the notebook |
| <CopyableCode code="commit_notebook" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="version" />, <CopyableCode code="comment" /> | If a Git connection is set up for the notebook, commits the LIVE version of the notebook to the Git repository |
| <CopyableCode code="execute_notebook" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="asyncExec" /> | Execute a Notebook |
| <CopyableCode code="rename_notebook" /> | `EXEC` | <CopyableCode code="database_name, name, schema_name, targetName, endpoint" /> | <CopyableCode code="ifExists" />, <CopyableCode code="targetDatabase" />, <CopyableCode code="targetSchema" /> | Changes the name of the notebook to new name. The new identifier must be unique for the schema. |


Expand this to view optional parameter details for all methods in this resource.


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="asyncExec" /> | Asynchronous execution enable/disable. Default is disable. | `boolean` | `false` |
| <CopyableCode code="comment" /> | Sets a comment for the notebook or version of the notebook | `string` | `-` |
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="fromLast" /> | Sets the LIVE version to the LAST version of the notebook | `boolean` | `-` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |
| <CopyableCode code="targetDatabase" /> | Database of the target resource. Defaults to the source's database | `string` | `-` |
| <CopyableCode code="targetSchema" /> | Schema of the target resource. Defaults to the source's schema | `string` | `-` |
| <CopyableCode code="version" /> | live version of the alias | `string` | `-` |

</details>

## `SELECT` examples

List notebooks


```sql
SELECT
name,
budget,
comment,
compute_pool,
created_on,
database_name,
default_packages,
default_version,
default_version_details,
external_access_integrations,
external_access_secrets,
fromLocation,
idle_auto_shutdown_time_seconds,
import_urls,
last_version_details,
live_version_location_uri,
main_file,
owner,
owner_role_type,
query_warehouse,
runtime_name,
schema_name,
title,
url_id,
user_packages,
version
FROM snowflake.notebook.notebooks
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notebooks</code> resource.

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
INSERT INTO snowflake.notebook.notebooks (
data__name,
data__version,
data__fromLocation,
data__main_file,
data__comment,
data__default_version,
data__query_warehouse,
data__default_version_details,
data__last_version_details,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ version }}',
'{{ fromLocation }}',
'{{ main_file }}',
'{{ comment }}',
'{{ default_version }}',
'{{ query_warehouse }}',
'{{ default_version_details }}',
'{{ last_version_details }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.notebook.notebooks (
data__name,
database_name,
schema_name,
endpoint
)
SELECT 
'{{ name }}',
'{{ database_name }}',
'{{ schema_name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: notebooks
  props:
    - name: database_name
      value: string
    - name: schema_name
      value: string
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: version
      value: string
    - name: fromLocation
      value: string
    - name: main_file
      value: string
    - name: comment
      value: string
    - name: default_version
      value: string
    - name: query_warehouse
      value: string
    - name: default_version_details
      props: []
    - name: last_version_details
      props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>notebooks</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.notebook.notebooks
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```

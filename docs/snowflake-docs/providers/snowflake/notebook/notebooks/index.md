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

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_notebooks"
    values={[
        { label: 'list_notebooks', value: 'list_notebooks' },
        { label: 'fetch_notebook', value: 'fetch_notebook' }
    ]}
>
<TabItem value="list_notebooks">

A Snowflake notebook

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the notebook (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="url_id" /></td>
    <td><code>string</code></td>
    <td>Unique ID associated with the notebook object.</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the notebook is stored (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="runtime_name" /></td>
    <td><code>string</code></td>
    <td>The runtime to run the Streamlit or Notebook on.  If this is not set, the warehouse is assumed</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the notebook is stored (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Name of the budget if the notebook is monitored by a budget (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="compute_pool" /></td>
    <td><code>string</code></td>
    <td>Compute pool name where the snowservice runs</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the notebook was created.</td>
</tr>
<tr>
    <td><CopyableCode code="default_packages" /></td>
    <td><code>string</code></td>
    <td>Default packages of the notebook</td>
</tr>
<tr>
    <td><CopyableCode code="default_version" /></td>
    <td><code>string</code></td>
    <td>The default version name of a file based entity.</td>
</tr>
<tr>
    <td><CopyableCode code="default_version_details" /></td>
    <td><code>object</code></td>
    <td>The version details of a file based entity</td>
</tr>
<tr>
    <td><CopyableCode code="external_access_integrations" /></td>
    <td><code>array</code></td>
    <td>List of external access integrations attached to this function</td>
</tr>
<tr>
    <td><CopyableCode code="external_access_secrets" /></td>
    <td><code>string</code></td>
    <td>Secrets to be used with this function for external access</td>
</tr>
<tr>
    <td><CopyableCode code="fromLocation" /></td>
    <td><code>string</code></td>
    <td>Location to copy the file from. This must be a Snowflake stage location.</td>
</tr>
<tr>
    <td><CopyableCode code="idle_auto_shutdown_time_seconds" /></td>
    <td><code>integer (int64)</code></td>
    <td>Sets the time in seconds for when to shutdown an idle Notebook.</td>
</tr>
<tr>
    <td><CopyableCode code="import_urls" /></td>
    <td><code>array</code></td>
    <td>List of urls</td>
</tr>
<tr>
    <td><CopyableCode code="last_version_details" /></td>
    <td><code>object</code></td>
    <td>The version details of a file based entity</td>
</tr>
<tr>
    <td><CopyableCode code="live_version_location_uri" /></td>
    <td><code>string</code></td>
    <td>The current version location</td>
</tr>
<tr>
    <td><CopyableCode code="main_file" /></td>
    <td><code>string</code></td>
    <td>Name + path of the file for the Notebook</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the notebook (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the notebook (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="query_warehouse" /></td>
    <td><code>string</code></td>
    <td>Warehouse against which the queries issued by the Streamlit app are run against</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>User facing title of the Streamlit app or an Organization Profile</td>
</tr>
<tr>
    <td><CopyableCode code="user_packages" /></td>
    <td><code>string</code></td>
    <td>User packages of the notebook</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>User specified version alias</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_notebook">

A Snowflake notebook

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the notebook (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="url_id" /></td>
    <td><code>string</code></td>
    <td>Unique ID associated with the notebook object.</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Database in which the notebook is stored (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="runtime_name" /></td>
    <td><code>string</code></td>
    <td>The runtime to run the Streamlit or Notebook on.  If this is not set, the warehouse is assumed</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Schema in which the notebook is stored (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="budget" /></td>
    <td><code>string</code></td>
    <td>Name of the budget if the notebook is monitored by a budget (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>user comment associated to an object in the dictionary</td>
</tr>
<tr>
    <td><CopyableCode code="compute_pool" /></td>
    <td><code>string</code></td>
    <td>Compute pool name where the snowservice runs</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the notebook was created.</td>
</tr>
<tr>
    <td><CopyableCode code="default_packages" /></td>
    <td><code>string</code></td>
    <td>Default packages of the notebook</td>
</tr>
<tr>
    <td><CopyableCode code="default_version" /></td>
    <td><code>string</code></td>
    <td>The default version name of a file based entity.</td>
</tr>
<tr>
    <td><CopyableCode code="default_version_details" /></td>
    <td><code>object</code></td>
    <td>The version details of a file based entity</td>
</tr>
<tr>
    <td><CopyableCode code="external_access_integrations" /></td>
    <td><code>array</code></td>
    <td>List of external access integrations attached to this function</td>
</tr>
<tr>
    <td><CopyableCode code="external_access_secrets" /></td>
    <td><code>string</code></td>
    <td>Secrets to be used with this function for external access</td>
</tr>
<tr>
    <td><CopyableCode code="fromLocation" /></td>
    <td><code>string</code></td>
    <td>Location to copy the file from. This must be a Snowflake stage location.</td>
</tr>
<tr>
    <td><CopyableCode code="idle_auto_shutdown_time_seconds" /></td>
    <td><code>integer (int64)</code></td>
    <td>Sets the time in seconds for when to shutdown an idle Notebook.</td>
</tr>
<tr>
    <td><CopyableCode code="import_urls" /></td>
    <td><code>array</code></td>
    <td>List of urls</td>
</tr>
<tr>
    <td><CopyableCode code="last_version_details" /></td>
    <td><code>object</code></td>
    <td>The version details of a file based entity</td>
</tr>
<tr>
    <td><CopyableCode code="live_version_location_uri" /></td>
    <td><code>string</code></td>
    <td>The current version location</td>
</tr>
<tr>
    <td><CopyableCode code="main_file" /></td>
    <td><code>string</code></td>
    <td>Name + path of the file for the Notebook</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the notebook (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the notebook (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="query_warehouse" /></td>
    <td><code>string</code></td>
    <td>Warehouse against which the queries issued by the Streamlit app are run against</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>User facing title of the Streamlit app or an Organization Profile</td>
</tr>
<tr>
    <td><CopyableCode code="user_packages" /></td>
    <td><code>string</code></td>
    <td>User packages of the notebook</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>User specified version alias</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#list_notebooks"><CopyableCode code="list_notebooks" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a>, <a href="#parameter-startsWith">startsWith</a>, <a href="#parameter-showLimit">showLimit</a>, <a href="#parameter-fromName">fromName</a></td>
    <td>List notebooks</td>
</tr>
<tr>
    <td><a href="#fetch_notebook"><CopyableCode code="fetch_notebook" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetch a notebook</td>
</tr>
<tr>
    <td><a href="#create_notebook"><CopyableCode code="create_notebook" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a></td>
    <td>Create a notebook</td>
</tr>
<tr>
    <td><a href="#delete_notebook"><CopyableCode code="delete_notebook" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Delete a notebook</td>
</tr>
<tr>
    <td><a href="#execute_notebook"><CopyableCode code="execute_notebook" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-asyncExec">asyncExec</a></td>
    <td>Execute a Notebook</td>
</tr>
<tr>
    <td><a href="#rename_notebook"><CopyableCode code="rename_notebook" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-targetName">targetName</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a>, <a href="#parameter-targetDatabase">targetDatabase</a>, <a href="#parameter-targetSchema">targetSchema</a></td>
    <td>Changes the name of the notebook to new name. The new identifier must be unique for the schema.</td>
</tr>
<tr>
    <td><a href="#add_live_version_notebook"><CopyableCode code="add_live_version_notebook" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-fromLast">fromLast</a>, <a href="#parameter-comment">comment</a></td>
    <td>Adds a LIVE version to the notebook</td>
</tr>
<tr>
    <td><a href="#commit_notebook"><CopyableCode code="commit_notebook" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-version">version</a>, <a href="#parameter-comment">comment</a></td>
    <td>If a Git connection is set up for the notebook, commits the LIVE version of the notebook to the Git repository</td>
</tr>
</tbody>
</table>## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the `/api/v2/databases` GET request to get a list of available databases. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the `/api/v2/databases/{database}/schemas` GET request to get a list of available schemas for the specified database. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-targetName">
    <td><CopyableCode code="targetName" /></td>
    <td><code>string</code></td>
    <td>Name of the target resource. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr id="parameter-asyncExec">
    <td><CopyableCode code="asyncExec" /></td>
    <td><code>boolean</code></td>
    <td>Asynchronous execution enable/disable. Default is disable. (default: false)</td>
</tr>
<tr id="parameter-comment">
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Sets a comment for the notebook or version of the notebook</td>
</tr>
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)</td>
</tr>
<tr id="parameter-fromLast">
    <td><CopyableCode code="fromLast" /></td>
    <td><code>boolean</code></td>
    <td>Sets the LIVE version to the LAST version of the notebook</td>
</tr>
<tr id="parameter-fromName">
    <td><CopyableCode code="fromName" /></td>
    <td><code>string</code></td>
    <td>Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. (example: from_test)</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. (example: true, default: false)</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. (example: test_%)</td>
</tr>
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command. (example: 10, minimum: 1, maximum: 10000)</td>
</tr>
<tr id="parameter-startsWith">
    <td><CopyableCode code="startsWith" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. (example: test)</td>
</tr>
<tr id="parameter-targetDatabase">
    <td><CopyableCode code="targetDatabase" /></td>
    <td><code>string</code></td>
    <td>Database of the target resource. Defaults to the source's database (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr id="parameter-targetSchema">
    <td><CopyableCode code="targetSchema" /></td>
    <td><code>string</code></td>
    <td>Schema of the target resource. Defaults to the source's schema (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr id="parameter-version">
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>live version of the alias</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_notebooks"
    values={[
        { label: 'list_notebooks', value: 'list_notebooks' },
        { label: 'fetch_notebook', value: 'fetch_notebook' }
    ]}
>
<TabItem value="list_notebooks">

List notebooks

```sql
SELECT
name,
url_id,
database_name,
runtime_name,
schema_name,
budget,
comment,
compute_pool,
created_on,
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
title,
user_packages,
version
FROM snowflake.notebook.notebooks
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}';
```
</TabItem>
<TabItem value="fetch_notebook">

Fetch a notebook

```sql
SELECT
name,
url_id,
database_name,
runtime_name,
schema_name,
budget,
comment,
compute_pool,
created_on,
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
title,
user_packages,
version
FROM snowflake.notebook.notebooks
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_notebook"
    values={[
        { label: 'create_notebook', value: 'create_notebook' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_notebook">

Create a notebook

```sql
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
endpoint,
createMode
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
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: notebooks
  props:
    - name: database_name
      value: string
      description: Required parameter for the notebooks resource.
    - name: schema_name
      value: string
      description: Required parameter for the notebooks resource.
    - name: endpoint
      value: string
      description: Required parameter for the notebooks resource.
    - name: name
      value: string
      description: >
        Name of the notebook
        
    - name: version
      value: string
      description: >
        User specified version alias
        
    - name: fromLocation
      value: string
      description: >
        Location to copy the file from. This must be a Snowflake stage location.
        
    - name: main_file
      value: string
      description: >
        Name + path of the file for the Notebook
        
    - name: comment
      value: string
      description: >
        user comment associated to an object in the dictionary
        
    - name: default_version
      value: string
      description: >
        The default version name of a file based entity.
        
    - name: query_warehouse
      value: string
      description: >
        Warehouse against which the queries issued by the Streamlit app are run against
        
    - name: default_version_details
      value: object
      description: >
        The version details of a file based entity
        
    - name: last_version_details
      value: object
      description: >
        The version details of a file based entity
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_notebook"
    values={[
        { label: 'delete_notebook', value: 'delete_notebook' }
    ]}
>
<TabItem value="delete_notebook">

Delete a notebook

```sql
DELETE FROM snowflake.notebook.notebooks
WHERE database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="execute_notebook"
    values={[
        { label: 'execute_notebook', value: 'execute_notebook' },
        { label: 'rename_notebook', value: 'rename_notebook' },
        { label: 'add_live_version_notebook', value: 'add_live_version_notebook' },
        { label: 'commit_notebook', value: 'commit_notebook' }
    ]}
>
<TabItem value="execute_notebook">

Execute a Notebook

```sql
EXEC snowflake.notebook.notebooks.execute_notebook 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@asyncExec={{ asyncExec }};
```
</TabItem>
<TabItem value="rename_notebook">

Changes the name of the notebook to new name. The new identifier must be unique for the schema.

```sql
EXEC snowflake.notebook.notebooks.rename_notebook 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@targetName='{{ targetName }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@ifExists={{ ifExists }}, 
@targetDatabase='{{ targetDatabase }}', 
@targetSchema='{{ targetSchema }}';
```
</TabItem>
<TabItem value="add_live_version_notebook">

Adds a LIVE version to the notebook

```sql
EXEC snowflake.notebook.notebooks.add_live_version_notebook 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@fromLast={{ fromLast }}, 
@comment='{{ comment }}';
```
</TabItem>
<TabItem value="commit_notebook">

If a Git connection is set up for the notebook, commits the LIVE version of the notebook to the Git repository

```sql
EXEC snowflake.notebook.notebooks.commit_notebook 
@database_name='{{ database_name }}' --required, 
@schema_name='{{ schema_name }}' --required, 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@version='{{ version }}', 
@comment='{{ comment }}';
```
</TabItem>
</Tabs>

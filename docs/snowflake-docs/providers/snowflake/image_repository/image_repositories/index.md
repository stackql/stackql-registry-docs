--- 
title: image_repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - image_repositories
  - image_repository
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

Creates, updates, deletes, gets or lists an <code>image_repositories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.image_repository.image_repositories" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_image_repositories"
    values={[
        { label: 'list_image_repositories', value: 'list_image_repositories' },
        { label: 'fetch_image_repository', value: 'fetch_image_repository' }
    ]}
>
<TabItem value="list_image_repositories">

A Snowflake image repository.

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
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the image repository was created.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Identifier for the current owner of the image repository.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>Role type of the image repository owner.</td>
</tr>
<tr>
    <td><CopyableCode code="repository_url" /></td>
    <td><code>string</code></td>
    <td>Current URL of the image repository.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_image_repository">

A Snowflake image repository.

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
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the image repository was created.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Identifier for the current owner of the image repository.</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>Role type of the image repository owner.</td>
</tr>
<tr>
    <td><CopyableCode code="repository_url" /></td>
    <td><code>string</code></td>
    <td>Current URL of the image repository.</td>
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
    <td><a href="#list_image_repositories"><CopyableCode code="list_image_repositories" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a></td>
    <td>Lists the image repositories under a specified database and schema.</td>
</tr>
<tr>
    <td><a href="#fetch_image_repository"><CopyableCode code="fetch_image_repository" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetches a named image repository in a specified database and schema.</td>
</tr>
<tr>
    <td><a href="#create_image_repository"><CopyableCode code="create_image_repository" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a></td>
    <td>Creates an image repository in the specified database, schema, and create mode. The `createMode` query parameter specifies what action to take based on whether the repository already exists. See the ImageRepository component definition for what is required to be provided in the request body.</td>
</tr>
<tr>
    <td><a href="#delete_image_repository"><CopyableCode code="delete_image_repository" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Deletes an image repository with the given name. If you enable the `ifExists` query parameter, the operation succeeds even if the object does not exist. Otherwise, a 404 failure is returned if the object does not exist.</td>
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
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_image_repositories"
    values={[
        { label: 'list_image_repositories', value: 'list_image_repositories' },
        { label: 'fetch_image_repository', value: 'fetch_image_repository' }
    ]}
>
<TabItem value="list_image_repositories">

Lists the image repositories under a specified database and schema.

```sql
SELECT
name,
database_name,
schema_name,
created_on,
owner,
owner_role_type,
repository_url
FROM snowflake.image_repository.image_repositories
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
<TabItem value="fetch_image_repository">

Fetches a named image repository in a specified database and schema.

```sql
SELECT
name,
database_name,
schema_name,
created_on,
owner,
owner_role_type,
repository_url
FROM snowflake.image_repository.image_repositories
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_image_repository"
    values={[
        { label: 'create_image_repository', value: 'create_image_repository' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_image_repository">

Creates an image repository in the specified database, schema, and create mode. The `createMode` query parameter specifies what action to take based on whether the repository already exists. See the ImageRepository component definition for what is required to be provided in the request body.

```sql
INSERT INTO snowflake.image_repository.image_repositories (
data__name,
data__database_name,
data__schema_name,
database_name,
schema_name,
endpoint,
createMode
)
SELECT 
'{{ name }}',
'{{ database_name }}',
'{{ schema_name }}',
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
- name: image_repositories
  props:
    - name: database_name
      value: string
      description: Required parameter for the image_repositories resource.
    - name: schema_name
      value: string
      description: Required parameter for the image_repositories resource.
    - name: endpoint
      value: string
      description: Required parameter for the image_repositories resource.
    - name: name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: database_name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: schema_name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_image_repository"
    values={[
        { label: 'delete_image_repository', value: 'delete_image_repository' }
    ]}
>
<TabItem value="delete_image_repository">

Deletes an image repository with the given name. If you enable the `ifExists` query parameter, the operation succeeds even if the object does not exist. Otherwise, a 404 failure is returned if the object does not exist.

```sql
DELETE FROM snowflake.image_repository.image_repositories
WHERE database_name = '{{ database_name }}' --required
AND schema_name = '{{ schema_name }}' --required
AND name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>

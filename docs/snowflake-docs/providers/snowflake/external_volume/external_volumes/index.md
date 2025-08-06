--- 
title: external_volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - external_volumes
  - external_volume
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

Creates, updates, deletes, gets or lists an <code>external_volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>external_volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.external_volume.external_volumes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_external_volumes"
    values={[
        { label: 'list_external_volumes', value: 'list_external_volumes' },
        { label: 'fetch_external_volume', value: 'fetch_external_volume' }
    ]}
>
<TabItem value="list_external_volumes">

A Snowflake external volume

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
    <td>String that specifies the identifier (the name) for the external volume; must be unique in your account. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_writes" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether write operations are allowed for the external volume; must be set to TRUE for Iceberg tables that use Snowflake as the catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>String (literal) that specifies a comment for the external volume.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the external volume was created.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the external volume (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the external volume (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="storage_locations" /></td>
    <td><code>array</code></td>
    <td>Set of named cloud storage locations in different regions and, optionally, cloud platforms.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_external_volume">

A Snowflake external volume

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
    <td>String that specifies the identifier (the name) for the external volume; must be unique in your account. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="allow_writes" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether write operations are allowed for the external volume; must be set to TRUE for Iceberg tables that use Snowflake as the catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>String (literal) that specifies a comment for the external volume.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the external volume was created.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td>Role that owns the external volume (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="owner_role_type" /></td>
    <td><code>string</code></td>
    <td>The type of role that owns the external volume (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$)</td>
</tr>
<tr>
    <td><CopyableCode code="storage_locations" /></td>
    <td><code>array</code></td>
    <td>Set of named cloud storage locations in different regions and, optionally, cloud platforms.</td>
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
    <td><a href="#list_external_volumes"><CopyableCode code="list_external_volumes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a></td>
    <td>List external volumes</td>
</tr>
<tr>
    <td><a href="#fetch_external_volume"><CopyableCode code="fetch_external_volume" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Fetch an external volume</td>
</tr>
<tr>
    <td><a href="#create_external_volume"><CopyableCode code="create_external_volume" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-createMode">createMode</a></td>
    <td>Create an external volume</td>
</tr>
<tr>
    <td><a href="#delete_external_volume"><CopyableCode code="delete_external_volume" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Delete an external volume</td>
</tr>
<tr>
    <td><a href="#undrop_external_volume"><CopyableCode code="undrop_external_volume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Undrop an external volume</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
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
    defaultValue="list_external_volumes"
    values={[
        { label: 'list_external_volumes', value: 'list_external_volumes' },
        { label: 'fetch_external_volume', value: 'fetch_external_volume' }
    ]}
>
<TabItem value="list_external_volumes">

List external volumes

```sql
SELECT
name,
allow_writes,
comment,
created_on,
owner,
owner_role_type,
storage_locations
FROM snowflake.external_volume.external_volumes
WHERE endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
<TabItem value="fetch_external_volume">

Fetch an external volume

```sql
SELECT
name,
allow_writes,
comment,
created_on,
owner,
owner_role_type,
storage_locations
FROM snowflake.external_volume.external_volumes
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_external_volume"
    values={[
        { label: 'create_external_volume', value: 'create_external_volume' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_external_volume">

Create an external volume

```sql
INSERT INTO snowflake.external_volume.external_volumes (
data__name,
data__storage_locations,
data__allow_writes,
data__comment,
endpoint,
createMode
)
SELECT 
'{{ name }}',
'{{ storage_locations }}',
{{ allow_writes }},
'{{ comment }}',
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: external_volumes
  props:
    - name: endpoint
      value: string
      description: Required parameter for the external_volumes resource.
    - name: name
      value: string
      description: >
        String that specifies the identifier (the name) for the external volume; must be unique in your account.
        
    - name: storage_locations
      value: array
      description: >
        Set of named cloud storage locations in different regions and, optionally, cloud platforms.
        
    - name: allow_writes
      value: boolean
      description: >
        Specifies whether write operations are allowed for the external volume; must be set to TRUE for Iceberg tables that use Snowflake as the catalog.
        
    - name: comment
      value: string
      description: >
        String (literal) that specifies a comment for the external volume.
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. (enum: [errorIfExists, orReplace, ifNotExists], example: ifNotExists, default: errorIfExists)
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_external_volume"
    values={[
        { label: 'delete_external_volume', value: 'delete_external_volume' }
    ]}
>
<TabItem value="delete_external_volume">

Delete an external volume

```sql
DELETE FROM snowflake.external_volume.external_volumes
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="undrop_external_volume"
    values={[
        { label: 'undrop_external_volume', value: 'undrop_external_volume' }
    ]}
>
<TabItem value="undrop_external_volume">

Undrop an external volume

```sql
EXEC snowflake.external_volume.external_volumes.undrop_external_volume 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
</Tabs>

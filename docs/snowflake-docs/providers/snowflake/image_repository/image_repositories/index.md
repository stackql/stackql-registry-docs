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

Creates, updates, deletes, gets or lists a <code>image_repositories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.image_repository.image_repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="created_on" /> | `string` | Time the image repository was created. |
| <CopyableCode code="database_name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="owner" /> | `string` | Identifier for the current owner of the image repository. |
| <CopyableCode code="owner_role_type" /> | `string` | Role type of the image repository owner. |
| <CopyableCode code="repository_url" /> | `string` | Current URL of the image repository. |
| <CopyableCode code="schema_name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_image_repository" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | - | Fetches a named image repository in a specified database and schema. |
| <CopyableCode code="list_image_repositories" /> | `SELECT` | <CopyableCode code="database_name, schema_name, endpoint" /> | <CopyableCode code="like" /> | Lists the image repositories under a specified database and schema. |
| <CopyableCode code="create_image_repository" /> | `INSERT` | <CopyableCode code="database_name, schema_name, data__name, endpoint" /> | <CopyableCode code="createMode" /> | Creates an image repository in the specified database, schema, and create mode. The `createMode` query parameter specifies what action to take based on whether the repository already exists. See the ImageRepository component definition for what is required to be provided in the request body. |
| <CopyableCode code="delete_image_repository" /> | `DELETE` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | <CopyableCode code="ifExists" /> | Deletes an image repository with the given name. If you enable the `ifExists` query parameter, the operation succeeds even if the object does not exist. Otherwise, a 404 failure is returned if the object does not exist. |
<br />

<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |

</details>

## `SELECT` examples

Lists the image repositories under a specified database and schema.


```sql
SELECT
name,
created_on,
database_name,
owner,
owner_role_type,
repository_url,
schema_name
FROM snowflake.image_repository.image_repositories
WHERE database_name = '{{ database_name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>image_repositories</code> resource.

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
INSERT INTO snowflake.image_repository.image_repositories (
data__name,
data__database_name,
data__schema_name,
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

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.image_repository.image_repositories (
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
- name: image_repositories
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
    - name: database_name
      value: string
    - name: schema_name
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>image_repositories</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.image_repository.image_repositories
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```

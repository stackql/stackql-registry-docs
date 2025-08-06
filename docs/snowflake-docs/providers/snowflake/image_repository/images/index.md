--- 
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
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

Creates, updates, deletes, gets or lists an <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.image_repository.images" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_images_in_repository"
    values={[
        { label: 'list_images_in_repository', value: 'list_images_in_repository' }
    ]}
>
<TabItem value="list_images_in_repository">

A image in a Snowflake image repository.

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
    <td><CopyableCode code="image_name" /></td>
    <td><code>string</code></td>
    <td>Image name.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string</code></td>
    <td>Date and time when the image was uploaded to the image repository.</td>
</tr>
<tr>
    <td><CopyableCode code="digest" /></td>
    <td><code>string</code></td>
    <td>SHA256 digest of the image.</td>
</tr>
<tr>
    <td><CopyableCode code="image_path" /></td>
    <td><code>string</code></td>
    <td>Image path (database_name/schema_name/repository_name/image_name:image_tag).</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>string</code></td>
    <td>Image tags.</td>
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
    <td><a href="#list_images_in_repository"><CopyableCode code="list_images_in_repository" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-database_name">database_name</a>, <a href="#parameter-schema_name">schema_name</a>, <a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>List images in the given image repository.</td>
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
    <td>Identifier (i.e. name) for the database to which the resource belongs. You can use the `/api/v2/databases` GET request to get a list of available databases. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
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
<tr id="parameter-schema_name">
    <td><CopyableCode code="schema_name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the schema to which the resource belongs. You can use the `/api/v2/databases/{database}/schemas` GET request to get a list of available schemas for the specified database. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_images_in_repository"
    values={[
        { label: 'list_images_in_repository', value: 'list_images_in_repository' }
    ]}
>
<TabItem value="list_images_in_repository">

List images in the given image repository.

```sql
SELECT
image_name,
created_on,
digest,
image_path,
tags
FROM snowflake.image_repository.images
WHERE database_name = '{{ database_name }}' -- required
AND schema_name = '{{ schema_name }}' -- required
AND name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>

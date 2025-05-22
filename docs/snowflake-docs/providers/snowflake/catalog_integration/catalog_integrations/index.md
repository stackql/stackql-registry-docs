---
title: catalog_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - catalog_integrations
  - catalog_integration
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

Creates, updates, deletes, gets or lists a <code>catalog_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>catalog_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.catalog_integration.catalog_integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the catalog integration. |
| <CopyableCode code="catalog" /> | `object` |  |
| <CopyableCode code="category" /> | `string` | Category of the integration. Always CATALOG. |
| <CopyableCode code="comment" /> | `string` | Comment. |
| <CopyableCode code="created_on" /> | `string` | Date and time when the catalog integration was created. |
| <CopyableCode code="enabled" /> | `boolean` | whether this catalog integration is available to use for Iceberg tables. |
| <CopyableCode code="table_format" /> | `string` | Table format of the catalog. |
| <CopyableCode code="type" /> | `string` | Type of the integration. Always CATALOG. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_catalog_integration" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | - | Fetch a catalog integration. |
| <CopyableCode code="list_catalog_integrations" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" /> | List catalog integrations. |
| <CopyableCode code="create_catalog_integration" /> | `INSERT` | <CopyableCode code="data__catalog, data__enabled, data__name, data__table_format, endpoint" /> | <CopyableCode code="createMode" /> | Create a catalog integration. |
| <CopyableCode code="delete_catalog_integration" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a catalog integration. |


Expand this to view optional parameter details for all methods in this resource.


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |

</details>

## `SELECT` examples

List catalog integrations.


```sql
SELECT
name,
catalog,
category,
comment,
created_on,
enabled,
table_format,
type
FROM snowflake.catalog_integration.catalog_integrations
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>catalog_integrations</code> resource.

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
INSERT INTO snowflake.catalog_integration.catalog_integrations (
data__name,
data__catalog,
data__table_format,
data__enabled,
data__comment,
endpoint
)
SELECT 
'{{ name }}',
'{{ catalog }}',
'{{ table_format }}',
'{{ enabled }}',
'{{ comment }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.catalog_integration.catalog_integrations (
data__name,
data__catalog,
data__table_format,
data__enabled,
endpoint
)
SELECT 
'{{ name }}',
'{{ catalog }}',
'{{ table_format }}',
'{{ enabled }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: catalog_integrations
  props:
    - name: data__catalog
      value: string
    - name: data__enabled
      value: string
    - name: data__name
      value: string
    - name: data__table_format
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
    - name: catalog
      props:
        - name: catalog_source
          value: string
    - name: table_format
      value: string
    - name: enabled
      value: boolean
    - name: comment
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>catalog_integrations</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.catalog_integration.catalog_integrations
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```

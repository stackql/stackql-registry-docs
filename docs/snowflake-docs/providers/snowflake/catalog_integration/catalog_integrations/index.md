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

<Tabs
    defaultValue="list_catalog_integrations"
    values={[
        { label: 'list_catalog_integrations', value: 'list_catalog_integrations' },
        { label: 'fetch_catalog_integration', value: 'fetch_catalog_integration' }
    ]
}>
<TabItem value="list_catalog_integrations">

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
</TabItem>
<TabItem value="fetch_catalog_integration">

Fetch a catalog integration.

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
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Create a catalog integration.

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
{{ enabled }},
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
{{ enabled }},
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: catalog_integrations
  props:
    - name: endpoint
      value: string
      description: Required parameter for the catalog_integrations resource.
    - name: name
      value: string
      description: >-
        Name of the catalog integration. (Required parameter for the
        catalog_integrations resource.)
    - name: catalog
      value:
        catalog_source: string
      description: Required parameter for the catalog_integrations resource.
    - name: table_format
      value: string
      description: >-
        Table format of the catalog. (valid values: 'ICEBERG') (Required
        parameter for the catalog_integrations resource.)
    - name: enabled
      value: boolean
      description: >-
        whether this catalog integration is available to use for Iceberg tables.
        (Required parameter for the catalog_integrations resource.)
    - name: comment
      value: string
      description: Comment.
```
</TabItem>
</Tabs>

## `DELETE` example

Delete a catalog integration.

```sql
/*+ delete */
DELETE FROM snowflake.catalog_integration.catalog_integrations
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```

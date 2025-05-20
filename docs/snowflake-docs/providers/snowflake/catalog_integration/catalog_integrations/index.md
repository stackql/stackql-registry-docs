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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_catalog_integration" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | Fetch a catalog integration. |
| <CopyableCode code="list_catalog_integrations" /> | `SELECT` | <CopyableCode code="endpoint" /> | List catalog integrations. |
| <CopyableCode code="create_catalog_integration" /> | `INSERT` | <CopyableCode code="data__catalog, data__enabled, data__name, data__table_format, endpoint" /> | Create a catalog integration. |
| <CopyableCode code="delete_catalog_integration" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | Delete a catalog integration. |

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

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.catalog_integration.catalog_integrations (
data__catalog,
data__table_format,
data__name,
endpoint,
data__enabled
)
SELECT 
'{ table_format }',
'{ endpoint }',
'{ enabled }',
'{ catalog }',
'{ name }'
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>catalog_integrations</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.catalog_integration.catalog_integrations
WHERE name = '{ name }' AND endpoint = '{ endpoint }';
```

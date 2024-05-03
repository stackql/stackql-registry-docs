---
title: data_cells_filter
hide_title: false
hide_table_of_contents: false
keywords:
  - data_cells_filter
  - lakeformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>data_cells_filter</code> resource, use <code>data_cells_filters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_cells_filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema representing a Lake Formation Data Cells Filter.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lakeformation.data_cells_filter" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="table_catalog_id" /></td><td><code>string</code></td><td>The Catalog Id of the Table on which to create a Data Cells Filter.</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>string</code></td><td>The name of the Database that the Table resides in.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>The name of the Table to create a Data Cells Filter for.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The desired name of the Data Cells Filter.</td></tr>
<tr><td><CopyableCode code="row_filter" /></td><td><code>object</code></td><td>An object representing the Data Cells Filter's Row Filter. Either a Filter Expression or a Wildcard is required</td></tr>
<tr><td><CopyableCode code="column_names" /></td><td><code>array</code></td><td>A list of columns to be included in this Data Cells Filter.</td></tr>
<tr><td><CopyableCode code="column_wildcard" /></td><td><code>object</code></td><td>An object representing the Data Cells Filter's Columns. Either Column Names or a Wildcard is required</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
table_catalog_id,
database_name,
table_name,
name,
row_filter,
column_names,
column_wildcard
FROM aws.lakeformation.data_cells_filter
WHERE data__Identifier = '<TableCatalogId>|<DatabaseName>|<TableName>|<Name>';
```

## Permissions

To operate on the <code>data_cells_filter</code> resource, the following permissions are required:

### Delete
```json
lakeformation:DeleteDataCellsFilter
```

### Read
```json
lakeformation:ListDataCellsFilter
```


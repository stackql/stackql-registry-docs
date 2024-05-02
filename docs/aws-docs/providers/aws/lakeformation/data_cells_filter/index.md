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
Gets or operates on an individual <code>data_cells_filter</code> resource, use <code>data_cells_filters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_cells_filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema representing a Lake Formation Data Cells Filter.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lakeformation.data_cells_filter</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>table_catalog_id</code></td><td><code>string</code></td><td>The Catalog Id of the Table on which to create a Data Cells Filter.</td></tr>
<tr><td><code>database_name</code></td><td><code>string</code></td><td>The name of the Database that the Table resides in.</td></tr>
<tr><td><code>table_name</code></td><td><code>string</code></td><td>The name of the Table to create a Data Cells Filter for.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The desired name of the Data Cells Filter.</td></tr>
<tr><td><code>row_filter</code></td><td><code>object</code></td><td>An object representing the Data Cells Filter's Row Filter. Either a Filter Expression or a Wildcard is required</td></tr>
<tr><td><code>column_names</code></td><td><code>array</code></td><td>A list of columns to be included in this Data Cells Filter.</td></tr>
<tr><td><code>column_wildcard</code></td><td><code>object</code></td><td>An object representing the Data Cells Filter's Columns. Either Column Names or a Wildcard is required</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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


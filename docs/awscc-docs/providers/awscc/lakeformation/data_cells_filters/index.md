---
title: data_cells_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - data_cells_filters
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
Retrieves a list of <code>data_cells_filters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_cells_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_cells_filters</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lakeformation.data_cells_filters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>table_catalog_id</code></td><td><code>undefined</code></td><td>The Catalog Id of the Table on which to create a Data Cells Filter.</td></tr>
<tr><td><code>database_name</code></td><td><code>undefined</code></td><td>The name of the Database that the Table resides in.</td></tr>
<tr><td><code>table_name</code></td><td><code>undefined</code></td><td>The name of the Table to create a Data Cells Filter for.</td></tr>
<tr><td><code>name</code></td><td><code>undefined</code></td><td>The desired name of the Data Cells Filter.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>data_cells_filters</code> resource, the following permissions are required:

### Create
```json
lakeformation:CreateDataCellsFilter,
glue:GetTable
```

### List
```json
lakeformation:ListDataCellsFilter
```


## Example
```sql
SELECT
region,
table_catalog_id,
database_name,
table_name,
name
FROM awscc.lakeformation.data_cells_filters
WHERE region = 'us-east-1'
```

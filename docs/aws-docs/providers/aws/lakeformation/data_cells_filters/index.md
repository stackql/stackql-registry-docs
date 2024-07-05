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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>data_cells_filter</code> resource or lists <code>data_cells_filters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_cells_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema representing a Lake Formation Data Cells Filter.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lakeformation.data_cells_filters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="table_catalog_id" /></td><td><code>string</code></td><td>The Catalog Id of the Table on which to create a Data Cells Filter.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="TableCatalogId, DatabaseName, TableName, Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>data_cells_filters</code> in a region.
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
FROM aws.lakeformation.data_cells_filters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>data_cells_filter</code>.
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
FROM aws.lakeformation.data_cells_filters
WHERE region = 'us-east-1' AND data__Identifier = '<TableCatalogId>|<DatabaseName>|<TableName>|<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_cells_filter</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.lakeformation.data_cells_filters (
 TableCatalogId,
 DatabaseName,
 TableName,
 Name,
 region
)
SELECT 
'{{ TableCatalogId }}',
 '{{ DatabaseName }}',
 '{{ TableName }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lakeformation.data_cells_filters (
 TableCatalogId,
 DatabaseName,
 TableName,
 Name,
 RowFilter,
 ColumnNames,
 ColumnWildcard,
 region
)
SELECT 
 '{{ TableCatalogId }}',
 '{{ DatabaseName }}',
 '{{ TableName }}',
 '{{ Name }}',
 '{{ RowFilter }}',
 '{{ ColumnNames }}',
 '{{ ColumnWildcard }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: data_cells_filter
    props:
      - name: TableCatalogId
        value: '{{ TableCatalogId }}'
      - name: DatabaseName
        value: '{{ DatabaseName }}'
      - name: TableName
        value: null
      - name: Name
        value: null
      - name: RowFilter
        value:
          FilterExpression: '{{ FilterExpression }}'
          AllRowsWildcard: {}
      - name: ColumnNames
        value:
          - null
      - name: ColumnWildcard
        value:
          ExcludedColumnNames: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lakeformation.data_cells_filters
WHERE data__Identifier = '<TableCatalogId|DatabaseName|TableName|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_cells_filters</code> resource, the following permissions are required:

### Create
```json
lakeformation:CreateDataCellsFilter,
glue:GetTable
```

### Delete
```json
lakeformation:DeleteDataCellsFilter
```

### Read
```json
lakeformation:ListDataCellsFilter
```

### List
```json
lakeformation:ListDataCellsFilter
```


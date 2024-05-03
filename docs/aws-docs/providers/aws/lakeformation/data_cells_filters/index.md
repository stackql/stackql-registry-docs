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

Used to retrieve a list of <code>data_cells_filters</code> in a region or create a <code>data_cells_filters</code> resource, use <code>data_cells_filter</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_cells_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema representing a Lake Formation Data Cells Filter.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lakeformation.data_cells_filters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="table_catalog_id" /></td><td><code>undefined</code></td><td>The Catalog Id of the Table on which to create a Data Cells Filter.</td></tr>
<tr><td><CopyableCode code="database_name" /></td><td><code>undefined</code></td><td>The name of the Database that the Table resides in.</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>undefined</code></td><td>The name of the Table to create a Data Cells Filter for.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>undefined</code></td><td>The desired name of the Data Cells Filter.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
table_catalog_id,
database_name,
table_name,
name
FROM aws.lakeformation.data_cells_filters
WHERE region = 'us-east-1'
```

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


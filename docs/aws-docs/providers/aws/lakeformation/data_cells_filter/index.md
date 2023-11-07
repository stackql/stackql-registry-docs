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
Gets an individual <code>data_cells_filter</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_cells_filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_cells_filter</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lakeformation.data_cells_filter</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>TableCatalogId</code></td><td><code>undefined</code></td><td>The Catalog Id of the Table on which to create a Data Cells Filter.</td></tr>
<tr><td><code>DatabaseName</code></td><td><code>undefined</code></td><td>The name of the Database that the Table resides in.</td></tr>
<tr><td><code>TableName</code></td><td><code>undefined</code></td><td>The name of the Table to create a Data Cells Filter for.</td></tr>
<tr><td><code>Name</code></td><td><code>undefined</code></td><td>The desired name of the Data Cells Filter.</td></tr>
<tr><td><code>RowFilter</code></td><td><code>undefined</code></td><td>An object representing the Data Cells Filter's Row Filter. Either a Filter Expression or a Wildcard is required</td></tr>
<tr><td><code>ColumnNames</code></td><td><code>undefined</code></td><td>A list of columns to be included in this Data Cells Filter.</td></tr>
<tr><td><code>ColumnWildcard</code></td><td><code>undefined</code></td><td>An object representing the Data Cells Filter's Columns. Either Column Names or a Wildcard is required</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lakeformation.data_cells_filter
WHERE region = 'us-east-1' AND data__Identifier = '&lt;TableCatalogId&gt;' AND data__Identifier = '&lt;DatabaseName&gt;' AND data__Identifier = '&lt;TableName&gt;' AND data__Identifier = '&lt;Name&gt;'
</pre>

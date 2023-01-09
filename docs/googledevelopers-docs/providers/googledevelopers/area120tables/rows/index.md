---
title: rows
hide_title: false
hide_table_of_contents: false
keywords:
  - rows
  - area120tables
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.area120tables.rows</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the row. Row names have the form `tables/&#123;table&#125;/rows/&#123;row&#125;`. The name is ignored when creating a row. |
| `updateTime` | `string` | Time when the row was last updated. |
| `values` | `object` | The values of the row. This is a map of column key to value. Key is user entered name(default) or the internal column id based on the view in the request. |
| `createTime` | `string` | Time when the row was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `tables_rows_get` | `SELECT` | `rowsId, tablesId` | Gets a row. Returns NOT_FOUND if the row does not exist in the table. |
| `tables_rows_list` | `SELECT` | `tablesId` | Lists rows in a table. Returns NOT_FOUND if the table does not exist. |
| `tables_rows_create` | `INSERT` | `tablesId` | Creates a row. |
| `tables_rows_delete` | `DELETE` | `rowsId, tablesId` | Deletes a row. |
| `tables_rows_batchCreate` | `EXEC` | `tablesId` | Creates multiple rows. |
| `tables_rows_batchDelete` | `EXEC` | `tablesId` | Deletes multiple rows. |
| `tables_rows_batchUpdate` | `EXEC` | `tablesId` | Updates multiple rows. |
| `tables_rows_patch` | `EXEC` | `rowsId, tablesId` | Updates a row. |

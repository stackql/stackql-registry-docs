---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
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
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.area120tables.tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the table. Table names have the form `tables/&#123;table&#125;`. |
| `timeZone` | `string` | The time zone of the table. IANA Time Zone Database time zone, e.g. "America/New_York". |
| `updateTime` | `string` | Time when the table was last updated excluding updates to individual rows |
| `columns` | `array` | List of columns in this table. Order of columns matches the display order. |
| `createTime` | `string` | Time when the table was created. |
| `displayName` | `string` | The human readable title of the table. |
| `savedViews` | `array` | Saved views for this table. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `tablesId` | Gets a table. Returns NOT_FOUND if the table does not exist. |
| `list` | `SELECT` |  | Lists tables for the user. |

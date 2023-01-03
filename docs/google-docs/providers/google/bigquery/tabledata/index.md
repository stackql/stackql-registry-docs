---
title: tabledata
hide_title: false
hide_table_of_contents: false
keywords:
  - tabledata
  - bigquery
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tabledata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.tabledata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `pageToken` | `string` | A token used for paging results. Providing this token instead of the startIndex parameter can help you retrieve stable results when an underlying table is changing. |
| `rows` | `array` | Rows of results. |
| `totalRows` | `string` | The total number of rows in the complete table. |
| `etag` | `string` | A hash of this page of results. |
| `kind` | `string` | The resource type of the response. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `datasetId, projectId, tableId` | Retrieves table data from a specified set of rows. Requires the READER dataset role. |
| `insertAll` | `INSERT` | `datasetId, projectId, tableId` | Streams data into BigQuery one record at a time without needing to run a load job. Requires the WRITER dataset role. |

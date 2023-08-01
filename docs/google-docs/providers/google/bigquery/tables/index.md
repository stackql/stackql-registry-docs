---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - bigquery
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | The type of list. |
| `nextPageToken` | `string` | A token to request the next page of results. |
| `tables` | `array` | Tables in the requested dataset. |
| `totalItems` | `integer` | The total number of tables in the dataset. |
| `etag` | `string` | A hash of this page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetId, projectId, tableId` | Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table. |
| `list` | `SELECT` | `datasetId, projectId` | Lists all tables in the specified dataset. Requires the READER dataset role. |
| `insert` | `INSERT` | `datasetId, projectId` | Creates a new, empty table in the dataset. |
| `delete` | `DELETE` | `datasetId, projectId, tableId` | Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted. |
| `patch` | `EXEC` | `datasetId, projectId, tableId` | Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports patch semantics. |
| `update` | `EXEC` | `datasetId, projectId, tableId` | Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. |

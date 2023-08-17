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
| `id` | `string` | An opaque ID of the table |
| `rangePartitioning` | `object` |  |
| `timePartitioning` | `object` |  |
| `type` | `string` | The type of table. Possible values are: TABLE, VIEW. |
| `clustering` | `object` |  |
| `creationTime` | `string` | The time when this table was created, in milliseconds since the epoch. |
| `kind` | `string` | The resource type. |
| `labels` | `object` | The labels associated with this table. You can use these to organize and group your tables. |
| `expirationTime` | `string` | [Optional] The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. |
| `view` | `object` | Additional details for a view. |
| `friendlyName` | `string` | The user-friendly name for this table. |
| `tableReference` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `datasetId, projectId, tableId` | Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table. |
| `list` | `SELECT` | `datasetId, projectId` | Lists all tables in the specified dataset. Requires the READER dataset role. |
| `insert` | `INSERT` | `datasetId, projectId` | Creates a new, empty table in the dataset. |
| `delete` | `DELETE` | `datasetId, projectId, tableId` | Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted. |
| `_list` | `EXEC` | `datasetId, projectId` | Lists all tables in the specified dataset. Requires the READER dataset role. |
| `patch` | `EXEC` | `datasetId, projectId, tableId` | Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports patch semantics. |
| `update` | `EXEC` | `datasetId, projectId, tableId` | Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. |

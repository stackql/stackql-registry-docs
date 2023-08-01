---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - bigtableadmin
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
<tr><td><b>Id</b></td><td><code>google.bigtableadmin.tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Set if not all tables could be returned in a single response. Pass this value to `page_token` in another request to get the next page of results. |
| `tables` | `array` | The tables present in the requested instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, projectsId, tablesId` | Gets metadata information about the specified table. |
| `list` | `SELECT` | `instancesId, projectsId` | Lists all tables served from a specified instance. |
| `create` | `INSERT` | `instancesId, projectsId` | Creates a new table in the specified instance. The table can be created with a full set of initial column families, specified in the request. |
| `delete` | `DELETE` | `instancesId, projectsId, tablesId` | Permanently deletes a specified table and all of its data. |
| `check_consistency` | `EXEC` | `instancesId, projectsId, tablesId` | Checks replication consistency based on a consistency token, that is, if replication has caught up based on the conditions specified in the token and the check request. |
| `drop_row_range` | `EXEC` | `instancesId, projectsId, tablesId` | Permanently drop/delete a row range from a specified table. The request can specify whether to delete all rows in a table, or only those that match a particular prefix. |
| `generate_consistency_token` | `EXEC` | `instancesId, projectsId, tablesId` | Generates a consistency token for a Table, which can be used in CheckConsistency to check whether mutations to the table that finished before this call started have been replicated. The tokens will be available for 90 days. |
| `modify_column_families` | `EXEC` | `instancesId, projectsId, tablesId` | Performs a series of column family modifications on the specified table. Either all or none of the modifications will occur before this method returns, but data requests received prior to that point may see a table where only some modifications have taken effect. |
| `patch` | `EXEC` | `instancesId, projectsId, tablesId` | Updates a specified table. |
| `restore` | `EXEC` | `instancesId, projectsId` | Create a new table by restoring from a completed backup. The returned table long-running operation can be used to track the progress of the operation, and to cancel it. The metadata field type is RestoreTableMetadata. The response type is Table, if successful. |
| `undelete` | `EXEC` | `instancesId, projectsId, tablesId` | Restores a specified table which was accidentally deleted. |

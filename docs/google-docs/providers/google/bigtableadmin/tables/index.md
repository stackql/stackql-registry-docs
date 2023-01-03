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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL` |
| `granularity` | `string` | Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`. |
| `restoreInfo` | `object` | Information about a table restore. |
| `clusterStates` | `object` | Output only. Map from cluster ID to per-cluster table state. If it could not be determined whether or not the table has data in a particular cluster (for example, if its zone is unavailable), then there will be an entry for the cluster with UNKNOWN `replication_status`. Views: `REPLICATION_VIEW`, `ENCRYPTION_VIEW`, `FULL` |
| `columnFamilies` | `object` | The column families configured for this table, mapped by column family ID. Views: `SCHEMA_VIEW`, `FULL` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_instances_tables_get` | `SELECT` | `instancesId, projectsId, tablesId` | Gets metadata information about the specified table. |
| `projects_instances_tables_list` | `SELECT` | `instancesId, projectsId` | Lists all tables served from a specified instance. |
| `projects_instances_tables_create` | `INSERT` | `instancesId, projectsId` | Creates a new table in the specified instance. The table can be created with a full set of initial column families, specified in the request. |
| `projects_instances_tables_delete` | `DELETE` | `instancesId, projectsId, tablesId` | Permanently deletes a specified table and all of its data. |
| `projects_instances_tables_checkConsistency` | `EXEC` | `instancesId, projectsId, tablesId` | Checks replication consistency based on a consistency token, that is, if replication has caught up based on the conditions specified in the token and the check request. |
| `projects_instances_tables_dropRowRange` | `EXEC` | `instancesId, projectsId, tablesId` | Permanently drop/delete a row range from a specified table. The request can specify whether to delete all rows in a table, or only those that match a particular prefix. |
| `projects_instances_tables_generateConsistencyToken` | `EXEC` | `instancesId, projectsId, tablesId` | Generates a consistency token for a Table, which can be used in CheckConsistency to check whether mutations to the table that finished before this call started have been replicated. The tokens will be available for 90 days. |
| `projects_instances_tables_modifyColumnFamilies` | `EXEC` | `instancesId, projectsId, tablesId` | Performs a series of column family modifications on the specified table. Either all or none of the modifications will occur before this method returns, but data requests received prior to that point may see a table where only some modifications have taken effect. |
| `projects_instances_tables_restore` | `EXEC` | `instancesId, projectsId` | Create a new table by restoring from a completed backup. The new table must be in the same project as the instance containing the backup. The returned table long-running operation can be used to track the progress of the operation, and to cancel it. The metadata field type is RestoreTableMetadata. The response type is Table, if successful. |
| `projects_instances_tables_undelete` | `EXEC` | `instancesId, projectsId, tablesId` | Restores a specified table which was accidentally deleted. |

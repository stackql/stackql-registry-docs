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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigtableadmin.tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique name of the table. Values are of the form `projects/&#123;project&#125;/instances/&#123;instance&#125;/tables/_a-zA-Z0-9*`. Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `STATS_VIEW`, `FULL` |
| <CopyableCode code="automatedBackupPolicy" /> | `object` | Defines an automated backup policy for a table |
| <CopyableCode code="changeStreamConfig" /> | `object` | Change stream configuration. |
| <CopyableCode code="clusterStates" /> | `object` | Output only. Map from cluster ID to per-cluster table state. If it could not be determined whether or not the table has data in a particular cluster (for example, if its zone is unavailable), then there will be an entry for the cluster with UNKNOWN `replication_status`. Views: `REPLICATION_VIEW`, `ENCRYPTION_VIEW`, `FULL` |
| <CopyableCode code="columnFamilies" /> | `object` | The column families configured for this table, mapped by column family ID. Views: `SCHEMA_VIEW`, `STATS_VIEW`, `FULL` |
| <CopyableCode code="deletionProtection" /> | `boolean` | Set to true to make the table protected against data loss. i.e. deleting the following resources through Admin APIs are prohibited: * The table. * The column families in the table. * The instance containing the table. Note one can still delete the data stored in the table through Data APIs. |
| <CopyableCode code="granularity" /> | `string` | Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`. |
| <CopyableCode code="restoreInfo" /> | `object` | Information about a table restore. |
| <CopyableCode code="stats" /> | `object` | Approximate statistics related to a table. These statistics are calculated infrequently, while simultaneously, data in the table can change rapidly. Thus the values reported here (e.g. row count) are very likely out-of date, even the instant they are received in this API. Thus, only treat these values as approximate. IMPORTANT: Everything below is approximate, unless otherwise specified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Gets metadata information about the specified table. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancesId, projectsId" /> | Lists all tables served from a specified instance. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="instancesId, projectsId" /> | Creates a new table in the specified instance. The table can be created with a full set of initial column families, specified in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Permanently deletes a specified table and all of its data. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Updates a specified table. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="instancesId, projectsId" /> | Lists all tables served from a specified instance. |
| <CopyableCode code="check_consistency" /> | `EXEC` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Checks replication consistency based on a consistency token, that is, if replication has caught up based on the conditions specified in the token and the check request. |
| <CopyableCode code="drop_row_range" /> | `EXEC` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Permanently drop/delete a row range from a specified table. The request can specify whether to delete all rows in a table, or only those that match a particular prefix. Note that row key prefixes used here are treated as service data. For more information about how service data is handled, see the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). |
| <CopyableCode code="generate_consistency_token" /> | `EXEC` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Generates a consistency token for a Table, which can be used in CheckConsistency to check whether mutations to the table that finished before this call started have been replicated. The tokens will be available for 90 days. |
| <CopyableCode code="modify_column_families" /> | `EXEC` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Performs a series of column family modifications on the specified table. Either all or none of the modifications will occur before this method returns, but data requests received prior to that point may see a table where only some modifications have taken effect. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="instancesId, projectsId" /> | Create a new table by restoring from a completed backup. The returned table long-running operation can be used to track the progress of the operation, and to cancel it. The metadata field type is RestoreTableMetadata. The response type is Table, if successful. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="instancesId, projectsId, tablesId" /> | Restores a specified table which was accidentally deleted. |

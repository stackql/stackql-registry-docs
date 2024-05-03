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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output-only] An opaque ID uniquely identifying the table. |
| <CopyableCode code="description" /> | `string` | [Optional] A user-friendly description of this table. |
| <CopyableCode code="biglakeConfiguration" /> | `object` |  |
| <CopyableCode code="cloneDefinition" /> | `object` |  |
| <CopyableCode code="clustering" /> | `object` |  |
| <CopyableCode code="creationTime" /> | `string` | [Output-only] The time when this table was created, in milliseconds since the epoch. |
| <CopyableCode code="defaultCollation" /> | `string` | [Output-only] The default collation of the table. |
| <CopyableCode code="defaultRoundingMode" /> | `string` | [Output-only] The default rounding mode of the table. |
| <CopyableCode code="encryptionConfiguration" /> | `object` |  |
| <CopyableCode code="etag" /> | `string` | [Output-only] A hash of the table metadata. Used to ensure there were no concurrent modifications to the resource when attempting an update. Not guaranteed to change when the table contents or the fields numRows, numBytes, numLongTermBytes or lastModifiedTime change. |
| <CopyableCode code="expirationTime" /> | `string` | [Optional] The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created tables. |
| <CopyableCode code="externalDataConfiguration" /> | `object` |  |
| <CopyableCode code="friendlyName" /> | `string` | [Optional] A descriptive name for this table. |
| <CopyableCode code="kind" /> | `string` | [Output-only] The type of the resource. |
| <CopyableCode code="labels" /> | `object` | The labels associated with this table. You can use these to organize and group your tables. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key. |
| <CopyableCode code="lastModifiedTime" /> | `string` | [Output-only] The time when this table was last modified, in milliseconds since the epoch. |
| <CopyableCode code="location" /> | `string` | [Output-only] The geographic location where the table resides. This value is inherited from the dataset. |
| <CopyableCode code="materializedView" /> | `object` |  |
| <CopyableCode code="maxStaleness" /> | `string` | [Optional] Max staleness of data that could be returned when table or materialized view is queried (formatted as Google SQL Interval type). |
| <CopyableCode code="model" /> | `object` |  |
| <CopyableCode code="numActiveLogicalBytes" /> | `string` | [Output-only] Number of logical bytes that are less than 90 days old. |
| <CopyableCode code="numActivePhysicalBytes" /> | `string` | [Output-only] Number of physical bytes less than 90 days old. This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="numBytes" /> | `string` | [Output-only] The size of this table in bytes, excluding any data in the streaming buffer. |
| <CopyableCode code="numLongTermBytes" /> | `string` | [Output-only] The number of bytes in the table that are considered "long-term storage". |
| <CopyableCode code="numLongTermLogicalBytes" /> | `string` | [Output-only] Number of logical bytes that are more than 90 days old. |
| <CopyableCode code="numLongTermPhysicalBytes" /> | `string` | [Output-only] Number of physical bytes more than 90 days old. This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="numPartitions" /> | `string` | [Output-only] The number of partitions present in the table or materialized view. This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="numPhysicalBytes" /> | `string` | [Output-only] [TrustedTester] The physical size of this table in bytes, excluding any data in the streaming buffer. This includes compression and storage used for time travel. |
| <CopyableCode code="numRows" /> | `string` | [Output-only] The number of rows of data in this table, excluding any data in the streaming buffer. |
| <CopyableCode code="numTimeTravelPhysicalBytes" /> | `string` | [Output-only] Number of physical bytes used by time travel storage (deleted or changed data). This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="numTotalLogicalBytes" /> | `string` | [Output-only] Total number of logical bytes in the table or materialized view. |
| <CopyableCode code="numTotalPhysicalBytes" /> | `string` | [Output-only] The physical size of this table in bytes. This also includes storage used for time travel. This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="rangePartitioning" /> | `object` |  |
| <CopyableCode code="requirePartitionFilter" /> | `boolean` | [Optional] If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. |
| <CopyableCode code="schema" /> | `object` |  |
| <CopyableCode code="selfLink" /> | `string` | [Output-only] A URL that can be used to access this resource again. |
| <CopyableCode code="snapshotDefinition" /> | `object` |  |
| <CopyableCode code="streamingBuffer" /> | `object` |  |
| <CopyableCode code="tableConstraints" /> | `object` |  |
| <CopyableCode code="tableReference" /> | `object` |  |
| <CopyableCode code="timePartitioning" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | [Output-only] Describes the table type. The following values are supported: TABLE: A normal BigQuery table. VIEW: A virtual table defined by a SQL query. SNAPSHOT: An immutable, read-only table that is a copy of another table. [TrustedTester] MATERIALIZED_VIEW: SQL query whose result is persisted. EXTERNAL: A table that references data stored in an external storage system, such as Google Cloud Storage. The default value is TABLE. |
| <CopyableCode code="view" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetId, projectId, tableId" /> | Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="datasetId, projectId" /> | Lists all tables in the specified dataset. Requires the READER dataset role. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="datasetId, projectId" /> | Creates a new, empty table in the dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetId, projectId, tableId" /> | Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="datasetId, projectId" /> | Lists all tables in the specified dataset. Requires the READER dataset role. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="datasetId, projectId, tableId" /> | Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports patch semantics. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="datasetId, projectId, tableId" /> | Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. |

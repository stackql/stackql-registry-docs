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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. An opaque ID uniquely identifying the table. |
| <CopyableCode code="description" /> | `string` | Optional. A user-friendly description of this table. |
| <CopyableCode code="biglakeConfiguration" /> | `object` | Configuration for BigLake managed tables. |
| <CopyableCode code="cloneDefinition" /> | `object` | Information about base table and clone time of a table clone. |
| <CopyableCode code="clustering" /> | `object` | Configures table clustering. |
| <CopyableCode code="creationTime" /> | `string` | Output only. The time when this table was created, in milliseconds since the epoch. |
| <CopyableCode code="defaultCollation" /> | `string` | Optional. Defines the default collation specification of new STRING fields in the table. During table creation or update, if a STRING field is added to this table without explicit collation specified, then the table inherits the table default collation. A change to this field affects only fields added afterwards, and does not alter the existing fields. The following values are supported: * 'und:ci': undetermined locale, case insensitive. * '': empty string. Default to case-sensitive behavior. |
| <CopyableCode code="defaultRoundingMode" /> | `string` | Optional. Defines the default rounding mode specification of new decimal fields (NUMERIC OR BIGNUMERIC) in the table. During table creation or update, if a decimal field is added to this table without an explicit rounding mode specified, then the field inherits the table default rounding mode. Changing this field doesn't affect existing fields. |
| <CopyableCode code="encryptionConfiguration" /> | `object` | Configuration for Cloud KMS encryption settings. |
| <CopyableCode code="etag" /> | `string` | Output only. A hash of this resource. |
| <CopyableCode code="expirationTime" /> | `string` | Optional. The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created tables. |
| <CopyableCode code="externalCatalogTableOptions" /> | `object` | Metadata about open source compatible table. The fields contained in these options correspond to hive metastore's table level properties. |
| <CopyableCode code="externalDataConfiguration" /> | `object` |  |
| <CopyableCode code="friendlyName" /> | `string` | Optional. A descriptive name for this table. |
| <CopyableCode code="kind" /> | `string` | The type of resource ID. |
| <CopyableCode code="labels" /> | `object` | The labels associated with this table. You can use these to organize and group your tables. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key. |
| <CopyableCode code="lastModifiedTime" /> | `string` | Output only. The time when this table was last modified, in milliseconds since the epoch. |
| <CopyableCode code="location" /> | `string` | Output only. The geographic location where the table resides. This value is inherited from the dataset. |
| <CopyableCode code="materializedView" /> | `object` | Definition and configuration of a materialized view. |
| <CopyableCode code="materializedViewStatus" /> | `object` | Status of a materialized view. The last refresh timestamp status is omitted here, but is present in the MaterializedViewDefinition message. |
| <CopyableCode code="maxStaleness" /> | `string` | Optional. The maximum staleness of data that could be returned when the table (or stale MV) is queried. Staleness encoded as a string encoding of sql IntervalValue type. |
| <CopyableCode code="model" /> | `object` |  |
| <CopyableCode code="numActiveLogicalBytes" /> | `string` | Output only. Number of logical bytes that are less than 90 days old. |
| <CopyableCode code="numActivePhysicalBytes" /> | `string` | Output only. Number of physical bytes less than 90 days old. This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="numBytes" /> | `string` | Output only. The size of this table in logical bytes, excluding any data in the streaming buffer. |
| <CopyableCode code="numCurrentPhysicalBytes" /> | `string` | Output only. Number of physical bytes used by current live data storage. This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="numLongTermBytes" /> | `string` | Output only. The number of logical bytes in the table that are considered "long-term storage". |
| <CopyableCode code="numLongTermLogicalBytes" /> | `string` | Output only. Number of logical bytes that are more than 90 days old. |
| <CopyableCode code="numLongTermPhysicalBytes" /> | `string` | Output only. Number of physical bytes more than 90 days old. This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="numPartitions" /> | `string` | Output only. The number of partitions present in the table or materialized view. This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="numPhysicalBytes" /> | `string` | Output only. The physical size of this table in bytes. This includes storage used for time travel. |
| <CopyableCode code="numRows" /> | `string` | Output only. The number of rows of data in this table, excluding any data in the streaming buffer. |
| <CopyableCode code="numTimeTravelPhysicalBytes" /> | `string` | Output only. Number of physical bytes used by time travel storage (deleted or changed data). This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="numTotalLogicalBytes" /> | `string` | Output only. Total number of logical bytes in the table or materialized view. |
| <CopyableCode code="numTotalPhysicalBytes" /> | `string` | Output only. The physical size of this table in bytes. This also includes storage used for time travel. This data is not kept in real time, and might be delayed by a few seconds to a few minutes. |
| <CopyableCode code="partitionDefinition" /> | `object` | The partitioning information, which includes managed table, external table and metastore partitioned table partition information. |
| <CopyableCode code="rangePartitioning" /> | `object` |  |
| <CopyableCode code="replicas" /> | `array` | Optional. Output only. Table references of all replicas currently active on the table. |
| <CopyableCode code="requirePartitionFilter" /> | `boolean` | Optional. If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. |
| <CopyableCode code="resourceTags" /> | `object` | [Optional] The tags associated with this table. Tag keys are globally unique. See additional information on [tags](https://cloud.google.com/iam/docs/tags-access-control#definitions). An object containing a list of "key": value pairs. The key is the namespaced friendly name of the tag key, e.g. "12345/environment" where 12345 is parent id. The value is the friendly short name of the tag value, e.g. "production". |
| <CopyableCode code="restrictions" /> | `object` |  |
| <CopyableCode code="schema" /> | `object` | Schema of a table |
| <CopyableCode code="selfLink" /> | `string` | Output only. A URL that can be used to access this resource again. |
| <CopyableCode code="snapshotDefinition" /> | `object` | Information about base table and snapshot time of the snapshot. |
| <CopyableCode code="streamingBuffer" /> | `object` |  |
| <CopyableCode code="tableConstraints" /> | `object` | The TableConstraints defines the primary key and foreign key. |
| <CopyableCode code="tableReference" /> | `object` |  |
| <CopyableCode code="tableReplicationInfo" /> | `object` | Replication info of a table created using `AS REPLICA` DDL like: `CREATE MATERIALIZED VIEW mv1 AS REPLICA OF src_mv` |
| <CopyableCode code="timePartitioning" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Output only. Describes the table type. The following values are supported: * `TABLE`: A normal BigQuery table. * `VIEW`: A virtual table defined by a SQL query. * `EXTERNAL`: A table that references data stored in an external storage system, such as Google Cloud Storage. * `MATERIALIZED_VIEW`: A precomputed view defined by a SQL query. * `SNAPSHOT`: An immutable BigQuery table that preserves the contents of a base table at a particular time. See additional information on [table snapshots](/bigquery/docs/table-snapshots-intro). The default value is `TABLE`. |
| <CopyableCode code="view" /> | `object` | Describes the definition of a logical view. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="+datasetId, +tableId, projectId" /> | Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="+datasetId, projectId" /> | Lists all tables in the specified dataset. Requires the READER dataset role. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="+datasetId, projectId" /> | Creates a new, empty table in the dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="+datasetId, +tableId, projectId" /> | Deletes the table specified by tableId from the dataset. If the table contains data, all the data will be deleted. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="+datasetId, +tableId, projectId" /> | Updates information in an existing table. The update method replaces the entire table resource, whereas the patch method only replaces fields that are provided in the submitted table resource. This method supports RFC5789 patch semantics. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="+datasetId, +tableId, projectId" /> | Updates information in an existing table. The update method replaces the entire Table resource, whereas the patch method only replaces fields that are provided in the submitted Table resource. |

## `SELECT` examples

Lists all tables in the specified dataset. Requires the READER dataset role.

```sql
SELECT
id,
description,
biglakeConfiguration,
cloneDefinition,
clustering,
creationTime,
defaultCollation,
defaultRoundingMode,
encryptionConfiguration,
etag,
expirationTime,
externalCatalogTableOptions,
externalDataConfiguration,
friendlyName,
kind,
labels,
lastModifiedTime,
location,
materializedView,
materializedViewStatus,
maxStaleness,
model,
numActiveLogicalBytes,
numActivePhysicalBytes,
numBytes,
numCurrentPhysicalBytes,
numLongTermBytes,
numLongTermLogicalBytes,
numLongTermPhysicalBytes,
numPartitions,
numPhysicalBytes,
numRows,
numTimeTravelPhysicalBytes,
numTotalLogicalBytes,
numTotalPhysicalBytes,
partitionDefinition,
rangePartitioning,
replicas,
requirePartitionFilter,
resourceTags,
restrictions,
schema,
selfLink,
snapshotDefinition,
streamingBuffer,
tableConstraints,
tableReference,
tableReplicationInfo,
timePartitioning,
type,
view
FROM google.bigquery.tables
WHERE +datasetId = '{{ +datasetId }}'
AND projectId = '{{ projectId }}'; 
```
undefined
## `UPDATE` example

Updates a <code>tables</code> resource.

```sql
/*+ update */
UPDATE google.bigquery.tables
SET 
biglakeConfiguration = '{{ biglakeConfiguration }}',
clustering = '{{ clustering }}',
defaultCollation = '{{ defaultCollation }}',
defaultRoundingMode = '{{ defaultRoundingMode }}',
description = '{{ description }}',
encryptionConfiguration = '{{ encryptionConfiguration }}',
expirationTime = '{{ expirationTime }}',
externalCatalogTableOptions = '{{ externalCatalogTableOptions }}',
externalDataConfiguration = '{{ externalDataConfiguration }}',
friendlyName = '{{ friendlyName }}',
labels = '{{ labels }}',
materializedView = '{{ materializedView }}',
maxStaleness = '{{ maxStaleness }}',
model = '{{ model }}',
partitionDefinition = '{{ partitionDefinition }}',
rangePartitioning = '{{ rangePartitioning }}',
requirePartitionFilter = true|false,
resourceTags = '{{ resourceTags }}',
schema = '{{ schema }}',
tableConstraints = '{{ tableConstraints }}',
tableReference = '{{ tableReference }}',
tableReplicationInfo = '{{ tableReplicationInfo }}',
timePartitioning = '{{ timePartitioning }}',
view = '{{ view }}'
WHERE 
+datasetId = '{{ +datasetId }}'
AND +tableId = '{{ +tableId }}'
AND projectId = '{{ projectId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>tables</code> resource.

```sql
/*+ update */
REPLACE google.bigquery.tables
SET 
biglakeConfiguration = '{{ biglakeConfiguration }}',
clustering = '{{ clustering }}',
defaultCollation = '{{ defaultCollation }}',
defaultRoundingMode = '{{ defaultRoundingMode }}',
description = '{{ description }}',
encryptionConfiguration = '{{ encryptionConfiguration }}',
expirationTime = '{{ expirationTime }}',
externalCatalogTableOptions = '{{ externalCatalogTableOptions }}',
externalDataConfiguration = '{{ externalDataConfiguration }}',
friendlyName = '{{ friendlyName }}',
labels = '{{ labels }}',
materializedView = '{{ materializedView }}',
maxStaleness = '{{ maxStaleness }}',
model = '{{ model }}',
partitionDefinition = '{{ partitionDefinition }}',
rangePartitioning = '{{ rangePartitioning }}',
requirePartitionFilter = true|false,
resourceTags = '{{ resourceTags }}',
schema = '{{ schema }}',
tableConstraints = '{{ tableConstraints }}',
tableReference = '{{ tableReference }}',
tableReplicationInfo = '{{ tableReplicationInfo }}',
timePartitioning = '{{ timePartitioning }}',
view = '{{ view }}'
WHERE 
+datasetId = '{{ +datasetId }}'
AND +tableId = '{{ +tableId }}'
AND projectId = '{{ projectId }}';
```

## `DELETE` example

Deletes the specified <code>tables</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigquery.tables
WHERE +datasetId = '{{ +datasetId }}'
AND +tableId = '{{ +tableId }}'
AND projectId = '{{ projectId }}';
```

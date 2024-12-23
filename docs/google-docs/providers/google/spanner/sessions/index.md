---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
  - spanner
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

Creates, updates, deletes, gets or lists a <code>sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.spanner.sessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the session. This is always system-assigned. |
| <CopyableCode code="approximateLastUseTime" /> | `string` | Output only. The approximate timestamp when the session is last used. It is typically earlier than the actual last use time. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the session is created. |
| <CopyableCode code="creatorRole" /> | `string` | The database role which created this session. |
| <CopyableCode code="labels" /> | `object` | The labels for the session. * Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`. * Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`. * No more than 64 labels can be associated with a given session. See https://goo.gl/xmQnxf for more information on and examples of labels. |
| <CopyableCode code="multiplexed" /> | `boolean` | Optional. If true, specifies a multiplexed session. Use a multiplexed session for multiple, concurrent read-only operations. Don't use them for read-write transactions, partitioned reads, or partitioned queries. Use CreateSession to create multiplexed sessions. Don't use BatchCreateSessions to create a multiplexed session. You can't delete or list multiplexed sessions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_instances_databases_sessions_get" /> | `SELECT` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Gets a session. Returns `NOT_FOUND` if the session does not exist. This is mainly useful for determining whether a session is still alive. |
| <CopyableCode code="projects_instances_databases_sessions_list" /> | `SELECT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Lists all sessions in a given database. |
| <CopyableCode code="projects_instances_databases_sessions_batch_create" /> | `INSERT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Creates multiple new sessions. This API can be used to initialize a session cache on the clients. See https://goo.gl/TgSFN2 for best practices on session cache management. |
| <CopyableCode code="projects_instances_databases_sessions_create" /> | `INSERT` | <CopyableCode code="databasesId, instancesId, projectsId" /> | Creates a new session. A session can be used to perform transactions that read and/or modify data in a Cloud Spanner database. Sessions are meant to be reused for many consecutive transactions. Sessions can only execute one transaction at a time. To execute multiple concurrent read-write/write-only transactions, create multiple sessions. Note that standalone reads and queries use a transaction internally, and count toward the one transaction limit. Active sessions use additional server resources, so it is a good idea to delete idle and unneeded sessions. Aside from explicit deletes, Cloud Spanner may delete sessions for which no operations are sent for more than an hour. If a session is deleted, requests to it return `NOT_FOUND`. Idle sessions can be kept alive by sending a trivial SQL query periodically, e.g., `"SELECT 1"`. |
| <CopyableCode code="projects_instances_databases_sessions_delete" /> | `DELETE` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Ends a session, releasing server resources associated with it. This will asynchronously trigger cancellation of any operations that are running with this session. |
| <CopyableCode code="projects_instances_databases_sessions_batch_write" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Batches the supplied mutation groups in a collection of efficient transactions. All mutations in a group are committed atomically. However, mutations across groups can be committed non-atomically in an unspecified order and thus, they must be independent of each other. Partial failure is possible, i.e., some groups may have been committed successfully, while some may have failed. The results of individual batches are streamed into the response as the batches are applied. BatchWrite requests are not replay protected, meaning that each mutation group may be applied more than once. Replays of non-idempotent mutations may have undesirable effects. For example, replays of an insert mutation may produce an already exists error or if you use generated or commit timestamp-based keys, it may result in additional rows being added to the mutation's table. We recommend structuring your mutation groups to be idempotent to avoid this issue. |
| <CopyableCode code="projects_instances_databases_sessions_begin_transaction" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Begins a new transaction. This step can often be skipped: Read, ExecuteSql and Commit can begin a new transaction as a side-effect. |
| <CopyableCode code="projects_instances_databases_sessions_commit" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Commits a transaction. The request includes the mutations to be applied to rows in the database. `Commit` might return an `ABORTED` error. This can occur at any time; commonly, the cause is conflicts with concurrent transactions. However, it can also happen for a variety of other reasons. If `Commit` returns `ABORTED`, the caller should re-attempt the transaction from the beginning, re-using the same session. On very rare occasions, `Commit` might return `UNKNOWN`. This can happen, for example, if the client job experiences a 1+ hour networking failure. At that point, Cloud Spanner has lost track of the transaction outcome and we recommend that you perform another read from the database to see the state of things as they are now. |
| <CopyableCode code="projects_instances_databases_sessions_execute_batch_dml" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Executes a batch of SQL DML statements. This method allows many statements to be run with lower latency than submitting them sequentially with ExecuteSql. Statements are executed in sequential order. A request can succeed even if a statement fails. The ExecuteBatchDmlResponse.status field in the response provides information about the statement that failed. Clients must inspect this field to determine whether an error occurred. Execution stops after the first failed statement; the remaining statements are not executed. |
| <CopyableCode code="projects_instances_databases_sessions_execute_sql" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Executes an SQL statement, returning all results in a single reply. This method cannot be used to return a result set larger than 10 MiB; if the query yields more data than that, the query fails with a `FAILED_PRECONDITION` error. Operations inside read-write transactions might return `ABORTED`. If this occurs, the application should restart the transaction from the beginning. See Transaction for more details. Larger result sets can be fetched in streaming fashion by calling ExecuteStreamingSql instead. |
| <CopyableCode code="projects_instances_databases_sessions_execute_streaming_sql" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Like ExecuteSql, except returns the result set as a stream. Unlike ExecuteSql, there is no limit on the size of the returned result set. However, no individual row in the result set can exceed 100 MiB, and no column value can exceed 10 MiB. |
| <CopyableCode code="projects_instances_databases_sessions_partition_query" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Creates a set of partition tokens that can be used to execute a query operation in parallel. Each of the returned partition tokens can be used by ExecuteStreamingSql to specify a subset of the query result to read. The same session and read-only transaction must be used by the PartitionQueryRequest used to create the partition tokens and the ExecuteSqlRequests that use the partition tokens. Partition tokens become invalid when the session used to create them is deleted, is idle for too long, begins a new transaction, or becomes too old. When any of these happen, it is not possible to resume the query, and the whole operation must be restarted from the beginning. |
| <CopyableCode code="projects_instances_databases_sessions_partition_read" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Creates a set of partition tokens that can be used to execute a read operation in parallel. Each of the returned partition tokens can be used by StreamingRead to specify a subset of the read result to read. The same session and read-only transaction must be used by the PartitionReadRequest used to create the partition tokens and the ReadRequests that use the partition tokens. There are no ordering guarantees on rows returned among the returned partition tokens, or even within each individual StreamingRead call issued with a partition_token. Partition tokens become invalid when the session used to create them is deleted, is idle for too long, begins a new transaction, or becomes too old. When any of these happen, it is not possible to resume the read, and the whole operation must be restarted from the beginning. |
| <CopyableCode code="projects_instances_databases_sessions_read" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Reads rows from the database using key lookups and scans, as a simple key/value style alternative to ExecuteSql. This method cannot be used to return a result set larger than 10 MiB; if the read matches more data than that, the read fails with a `FAILED_PRECONDITION` error. Reads inside read-write transactions might return `ABORTED`. If this occurs, the application should restart the transaction from the beginning. See Transaction for more details. Larger result sets can be yielded in streaming fashion by calling StreamingRead instead. |
| <CopyableCode code="projects_instances_databases_sessions_rollback" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Rolls back a transaction, releasing any locks it holds. It is a good idea to call this for any transaction that includes one or more Read or ExecuteSql requests and ultimately decides not to commit. `Rollback` returns `OK` if it successfully aborts the transaction, the transaction was already aborted, or the transaction is not found. `Rollback` never returns `ABORTED`. |
| <CopyableCode code="projects_instances_databases_sessions_streaming_read" /> | `EXEC` | <CopyableCode code="databasesId, instancesId, projectsId, sessionsId" /> | Like Read, except returns the result set as a stream. Unlike Read, there is no limit on the size of the returned result set. However, no individual row in the result set can exceed 100 MiB, and no column value can exceed 10 MiB. |

## `SELECT` examples

Lists all sessions in a given database.

```sql
SELECT
name,
approximateLastUseTime,
createTime,
creatorRole,
labels,
multiplexed
FROM google.spanner.sessions
WHERE databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sessions</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.spanner.sessions (
databasesId,
instancesId,
projectsId,
sessionTemplate,
sessionCount
)
SELECT 
'{{ databasesId }}',
'{{ instancesId }}',
'{{ projectsId }}',
'{{ sessionTemplate }}',
'{{ sessionCount }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sessionTemplate
      value:
        - name: name
          value: string
        - name: labels
          value: object
        - name: createTime
          value: string
        - name: approximateLastUseTime
          value: string
        - name: creatorRole
          value: string
        - name: multiplexed
          value: boolean
    - name: sessionCount
      value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sessions</code> resource.

```sql
/*+ delete */
DELETE FROM google.spanner.sessions
WHERE databasesId = '{{ databasesId }}'
AND instancesId = '{{ instancesId }}'
AND projectsId = '{{ projectsId }}'
AND sessionsId = '{{ sessionsId }}';
```

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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.spanner.sessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the session. This is always system-assigned. |
| `labels` | `object` | The labels for the session. * Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`. * Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`. * No more than 64 labels can be associated with a given session. See https://goo.gl/xmQnxf for more information on and examples of labels. |
| `approximateLastUseTime` | `string` | Output only. The approximate timestamp when the session is last used. It is typically earlier than the actual last use time. |
| `createTime` | `string` | Output only. The timestamp when the session is created. |
| `creatorRole` | `string` | The database role which created this session. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_instances_databases_sessions_get` | `SELECT` | `databasesId, instancesId, projectsId, sessionsId` | Gets a session. Returns `NOT_FOUND` if the session does not exist. This is mainly useful for determining whether a session is still alive. |
| `projects_instances_databases_sessions_list` | `SELECT` | `databasesId, instancesId, projectsId` | Lists all sessions in a given database. |
| `projects_instances_databases_sessions_create` | `INSERT` | `databasesId, instancesId, projectsId` | Creates a new session. A session can be used to perform transactions that read and/or modify data in a Cloud Spanner database. Sessions are meant to be reused for many consecutive transactions. Sessions can only execute one transaction at a time. To execute multiple concurrent read-write/write-only transactions, create multiple sessions. Note that standalone reads and queries use a transaction internally, and count toward the one transaction limit. Active sessions use additional server resources, so it is a good idea to delete idle and unneeded sessions. Aside from explicit deletes, Cloud Spanner may delete sessions for which no operations are sent for more than an hour. If a session is deleted, requests to it return `NOT_FOUND`. Idle sessions can be kept alive by sending a trivial SQL query periodically, e.g., `"SELECT 1"`. |
| `projects_instances_databases_sessions_delete` | `DELETE` | `databasesId, instancesId, projectsId, sessionsId` | Ends a session, releasing server resources associated with it. This will asynchronously trigger cancellation of any operations that are running with this session. |
| `projects_instances_databases_sessions_beginTransaction` | `EXEC` | `databasesId, instancesId, projectsId, sessionsId` | Begins a new transaction. This step can often be skipped: Read, ExecuteSql and Commit can begin a new transaction as a side-effect. |
| `projects_instances_databases_sessions_commit` | `EXEC` | `databasesId, instancesId, projectsId, sessionsId` | Commits a transaction. The request includes the mutations to be applied to rows in the database. `Commit` might return an `ABORTED` error. This can occur at any time; commonly, the cause is conflicts with concurrent transactions. However, it can also happen for a variety of other reasons. If `Commit` returns `ABORTED`, the caller should re-attempt the transaction from the beginning, re-using the same session. On very rare occasions, `Commit` might return `UNKNOWN`. This can happen, for example, if the client job experiences a 1+ hour networking failure. At that point, Cloud Spanner has lost track of the transaction outcome and we recommend that you perform another read from the database to see the state of things as they are now. |
| `projects_instances_databases_sessions_executeBatchDml` | `EXEC` | `databasesId, instancesId, projectsId, sessionsId` | Executes a batch of SQL DML statements. This method allows many statements to be run with lower latency than submitting them sequentially with ExecuteSql. Statements are executed in sequential order. A request can succeed even if a statement fails. The ExecuteBatchDmlResponse.status field in the response provides information about the statement that failed. Clients must inspect this field to determine whether an error occurred. Execution stops after the first failed statement; the remaining statements are not executed. |
| `projects_instances_databases_sessions_executeSql` | `EXEC` | `databasesId, instancesId, projectsId, sessionsId` | Executes an SQL statement, returning all results in a single reply. This method cannot be used to return a result set larger than 10 MiB; if the query yields more data than that, the query fails with a `FAILED_PRECONDITION` error. Operations inside read-write transactions might return `ABORTED`. If this occurs, the application should restart the transaction from the beginning. See Transaction for more details. Larger result sets can be fetched in streaming fashion by calling ExecuteStreamingSql instead. |
| `projects_instances_databases_sessions_executeStreamingSql` | `EXEC` | `databasesId, instancesId, projectsId, sessionsId` | Like ExecuteSql, except returns the result set as a stream. Unlike ExecuteSql, there is no limit on the size of the returned result set. However, no individual row in the result set can exceed 100 MiB, and no column value can exceed 10 MiB. |
| `projects_instances_databases_sessions_partitionQuery` | `EXEC` | `databasesId, instancesId, projectsId, sessionsId` | Creates a set of partition tokens that can be used to execute a query operation in parallel. Each of the returned partition tokens can be used by ExecuteStreamingSql to specify a subset of the query result to read. The same session and read-only transaction must be used by the PartitionQueryRequest used to create the partition tokens and the ExecuteSqlRequests that use the partition tokens. Partition tokens become invalid when the session used to create them is deleted, is idle for too long, begins a new transaction, or becomes too old. When any of these happen, it is not possible to resume the query, and the whole operation must be restarted from the beginning. |
| `projects_instances_databases_sessions_partitionRead` | `EXEC` | `databasesId, instancesId, projectsId, sessionsId` | Creates a set of partition tokens that can be used to execute a read operation in parallel. Each of the returned partition tokens can be used by StreamingRead to specify a subset of the read result to read. The same session and read-only transaction must be used by the PartitionReadRequest used to create the partition tokens and the ReadRequests that use the partition tokens. There are no ordering guarantees on rows returned among the returned partition tokens, or even within each individual StreamingRead call issued with a partition_token. Partition tokens become invalid when the session used to create them is deleted, is idle for too long, begins a new transaction, or becomes too old. When any of these happen, it is not possible to resume the read, and the whole operation must be restarted from the beginning. |
| `projects_instances_databases_sessions_rollback` | `EXEC` | `databasesId, instancesId, projectsId, sessionsId` | Rolls back a transaction, releasing any locks it holds. It is a good idea to call this for any transaction that includes one or more Read or ExecuteSql requests and ultimately decides not to commit. `Rollback` returns `OK` if it successfully aborts the transaction, the transaction was already aborted, or the transaction is not found. `Rollback` never returns `ABORTED`. |
| `projects_instances_databases_sessions_streamingRead` | `EXEC` | `databasesId, instancesId, projectsId, sessionsId` | Like Read, except returns the result set as a stream. Unlike Read, there is no limit on the size of the returned result set. However, no individual row in the result set can exceed 100 MiB, and no column value can exceed 10 MiB. |

---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - sqladmin
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sqladmin.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | An identifier that uniquely identifies the operation. You can use this identifier to retrieve the Operations resource that has information about the operation. |
| `targetProject` | `string` | The project ID of the target instance related to this operation. |
| `importContext` | `object` | Database instance import context. |
| `insertTime` | `string` | The time this operation was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| `targetId` | `string` | Name of the database instance related to this operation. |
| `user` | `string` | The email address of the user who initiated this operation. |
| `status` | `string` | The status of an operation. |
| `endTime` | `string` | The time this operation finished in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| `operationType` | `string` | The type of the operation. Valid values are: * `CREATE` * `DELETE` * `UPDATE` * `RESTART` * `IMPORT` * `EXPORT` * `BACKUP_VOLUME` * `RESTORE_VOLUME` * `CREATE_USER` * `DELETE_USER` * `CREATE_DATABASE` * `DELETE_DATABASE` |
| `targetLink` | `string` |  |
| `exportContext` | `object` | Database instance export context. |
| `backupContext` | `object` | Backup context. |
| `kind` | `string` | This is always `sql#operation`. |
| `selfLink` | `string` | The URI of this resource. |
| `error` | `object` | Database instance operation errors list wrapper. |
| `startTime` | `string` | The time this operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `sql_operations_get` | `SELECT` | `operation, project` | Retrieves an instance operation that has been performed on an instance. |
| `sql_operations_list` | `SELECT` | `project` | Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time. |

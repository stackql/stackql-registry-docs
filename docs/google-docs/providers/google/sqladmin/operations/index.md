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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>operation</code> resource or lists <code>operations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | An identifier that uniquely identifies the operation. You can use this identifier to retrieve the Operations resource that has information about the operation. |
| <CopyableCode code="acquireSsrsLeaseContext" /> | `object` | Acquire SSRS lease context. |
| <CopyableCode code="apiWarning" /> | `object` | An Admin API warning message. |
| <CopyableCode code="backupContext" /> | `object` | Backup context. |
| <CopyableCode code="endTime" /> | `string` | The time this operation finished in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| <CopyableCode code="error" /> | `object` | Database instance operation errors list wrapper. |
| <CopyableCode code="exportContext" /> | `object` | Database instance export context. |
| <CopyableCode code="importContext" /> | `object` | Database instance import context. |
| <CopyableCode code="insertTime" /> | `string` | The time this operation was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| <CopyableCode code="kind" /> | `string` | This is always `sql#operation`. |
| <CopyableCode code="operationType" /> | `string` | The type of the operation. Valid values are: * `CREATE` * `DELETE` * `UPDATE` * `RESTART` * `IMPORT` * `EXPORT` * `BACKUP_VOLUME` * `RESTORE_VOLUME` * `CREATE_USER` * `DELETE_USER` * `CREATE_DATABASE` * `DELETE_DATABASE` |
| <CopyableCode code="selfLink" /> | `string` | The URI of this resource. |
| <CopyableCode code="startTime" /> | `string` | The time this operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| <CopyableCode code="status" /> | `string` | The status of an operation. |
| <CopyableCode code="targetId" /> | `string` | Name of the database instance related to this operation. |
| <CopyableCode code="targetLink" /> | `string` |  |
| <CopyableCode code="targetProject" /> | `string` | The project ID of the target instance related to this operation. |
| <CopyableCode code="user" /> | `string` | The email address of the user who initiated this operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operation, project" /> | Retrieves an instance operation that has been performed on an instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="operation, project" /> | Cancels an instance operation that has been performed on an instance. |

## `SELECT` examples

Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time.

```sql
SELECT
name,
acquireSsrsLeaseContext,
apiWarning,
backupContext,
endTime,
error,
exportContext,
importContext,
insertTime,
kind,
operationType,
selfLink,
startTime,
status,
targetId,
targetLink,
targetProject,
user
FROM google.sqladmin.operations
WHERE project = '{{ project }}'; 
```

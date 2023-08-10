---
title: backup_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_runs
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
<tr><td><b>Name</b></td><td><code>backup_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sqladmin.backup_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier for this backup run. Unique only for a specific Cloud SQL instance. |
| `description` | `string` | The description of this run, only applicable to on-demand backups. |
| `diskEncryptionConfiguration` | `object` | Disk encryption configuration for an instance. |
| `timeZone` | `string` | Backup time zone to prevent restores to an instance with a different time zone. Now relevant only for SQL Server. |
| `startTime` | `string` | The time the backup operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| `status` | `string` | The status of this run. |
| `backupKind` | `string` | Specifies the kind of backup, PHYSICAL or DEFAULT_SNAPSHOT. |
| `kind` | `string` | This is always `sql#backupRun`. |
| `instance` | `string` | Name of the database instance. |
| `selfLink` | `string` | The URI of this resource. |
| `diskEncryptionStatus` | `object` | Disk encryption status for an instance. |
| `windowStartTime` | `string` | The start time of the backup window during which this the backup was attempted in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| `error` | `object` | Database instance operation error. |
| `enqueuedTime` | `string` | The time the run was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| `location` | `string` | Location of the backups. |
| `endTime` | `string` | The time the backup operation completed in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
| `type` | `string` | The type of this run; can be either "AUTOMATED" or "ON_DEMAND" or "FINAL". This field defaults to "ON_DEMAND" and is ignored, when specified for insert requests. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, instance, project` | Retrieves a resource containing information about a backup run. |
| `list` | `SELECT` | `instance, project` | Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time. |
| `insert` | `INSERT` | `instance, project` | Creates a new backup run on demand. |
| `delete` | `DELETE` | `id, instance, project` | Deletes the backup taken by a backup run. |
| `_list` | `EXEC` | `instance, project` | Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time. |

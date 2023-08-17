---
title: backup_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_schedules
  - firestore
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
<tr><td><b>Name</b></td><td><code>backup_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firestore.backup_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The unique backup schedule identifier across all locations and databases for the given project. This will be auto-assigned. Format is `projects/&#123;project&#125;/databases/&#123;database&#125;/backupSchedules/&#123;backup_schedule&#125;` |
| `weeklyRecurrence` | `object` | Represents a recurring schedule that runs on a specified day of the week. The time zone is UTC. |
| `createTime` | `string` | Output only. The timestamp at which this backup schedule was created and effective since. No backups will be created for this schedule before this time. |
| `dailyRecurrence` | `object` | Represent a recurring schedule that runs at a specific time every day. The time zone is UTC. |
| `retention` | `string` | At what relative time in the future, compared to its creation time, the backup should be deleted, e.g. keep backups for 7 days. |
| `updateTime` | `string` | Output only. The timestamp at which this backup schedule was most recently updated. When a backup schedule is first created, this is the same as create_time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupSchedulesId, databasesId, projectsId` | Gets information about a backup schedule. |
| `list` | `SELECT` | `databasesId, projectsId` | List backup schedules. |
| `create` | `INSERT` | `databasesId, projectsId` | Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule with retention up to 7 days and one weekly backup schedule with retention up to 14 weeks. |
| `delete` | `DELETE` | `backupSchedulesId, databasesId, projectsId` | Deletes a backup schedule. |
| `patch` | `EXEC` | `backupSchedulesId, databasesId, projectsId` | Updates a backup schedule. |

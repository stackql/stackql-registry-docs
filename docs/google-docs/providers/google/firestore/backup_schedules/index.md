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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.firestore.backup_schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The unique backup schedule identifier across all locations and databases for the given project. This will be auto-assigned. Format is `projects/&#123;project&#125;/databases/&#123;database&#125;/backupSchedules/&#123;backup_schedule&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp at which this backup schedule was created and effective since. No backups will be created for this schedule before this time. |
| <CopyableCode code="dailyRecurrence" /> | `object` | Represents a recurring schedule that runs every day. The time zone is UTC. |
| <CopyableCode code="retention" /> | `string` | At what relative time in the future, compared to its creation time, the backup should be deleted, e.g. keep backups for 7 days. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp at which this backup schedule was most recently updated. When a backup schedule is first created, this is the same as create_time. |
| <CopyableCode code="weeklyRecurrence" /> | `object` | Represents a recurring schedule that runs on a specified day of the week. The time zone is UTC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupSchedulesId, databasesId, projectsId" /> | Gets information about a backup schedule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="databasesId, projectsId" /> | List backup schedules. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="databasesId, projectsId" /> | Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule and one weekly backup schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupSchedulesId, databasesId, projectsId" /> | Deletes a backup schedule. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="backupSchedulesId, databasesId, projectsId" /> | Updates a backup schedule. |

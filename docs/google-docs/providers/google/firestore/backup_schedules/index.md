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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupSchedulesId, databasesId, projectsId` | Gets information about a backup schedule. |
| `list` | `SELECT` | `databasesId, projectsId` | List backup schedules. |
| `create` | `INSERT` | `databasesId, projectsId` | Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule with retention up to 7 days and one weekly backup schedule with retention up to 14 weeks. |
| `delete` | `DELETE` | `backupSchedulesId, databasesId, projectsId` | Deletes a backup schedule. |
| `patch` | `EXEC` | `backupSchedulesId, databasesId, projectsId` | Updates a backup schedule. |

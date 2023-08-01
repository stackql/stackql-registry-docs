---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - gkebackup
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `backups` | `array` | The list of Backups matching the given criteria. |
| `nextPageToken` | `string` | A token which may be sent as page_token in a subsequent `ListBackups` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupPlansId, backupsId, locationsId, projectsId` | Retrieve the details of a single Backup. |
| `list` | `SELECT` | `backupPlansId, locationsId, projectsId` | Lists the Backups for a given BackupPlan. |
| `create` | `INSERT` | `backupPlansId, locationsId, projectsId` | Creates a Backup for the given BackupPlan. |
| `delete` | `DELETE` | `backupPlansId, backupsId, locationsId, projectsId` | Deletes an existing Backup. |
| `patch` | `EXEC` | `backupPlansId, backupsId, locationsId, projectsId` | Update a Backup. |

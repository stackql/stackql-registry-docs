---
title: volume_backups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_backups
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
<tr><td><b>Name</b></td><td><code>volume_backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.volume_backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token which may be sent as page_token in a subsequent `ListVolumeBackups` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. |
| `volumeBackups` | `array` | The list of VolumeBackups matching the given criteria. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupPlansId, backupsId, locationsId, projectsId, volumeBackupsId` | Retrieve the details of a single VolumeBackup. |
| `list` | `SELECT` | `backupPlansId, backupsId, locationsId, projectsId` | Lists the VolumeBackups for a given Backup. |

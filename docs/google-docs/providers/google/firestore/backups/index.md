---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firestore.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The unique resource name of the Backup. Format is `projects/&#123;project&#125;/locations/&#123;location&#125;/backups/&#123;backup&#125;`. |
| `stats` | `object` | Backup specific statistics. |
| `database` | `string` | Output only. Name of the Firestore database that the backup is from. Format is `projects/&#123;project&#125;/databases/&#123;database&#125;`. |
| `databaseUid` | `string` | Output only. The system-generated UUID4 for the Firestore database that the backup is from. |
| `expireTime` | `string` | Output only. The timestamp at which this backup expires. |
| `snapshotTime` | `string` | Output only. The backup contains an externally consistent copy of the database at this time. |
| `state` | `string` | Output only. The current state of the backup. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupsId, locationsId, projectsId` | Gets information about a backup. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the backups. |
| `delete` | `DELETE` | `backupsId, locationsId, projectsId` | Deletes a backup. |

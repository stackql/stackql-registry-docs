---
title: backup_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_plans
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
<tr><td><b>Name</b></td><td><code>backup_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.gkebackup.backup_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token which may be sent as page_token in a subsequent `ListBackupPlans` call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. |
| `unreachable` | `array` | Locations that could not be reached. |
| `backupPlans` | `array` | The list of BackupPlans matching the given criteria. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupPlansId, locationsId, projectsId` | Retrieve the details of a single BackupPlan. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists BackupPlans in a given location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new BackupPlan in a given location. |
| `delete` | `DELETE` | `backupPlansId, locationsId, projectsId` | Deletes an existing BackupPlan. |
| `patch` | `EXEC` | `backupPlansId, locationsId, projectsId` | Update a BackupPlan. |

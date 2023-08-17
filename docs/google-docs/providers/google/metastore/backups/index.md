---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - metastore
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
<tr><td><b>Id</b></td><td><code>google.metastore.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The relative resource name of the backup, in the following form:projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/services/&#123;service_id&#125;/backups/&#123;backup_id&#125; |
| `description` | `string` | The description of the backup. |
| `state` | `string` | Output only. The current state of the backup. |
| `createTime` | `string` | Output only. The time when the backup was started. |
| `endTime` | `string` | Output only. The time when the backup finished creating. |
| `restoringServices` | `array` | Output only. Services that are restoring from the backup. |
| `serviceRevision` | `object` | A managed metastore service that serves metadata queries. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupsId, locationsId, projectsId, servicesId` | Gets details of a single backup. |
| `list` | `SELECT` | `locationsId, projectsId, servicesId` | Lists backups in a service. |
| `create` | `INSERT` | `locationsId, projectsId, servicesId` | Creates a new backup in a given project and location. |
| `delete` | `DELETE` | `backupsId, locationsId, projectsId, servicesId` | Deletes a single backup. |
| `_list` | `EXEC` | `locationsId, projectsId, servicesId` | Lists backups in a service. |

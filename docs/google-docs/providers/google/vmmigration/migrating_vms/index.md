---
title: migrating_vms
hide_title: false
hide_table_of_contents: false
keywords:
  - migrating_vms
  - vmmigration
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
<tr><td><b>Name</b></td><td><code>migrating_vms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.vmmigration.migrating_vms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `migratingVms` | `array` | Output only. The list of Migrating VMs response. |
| `nextPageToken` | `string` | Output only. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `unreachable` | `array` | Output only. Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Gets details of a single MigratingVm. |
| `list` | `SELECT` | `locationsId, projectsId, sourcesId` | Lists MigratingVms in a given Source. |
| `create` | `INSERT` | `locationsId, projectsId, sourcesId` | Creates a new MigratingVm in a given Source. |
| `delete` | `DELETE` | `locationsId, migratingVmsId, projectsId, sourcesId` | Deletes a single MigratingVm. |
| `finalize_migration` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Marks a migration as completed, deleting migration resources that are no longer being used. Only applicable after cutover is done. |
| `patch` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Updates the parameters of a single MigratingVm. |
| `pause_migration` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Pauses a migration for a VM. If cycle tasks are running they will be cancelled, preserving source task data. Further replication cycles will not be triggered while the VM is paused. |
| `resume_migration` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Resumes a migration for a VM. When called on a paused migration, will start the process of uploading data and creating snapshots; when called on a completed cut-over migration, will update the migration to active state and start the process of uploading data and creating snapshots. |
| `start_migration` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Starts migration for a VM. Starts the process of uploading data and creating snapshots, in replication cycles scheduled by the policy. |

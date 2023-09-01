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
| `name` | `string` | Output only. The identifier of the MigratingVm. |
| `description` | `string` | The description attached to the migrating VM by the user. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `computeEngineTargetDefaults` | `object` | ComputeEngineTargetDefaults is a collection of details for creating a VM in a target Compute Engine project. |
| `state` | `string` | Output only. State of the MigratingVm. |
| `group` | `string` | Output only. The group this migrating vm is included in, if any. The group is represented by the full path of the appropriate Group resource. |
| `vmwareSourceVmDetails` | `object` | Represent the source Vmware VM details. |
| `labels` | `object` | The labels of the migrating VM. |
| `stateTime` | `string` | Output only. The last time the migrating VM state was updated. |
| `computeEngineDisksTargetDefaults` | `object` | ComputeEngineDisksTargetDefaults is a collection of details for creating Persistent Disks in a target Compute Engine project. |
| `recentCutoverJobs` | `array` | Output only. The recent cutover jobs performed on the migrating VM. This field holds the vm's last completed cutover job and the vm's running cutover job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request. |
| `cutoverForecast` | `object` | CutoverForecast holds information about future CutoverJobs of a MigratingVm. |
| `policy` | `object` | A policy for scheduling replications. |
| `awsSourceVmDetails` | `object` | Represent the source AWS VM details. |
| `lastReplicationCycle` | `object` | ReplicationCycle contains information about the current replication cycle status. |
| `updateTime` | `string` | Output only. The last time the migrating VM resource was updated. |
| `lastSync` | `object` | ReplicationSync contain information about the last replica sync to the cloud. |
| `currentSyncInfo` | `object` | ReplicationCycle contains information about the current replication cycle status. |
| `recentCloneJobs` | `array` | Output only. The recent clone jobs performed on the migrating VM. This field holds the vm's last completed clone job and the vm's running clone job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request. |
| `createTime` | `string` | Output only. The time the migrating VM was created (this refers to this resource and not to the time it was installed in the source). |
| `displayName` | `string` | The display name attached to the MigratingVm by the user. |
| `sourceVmId` | `string` | The unique ID of the VM in the source. The VM's name in vSphere can be changed, so this is not the VM's name but rather its moRef id. This id is of the form vm-. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, migratingVmsId, projectsId, sourcesId` | Gets details of a single MigratingVm. |
| `list` | `SELECT` | `locationsId, projectsId, sourcesId` | Lists MigratingVms in a given Source. |
| `create` | `INSERT` | `locationsId, projectsId, sourcesId` | Creates a new MigratingVm in a given Source. |
| `delete` | `DELETE` | `locationsId, migratingVmsId, projectsId, sourcesId` | Deletes a single MigratingVm. |
| `_list` | `EXEC` | `locationsId, projectsId, sourcesId` | Lists MigratingVms in a given Source. |
| `finalize_migration` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Marks a migration as completed, deleting migration resources that are no longer being used. Only applicable after cutover is done. |
| `patch` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Updates the parameters of a single MigratingVm. |
| `pause_migration` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Pauses a migration for a VM. If cycle tasks are running they will be cancelled, preserving source task data. Further replication cycles will not be triggered while the VM is paused. |
| `resume_migration` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Resumes a migration for a VM. When called on a paused migration, will start the process of uploading data and creating snapshots; when called on a completed cut-over migration, will update the migration to active state and start the process of uploading data and creating snapshots. |
| `start_migration` | `EXEC` | `locationsId, migratingVmsId, projectsId, sourcesId` | Starts migration for a VM. Starts the process of uploading data and creating snapshots, in replication cycles scheduled by the policy. |

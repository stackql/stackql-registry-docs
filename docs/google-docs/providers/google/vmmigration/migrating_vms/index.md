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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>migrating_vms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migrating_vms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.migrating_vms" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The identifier of the MigratingVm. |
| <CopyableCode code="description" /> | `string` | The description attached to the migrating VM by the user. |
| <CopyableCode code="awsSourceVmDetails" /> | `object` | Represent the source AWS VM details. |
| <CopyableCode code="azureSourceVmDetails" /> | `object` | Represent the source Azure VM details. |
| <CopyableCode code="computeEngineDisksTargetDefaults" /> | `object` | ComputeEngineDisksTargetDefaults is a collection of details for creating Persistent Disks in a target Compute Engine project. |
| <CopyableCode code="computeEngineTargetDefaults" /> | `object` | ComputeEngineTargetDefaults is a collection of details for creating a VM in a target Compute Engine project. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the migrating VM was created (this refers to this resource and not to the time it was installed in the source). |
| <CopyableCode code="currentSyncInfo" /> | `object` | ReplicationCycle contains information about the current replication cycle status. |
| <CopyableCode code="cutoverForecast" /> | `object` | CutoverForecast holds information about future CutoverJobs of a MigratingVm. |
| <CopyableCode code="displayName" /> | `string` | The display name attached to the MigratingVm by the user. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="group" /> | `string` | Output only. The group this migrating vm is included in, if any. The group is represented by the full path of the appropriate Group resource. |
| <CopyableCode code="labels" /> | `object` | The labels of the migrating VM. |
| <CopyableCode code="lastReplicationCycle" /> | `object` | ReplicationCycle contains information about the current replication cycle status. |
| <CopyableCode code="lastSync" /> | `object` | ReplicationSync contain information about the last replica sync to the cloud. |
| <CopyableCode code="policy" /> | `object` | A policy for scheduling replications. |
| <CopyableCode code="recentCloneJobs" /> | `array` | Output only. The recent clone jobs performed on the migrating VM. This field holds the vm's last completed clone job and the vm's running clone job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request. |
| <CopyableCode code="recentCutoverJobs" /> | `array` | Output only. The recent cutover jobs performed on the migrating VM. This field holds the vm's last completed cutover job and the vm's running cutover job, if one exists. Note: To have this field populated you need to explicitly request it via the "view" parameter of the Get/List request. |
| <CopyableCode code="sourceVmId" /> | `string` | The unique ID of the VM in the source. The VM's name in vSphere can be changed, so this is not the VM's name but rather its moRef id. This id is of the form vm-. |
| <CopyableCode code="state" /> | `string` | Output only. State of the MigratingVm. |
| <CopyableCode code="stateTime" /> | `string` | Output only. The last time the migrating VM state was updated. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last time the migrating VM resource was updated. |
| <CopyableCode code="vmwareSourceVmDetails" /> | `object` | Represent the source Vmware VM details. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Gets details of a single MigratingVm. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Lists MigratingVms in a given Source. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, sourcesId" /> | Creates a new MigratingVm in a given Source. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Deletes a single MigratingVm. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Updates the parameters of a single MigratingVm. |
| <CopyableCode code="finalize_migration" /> | `EXEC` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Marks a migration as completed, deleting migration resources that are no longer being used. Only applicable after cutover is done. |
| <CopyableCode code="pause_migration" /> | `EXEC` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Pauses a migration for a VM. If cycle tasks are running they will be cancelled, preserving source task data. Further replication cycles will not be triggered while the VM is paused. |
| <CopyableCode code="resume_migration" /> | `EXEC` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Resumes a migration for a VM. When called on a paused migration, will start the process of uploading data and creating snapshots; when called on a completed cut-over migration, will update the migration to active state and start the process of uploading data and creating snapshots. |
| <CopyableCode code="start_migration" /> | `EXEC` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Starts migration for a VM. Starts the process of uploading data and creating snapshots, in replication cycles scheduled by the policy. |

## `SELECT` examples

Lists MigratingVms in a given Source.

```sql
SELECT
name,
description,
awsSourceVmDetails,
azureSourceVmDetails,
computeEngineDisksTargetDefaults,
computeEngineTargetDefaults,
createTime,
currentSyncInfo,
cutoverForecast,
displayName,
error,
group,
labels,
lastReplicationCycle,
lastSync,
policy,
recentCloneJobs,
recentCutoverJobs,
sourceVmId,
state,
stateTime,
updateTime,
vmwareSourceVmDetails
FROM google.vmmigration.migrating_vms
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>migrating_vms</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.vmmigration.migrating_vms (
locationsId,
projectsId,
sourcesId,
computeEngineTargetDefaults,
computeEngineDisksTargetDefaults,
sourceVmId,
displayName,
description,
policy,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ sourcesId }}',
'{{ computeEngineTargetDefaults }}',
'{{ computeEngineDisksTargetDefaults }}',
'{{ sourceVmId }}',
'{{ displayName }}',
'{{ description }}',
'{{ policy }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: computeEngineTargetDefaults
      value:
        - name: vmName
          value: string
        - name: targetProject
          value: string
        - name: zone
          value: string
        - name: machineTypeSeries
          value: string
        - name: machineType
          value: string
        - name: networkTags
          value:
            - string
        - name: networkInterfaces
          value:
            - - name: network
                value: string
              - name: subnetwork
                value: string
              - name: internalIp
                value: string
              - name: externalIp
                value: string
              - name: networkTier
                value: string
        - name: serviceAccount
          value: string
        - name: diskType
          value: string
        - name: labels
          value: object
        - name: licenseType
          value: string
        - name: appliedLicense
          value:
            - name: type
              value: string
            - name: osLicense
              value: string
        - name: computeScheduling
          value:
            - name: onHostMaintenance
              value: string
            - name: restartType
              value: string
            - name: nodeAffinities
              value:
                - - name: key
                    value: string
                  - name: operator
                    value: string
                  - name: values
                    value:
                      - string
            - name: minNodeCpus
              value: integer
        - name: secureBoot
          value: boolean
        - name: enableVtpm
          value: boolean
        - name: enableIntegrityMonitoring
          value: boolean
        - name: bootOption
          value: string
        - name: metadata
          value: object
        - name: additionalLicenses
          value:
            - string
        - name: hostname
          value: string
        - name: encryption
          value:
            - name: kmsKey
              value: string
        - name: bootConversion
          value: string
    - name: computeEngineDisksTargetDefaults
      value:
        - name: zone
          value: string
        - name: disksTargetDefaults
          value: []
        - name: vmTargetDefaults
          value:
            - name: vmName
              value: string
            - name: machineTypeSeries
              value: string
            - name: machineType
              value: string
            - name: networkTags
              value:
                - string
            - name: networkInterfaces
              value:
                - - name: network
                    value: string
                  - name: subnetwork
                    value: string
                  - name: internalIp
                    value: string
                  - name: externalIp
                    value: string
                  - name: networkTier
                    value: string
            - name: serviceAccount
              value: string
            - name: secureBoot
              value: boolean
            - name: enableVtpm
              value: boolean
            - name: enableIntegrityMonitoring
              value: boolean
            - name: metadata
              value: object
            - name: additionalLicenses
              value:
                - string
            - name: hostname
              value: string
            - name: labels
              value: object
            - name: bootDiskDefaults
              value:
                - name: image
                  value:
                    - name: sourceImage
                      value: string
                - name: diskName
                  value: string
                - name: diskType
                  value: string
                - name: deviceName
                  value: string
        - name: targetProject
          value: string
        - name: disks
          value:
            - - name: sourceDiskNumber
                value: integer
              - name: diskName
                value: string
              - name: diskType
                value: string
              - name: additionalLabels
                value: object
              - name: vmAttachmentDetails
                value:
                  - name: deviceName
                    value: string
    - name: vmwareSourceVmDetails
      value:
        - name: firmware
          value: string
        - name: committedStorageBytes
          value: string
        - name: disks
          value:
            - - name: diskNumber
                value: integer
              - name: sizeGb
                value: string
              - name: label
                value: string
        - name: vmCapabilitiesInfo
          value:
            - name: osCapabilities
              value:
                - string
            - name: lastOsCapabilitiesUpdateTime
              value: string
    - name: awsSourceVmDetails
      value:
        - name: firmware
          value: string
        - name: committedStorageBytes
          value: string
        - name: disks
          value:
            - - name: diskNumber
                value: integer
              - name: volumeId
                value: string
              - name: sizeGb
                value: string
    - name: azureSourceVmDetails
      value:
        - name: firmware
          value: string
        - name: committedStorageBytes
          value: string
        - name: disks
          value:
            - - name: diskNumber
                value: integer
              - name: diskId
                value: string
              - name: sizeGb
                value: string
    - name: name
      value: string
    - name: sourceVmId
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: policy
      value:
        - name: idleDuration
          value: string
        - name: skipOsAdaptation
          value: boolean
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: lastSync
      value:
        - name: lastSyncTime
          value: string
    - name: state
      value: string
    - name: stateTime
      value: string
    - name: currentSyncInfo
      value:
        - name: name
          value: string
        - name: cycleNumber
          value: integer
        - name: startTime
          value: string
        - name: endTime
          value: string
        - name: totalPauseDuration
          value: string
        - name: progressPercent
          value: integer
        - name: steps
          value:
            - - name: initializingReplication
                value: []
              - name: replicating
                value:
                  - name: totalBytes
                    value: string
                  - name: replicatedBytes
                    value: string
                  - name: lastTwoMinutesAverageBytesPerSecond
                    value: string
                  - name: lastThirtyMinutesAverageBytesPerSecond
                    value: string
              - name: postProcessing
                value: []
              - name: startTime
                value: string
              - name: endTime
                value: string
        - name: state
          value: string
        - name: error
          value:
            - name: code
              value: integer
            - name: message
              value: string
            - name: details
              value:
                - object
        - name: warnings
          value:
            - - name: code
                value: string
              - name: warningMessage
                value:
                  - name: locale
                    value: string
                  - name: message
                    value: string
              - name: helpLinks
                value:
                  - - name: description
                      value: string
                    - name: url
                      value: string
              - name: warningTime
                value: string
    - name: group
      value: string
    - name: labels
      value: object
    - name: recentCloneJobs
      value:
        - - name: computeEngineTargetDetails
            value:
              - name: vmName
                value: string
              - name: project
                value: string
              - name: zone
                value: string
              - name: machineTypeSeries
                value: string
              - name: machineType
                value: string
              - name: networkTags
                value:
                  - string
              - name: networkInterfaces
                value:
                  - - name: network
                      value: string
                    - name: subnetwork
                      value: string
                    - name: internalIp
                      value: string
                    - name: externalIp
                      value: string
                    - name: networkTier
                      value: string
              - name: serviceAccount
                value: string
              - name: diskType
                value: string
              - name: labels
                value: object
              - name: licenseType
                value: string
              - name: secureBoot
                value: boolean
              - name: enableVtpm
                value: boolean
              - name: enableIntegrityMonitoring
                value: boolean
              - name: bootOption
                value: string
              - name: metadata
                value: object
              - name: additionalLicenses
                value:
                  - string
              - name: hostname
                value: string
              - name: bootConversion
                value: string
          - name: computeEngineDisksTargetDetails
            value:
              - name: disksTargetDetails
                value: []
              - name: vmTargetDetails
                value:
                  - name: vmUri
                    value: string
              - name: disks
                value:
                  - - name: sourceDiskNumber
                      value: integer
                    - name: diskUri
                      value: string
          - name: createTime
            value: string
          - name: endTime
            value: string
          - name: name
            value: string
          - name: state
            value: string
          - name: stateTime
            value: string
          - name: steps
            value:
              - - name: adaptingOs
                  value: []
                - name: preparingVmDisks
                  value: []
                - name: instantiatingMigratedVm
                  value: []
                - name: startTime
                  value: string
                - name: endTime
                  value: string
    - name: recentCutoverJobs
      value:
        - - name: createTime
            value: string
          - name: endTime
            value: string
          - name: name
            value: string
          - name: state
            value: string
          - name: stateTime
            value: string
          - name: progressPercent
            value: integer
          - name: stateMessage
            value: string
          - name: steps
            value:
              - - name: shuttingDownSourceVm
                  value: []
                - name: startTime
                  value: string
                - name: endTime
                  value: string
    - name: cutoverForecast
      value:
        - name: estimatedCutoverJobDuration
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>migrating_vms</code> resource.

```sql
/*+ update */
UPDATE google.vmmigration.migrating_vms
SET 
computeEngineTargetDefaults = '{{ computeEngineTargetDefaults }}',
computeEngineDisksTargetDefaults = '{{ computeEngineDisksTargetDefaults }}',
sourceVmId = '{{ sourceVmId }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
policy = '{{ policy }}',
labels = '{{ labels }}'
WHERE 
locationsId = '{{ locationsId }}'
AND migratingVmsId = '{{ migratingVmsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}';
```

## `DELETE` example

Deletes the specified <code>migrating_vms</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmmigration.migrating_vms
WHERE locationsId = '{{ locationsId }}'
AND migratingVmsId = '{{ migratingVmsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}';
```

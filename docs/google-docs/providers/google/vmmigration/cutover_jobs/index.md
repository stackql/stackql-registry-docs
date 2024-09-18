---
title: cutover_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - cutover_jobs
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

Creates, updates, deletes, gets or lists a <code>cutover_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cutover_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.cutover_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the cutover job. |
| <CopyableCode code="computeEngineDisksTargetDetails" /> | `object` | ComputeEngineDisksTargetDetails is a collection of created Persistent Disks details. |
| <CopyableCode code="computeEngineTargetDetails" /> | `object` | ComputeEngineTargetDetails is a collection of details for creating a VM in a target Compute Engine project. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the cutover job was created (as an API call, not when it was actually created in the target). |
| <CopyableCode code="endTime" /> | `string` | Output only. The time the cutover job had finished. |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="progressPercent" /> | `integer` | Output only. The current progress in percentage of the cutover job. |
| <CopyableCode code="state" /> | `string` | Output only. State of the cutover job. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. A message providing possible extra details about the current state. |
| <CopyableCode code="stateTime" /> | `string` | Output only. The time the state was last updated. |
| <CopyableCode code="steps" /> | `array` | Output only. The cutover steps list representing its progress. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cutoverJobsId, locationsId, migratingVmsId, projectsId, sourcesId" /> | Gets details of a single CutoverJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Lists the CutoverJobs of a migrating VM. Only 25 most recent CutoverJobs are listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, migratingVmsId, projectsId, sourcesId" /> | Initiates a Cutover of a specific migrating VM. The returned LRO is completed when the cutover job resource is created and the job is initiated. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="cutoverJobsId, locationsId, migratingVmsId, projectsId, sourcesId" /> | Initiates the cancellation of a running cutover job. |

## `SELECT` examples

Lists the CutoverJobs of a migrating VM. Only 25 most recent CutoverJobs are listed.

```sql
SELECT
name,
computeEngineDisksTargetDetails,
computeEngineTargetDetails,
createTime,
endTime,
error,
progressPercent,
state,
stateMessage,
stateTime,
steps
FROM google.vmmigration.cutover_jobs
WHERE locationsId = '{{ locationsId }}'
AND migratingVmsId = '{{ migratingVmsId }}'
AND projectsId = '{{ projectsId }}'
AND sourcesId = '{{ sourcesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cutover_jobs</code> resource.

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
INSERT INTO google.vmmigration.cutover_jobs (
locationsId,
migratingVmsId,
projectsId,
sourcesId
)
SELECT 
'{{ locationsId }}',
'{{ migratingVmsId }}',
'{{ projectsId }}',
'{{ sourcesId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
computeEngineTargetDetails:
  vmName: string
  project: string
  zone: string
  machineTypeSeries: string
  machineType: string
  networkTags:
    - type: string
  networkInterfaces:
    - network: string
      subnetwork: string
      internalIp: string
      externalIp: string
      networkTier: string
  serviceAccount: string
  diskType: string
  labels: object
  licenseType: string
  appliedLicense:
    type: string
    osLicense: string
  computeScheduling:
    onHostMaintenance: string
    restartType: string
    nodeAffinities:
      - key: string
        operator: string
        values:
          - type: string
    minNodeCpus: integer
  secureBoot: boolean
  enableVtpm: boolean
  enableIntegrityMonitoring: boolean
  bootOption: string
  metadata: object
  additionalLicenses:
    - type: string
  hostname: string
  encryption:
    kmsKey: string
  bootConversion: string
computeEngineDisksTargetDetails:
  disksTargetDetails: {}
  vmTargetDetails:
    vmUri: string
  disks:
    - sourceDiskNumber: integer
      diskUri: string
createTime: string
endTime: string
name: string
state: string
stateTime: string
progressPercent: integer
error:
  code: integer
  message: string
  details:
    - type: string
      additionalProperties: any
stateMessage: string
steps:
  - previousReplicationCycle:
      name: string
      cycleNumber: integer
      startTime: string
      endTime: string
      totalPauseDuration: string
      progressPercent: integer
      steps:
        - initializingReplication: {}
          replicating:
            totalBytes: string
            replicatedBytes: string
            lastTwoMinutesAverageBytesPerSecond: string
            lastThirtyMinutesAverageBytesPerSecond: string
          postProcessing: {}
          startTime: string
          endTime: string
      state: string
      warnings:
        - code: string
          warningMessage:
            locale: string
            message: string
          helpLinks:
            - description: string
              url: string
          warningTime: string
    shuttingDownSourceVm: {}
    preparingVmDisks: {}
    instantiatingMigratedVm: {}
    startTime: string
    endTime: string

```
</TabItem>
</Tabs>

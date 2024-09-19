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
- name: your_resource_model_name
  props:
    - name: computeEngineTargetDetails
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
    - name: progressPercent
      value: integer
    - name: error
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: stateMessage
      value: string
    - name: steps
      value:
        - - name: previousReplicationCycle
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
          - name: shuttingDownSourceVm
            value: []
          - name: preparingVmDisks
            value: []
          - name: instantiatingMigratedVm
            value: []
          - name: startTime
            value: string
          - name: endTime
            value: string

```
</TabItem>
</Tabs>

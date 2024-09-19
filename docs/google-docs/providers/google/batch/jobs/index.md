---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - batch
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

Creates, updates, deletes, gets or lists a <code>jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.batch.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Job name. For example: "projects/123456/locations/us-central1/jobs/job01". |
| <CopyableCode code="allocationPolicy" /> | `object` | A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job. |
| <CopyableCode code="createTime" /> | `string` | Output only. When the Job was created. |
| <CopyableCode code="labels" /> | `object` | Labels for the Job. Labels could be user provided or system generated. For example, "labels": { "department": "finance", "environment": "test" } You can assign up to 64 labels. [Google Compute Engine label restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) apply. Label names that start with "goog-" or "google-" are reserved. |
| <CopyableCode code="logsPolicy" /> | `object` | LogsPolicy describes how outputs from a Job's Tasks (stdout/stderr) will be preserved. |
| <CopyableCode code="notifications" /> | `array` | Notification configurations. |
| <CopyableCode code="priority" /> | `string` | Priority of the Job. The valid value range is [0, 100). Default value is 0. Higher value indicates higher priority. A job with higher priority value is more likely to run earlier if all other requirements are satisfied. |
| <CopyableCode code="status" /> | `object` | Job status. |
| <CopyableCode code="taskGroups" /> | `array` | Required. TaskGroups in the Job. Only one TaskGroup is supported now. |
| <CopyableCode code="uid" /> | `string` | Output only. A system generated unique ID for the Job. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last time the Job was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Get a Job specified by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List all Jobs for a project within a region. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a Job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Delete a Job. |

## `SELECT` examples

List all Jobs for a project within a region.

```sql
SELECT
name,
allocationPolicy,
createTime,
labels,
logsPolicy,
notifications,
priority,
status,
taskGroups,
uid,
updateTime
FROM google.batch.jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>jobs</code> resource.

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
INSERT INTO google.batch.jobs (
locationsId,
projectsId,
priority,
taskGroups,
allocationPolicy,
labels,
logsPolicy,
notifications
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ priority }}',
'{{ taskGroups }}',
'{{ allocationPolicy }}',
'{{ labels }}',
'{{ logsPolicy }}',
'{{ notifications }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: uid
      value: string
    - name: priority
      value: string
    - name: taskGroups
      value:
        - - name: name
            value: string
          - name: taskSpec
            value:
              - name: runnables
                value:
                  - - name: container
                      value:
                        - name: imageUri
                          value: string
                        - name: commands
                          value:
                            - string
                        - name: entrypoint
                          value: string
                        - name: volumes
                          value:
                            - string
                        - name: options
                          value: string
                        - name: blockExternalNetwork
                          value: boolean
                        - name: username
                          value: string
                        - name: password
                          value: string
                        - name: enableImageStreaming
                          value: boolean
                    - name: script
                      value:
                        - name: path
                          value: string
                        - name: text
                          value: string
                    - name: barrier
                      value:
                        - name: name
                          value: string
                    - name: displayName
                      value: string
                    - name: ignoreExitStatus
                      value: boolean
                    - name: background
                      value: boolean
                    - name: alwaysRun
                      value: boolean
                    - name: environment
                      value:
                        - name: variables
                          value: object
                        - name: secretVariables
                          value: object
                        - name: encryptedVariables
                          value:
                            - name: keyName
                              value: string
                            - name: cipherText
                              value: string
                    - name: timeout
                      value: string
                    - name: labels
                      value: object
              - name: computeResource
                value:
                  - name: cpuMilli
                    value: string
                  - name: memoryMib
                    value: string
                  - name: bootDiskMib
                    value: string
              - name: maxRunDuration
                value: string
              - name: maxRetryCount
                value: integer
              - name: lifecyclePolicies
                value:
                  - - name: action
                      value: string
                    - name: actionCondition
                      value:
                        - name: exitCodes
                          value:
                            - integer
              - name: environments
                value: object
              - name: volumes
                value:
                  - - name: nfs
                      value:
                        - name: server
                          value: string
                        - name: remotePath
                          value: string
                    - name: gcs
                      value:
                        - name: remotePath
                          value: string
                    - name: deviceName
                      value: string
                    - name: mountPath
                      value: string
                    - name: mountOptions
                      value:
                        - string
          - name: taskCount
            value: string
          - name: parallelism
            value: string
          - name: schedulingPolicy
            value: string
          - name: taskEnvironments
            value:
              - - name: variables
                  value: object
                - name: secretVariables
                  value: object
          - name: taskCountPerNode
            value: string
          - name: requireHostsFile
            value: boolean
          - name: permissiveSsh
            value: boolean
          - name: runAsNonRoot
            value: boolean
    - name: allocationPolicy
      value:
        - name: location
          value:
            - name: allowedLocations
              value:
                - string
        - name: instances
          value:
            - - name: policy
                value:
                  - name: machineType
                    value: string
                  - name: minCpuPlatform
                    value: string
                  - name: provisioningModel
                    value: string
                  - name: accelerators
                    value:
                      - - name: type
                          value: string
                        - name: count
                          value: string
                        - name: installGpuDrivers
                          value: boolean
                        - name: driverVersion
                          value: string
                  - name: bootDisk
                    value:
                      - name: image
                        value: string
                      - name: snapshot
                        value: string
                      - name: type
                        value: string
                      - name: sizeGb
                        value: string
                      - name: diskInterface
                        value: string
                  - name: disks
                    value:
                      - - name: existingDisk
                          value: string
                        - name: deviceName
                          value: string
                  - name: reservation
                    value: string
              - name: instanceTemplate
                value: string
              - name: installGpuDrivers
                value: boolean
              - name: installOpsAgent
                value: boolean
              - name: blockProjectSshKeys
                value: boolean
        - name: serviceAccount
          value:
            - name: email
              value: string
            - name: scopes
              value:
                - string
        - name: labels
          value: object
        - name: network
          value:
            - name: networkInterfaces
              value:
                - - name: network
                    value: string
                  - name: subnetwork
                    value: string
                  - name: noExternalIpAddress
                    value: boolean
        - name: placement
          value:
            - name: collocation
              value: string
            - name: maxDistance
              value: string
        - name: tags
          value:
            - string
    - name: labels
      value: object
    - name: status
      value:
        - name: state
          value: string
        - name: statusEvents
          value:
            - - name: type
                value: string
              - name: description
                value: string
              - name: eventTime
                value: string
              - name: taskExecution
                value:
                  - name: exitCode
                    value: integer
              - name: taskState
                value: string
        - name: taskGroups
          value: object
        - name: runDuration
          value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: logsPolicy
      value:
        - name: destination
          value: string
        - name: logsPath
          value: string
        - name: cloudLoggingOption
          value:
            - name: useGenericTaskMonitoredResource
              value: boolean
    - name: notifications
      value:
        - - name: pubsubTopic
            value: string
          - name: message
            value:
              - name: type
                value: string
              - name: newJobState
                value: string
              - name: newTaskState
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.batch.jobs
WHERE jobsId = '{{ jobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

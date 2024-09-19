---
title: patch_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - patch_deployments
  - osconfig
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

Creates, updates, deletes, gets or lists a <code>patch_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.osconfig.patch_deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Unique name for the patch deployment resource in a project. The patch deployment name is in the form: `projects/{project_id}/patchDeployments/{patch_deployment_id}`. This field is ignored when you create a new patch deployment. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the patch deployment. Length of the description is limited to 1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time the patch deployment was created. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="duration" /> | `string` | Optional. Duration of the patch. After the duration ends, the patch times out. |
| <CopyableCode code="instanceFilter" /> | `object` | A filter to target VM instances for patching. The targeted VMs must meet all criteria specified. So if both labels and zones are specified, the patch job targets only VMs with those labels and in those zones. |
| <CopyableCode code="lastExecuteTime" /> | `string` | Output only. The last time a patch job was started by this deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="oneTimeSchedule" /> | `object` | Sets the time for a one time patch deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |
| <CopyableCode code="patchConfig" /> | `object` | Patch configuration specifications. Contains details on how to apply the patch(es) to a VM instance. |
| <CopyableCode code="recurringSchedule" /> | `object` | Sets the time for recurring patch deployments. |
| <CopyableCode code="rollout" /> | `object` | Patch rollout configuration specifications. Contains details on the concurrency control when applying patch(es) to all targeted VMs. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the patch deployment. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time the patch deployment was last updated. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Get an OS Config patch deployment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Get a page of OS Config patch deployments. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Create an OS Config patch deployment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Delete an OS Config patch deployment. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Update an OS Config patch deployment. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="patchDeploymentsId, projectsId" /> | Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs. |

## `SELECT` examples

Get a page of OS Config patch deployments.

```sql
SELECT
name,
description,
createTime,
duration,
instanceFilter,
lastExecuteTime,
oneTimeSchedule,
patchConfig,
recurringSchedule,
rollout,
state,
updateTime
FROM google.osconfig.patch_deployments
WHERE projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>patch_deployments</code> resource.

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
INSERT INTO google.osconfig.patch_deployments (
projectsId,
name,
description,
instanceFilter,
patchConfig,
duration,
oneTimeSchedule,
recurringSchedule,
rollout
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ instanceFilter }}',
'{{ patchConfig }}',
'{{ duration }}',
'{{ oneTimeSchedule }}',
'{{ recurringSchedule }}',
'{{ rollout }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: instanceFilter
      value:
        - name: all
          value: boolean
        - name: groupLabels
          value:
            - - name: labels
                value: object
        - name: zones
          value:
            - string
        - name: instances
          value:
            - string
        - name: instanceNamePrefixes
          value:
            - string
    - name: patchConfig
      value:
        - name: rebootConfig
          value: string
        - name: apt
          value:
            - name: type
              value: string
            - name: excludes
              value:
                - string
            - name: exclusivePackages
              value:
                - string
        - name: yum
          value:
            - name: security
              value: boolean
            - name: minimal
              value: boolean
            - name: excludes
              value:
                - string
            - name: exclusivePackages
              value:
                - string
        - name: goo
          value: []
        - name: zypper
          value:
            - name: withOptional
              value: boolean
            - name: withUpdate
              value: boolean
            - name: categories
              value:
                - string
            - name: severities
              value:
                - string
            - name: excludes
              value:
                - string
            - name: exclusivePatches
              value:
                - string
        - name: windowsUpdate
          value:
            - name: classifications
              value:
                - string
            - name: excludes
              value:
                - string
            - name: exclusivePatches
              value:
                - string
        - name: preStep
          value:
            - name: linuxExecStepConfig
              value:
                - name: localPath
                  value: string
                - name: gcsObject
                  value:
                    - name: bucket
                      value: string
                    - name: object
                      value: string
                    - name: generationNumber
                      value: string
                - name: allowedSuccessCodes
                  value:
                    - integer
                - name: interpreter
                  value: string
        - name: migInstancesAllowed
          value: boolean
    - name: duration
      value: string
    - name: oneTimeSchedule
      value:
        - name: executeTime
          value: string
    - name: recurringSchedule
      value:
        - name: timeZone
          value:
            - name: id
              value: string
            - name: version
              value: string
        - name: startTime
          value: string
        - name: endTime
          value: string
        - name: timeOfDay
          value:
            - name: hours
              value: integer
            - name: minutes
              value: integer
            - name: seconds
              value: integer
            - name: nanos
              value: integer
        - name: frequency
          value: string
        - name: weekly
          value:
            - name: dayOfWeek
              value: string
        - name: monthly
          value:
            - name: weekDayOfMonth
              value:
                - name: weekOrdinal
                  value: integer
                - name: dayOfWeek
                  value: string
                - name: dayOffset
                  value: integer
            - name: monthDay
              value: integer
        - name: lastExecuteTime
          value: string
        - name: nextExecuteTime
          value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: lastExecuteTime
      value: string
    - name: rollout
      value:
        - name: mode
          value: string
        - name: disruptionBudget
          value:
            - name: fixed
              value: integer
            - name: percent
              value: integer
    - name: state
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>patch_deployments</code> resource.

```sql
/*+ update */
UPDATE google.osconfig.patch_deployments
SET 
name = '{{ name }}',
description = '{{ description }}',
instanceFilter = '{{ instanceFilter }}',
patchConfig = '{{ patchConfig }}',
duration = '{{ duration }}',
oneTimeSchedule = '{{ oneTimeSchedule }}',
recurringSchedule = '{{ recurringSchedule }}',
rollout = '{{ rollout }}'
WHERE 
patchDeploymentsId = '{{ patchDeploymentsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>patch_deployments</code> resource.

```sql
/*+ delete */
DELETE FROM google.osconfig.patch_deployments
WHERE patchDeploymentsId = '{{ patchDeploymentsId }}'
AND projectsId = '{{ projectsId }}';
```

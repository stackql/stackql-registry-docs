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
name: string
description: string
instanceFilter:
  all: boolean
  groupLabels:
    - labels: object
  zones:
    - type: string
  instances:
    - type: string
  instanceNamePrefixes:
    - type: string
patchConfig:
  rebootConfig: string
  apt:
    type: string
    excludes:
      - type: string
    exclusivePackages:
      - type: string
  yum:
    security: boolean
    minimal: boolean
    excludes:
      - type: string
    exclusivePackages:
      - type: string
  goo: {}
  zypper:
    withOptional: boolean
    withUpdate: boolean
    categories:
      - type: string
    severities:
      - type: string
    excludes:
      - type: string
    exclusivePatches:
      - type: string
  windowsUpdate:
    classifications:
      - type: string
        enumDescriptions: string
        enum: string
    excludes:
      - type: string
    exclusivePatches:
      - type: string
  preStep:
    linuxExecStepConfig:
      localPath: string
      gcsObject:
        bucket: string
        object: string
        generationNumber: string
      allowedSuccessCodes:
        - type: string
          format: string
      interpreter: string
  migInstancesAllowed: boolean
duration: string
oneTimeSchedule:
  executeTime: string
recurringSchedule:
  timeZone:
    id: string
    version: string
  startTime: string
  endTime: string
  timeOfDay:
    hours: integer
    minutes: integer
    seconds: integer
    nanos: integer
  frequency: string
  weekly:
    dayOfWeek: string
  monthly:
    weekDayOfMonth:
      weekOrdinal: integer
      dayOfWeek: string
      dayOffset: integer
    monthDay: integer
  lastExecuteTime: string
  nextExecuteTime: string
createTime: string
updateTime: string
lastExecuteTime: string
rollout:
  mode: string
  disruptionBudget:
    fixed: integer
    percent: integer
state: string

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

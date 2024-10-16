---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - dataplex
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

Creates, updates, deletes, gets or lists a <code>tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the task, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/ tasks/{task_id}. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the task. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the task was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly display name. |
| <CopyableCode code="executionSpec" /> | `object` | Execution related settings, like retry and service_account. |
| <CopyableCode code="executionStatus" /> | `object` | Status of the task execution (e.g. Jobs). |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for the task. |
| <CopyableCode code="notebook" /> | `object` | Config for running scheduled notebooks. |
| <CopyableCode code="spark" /> | `object` | User-specified config for running a Spark task. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the task. |
| <CopyableCode code="triggerSpec" /> | `object` | Task scheduling and trigger settings. |
| <CopyableCode code="uid" /> | `string` | Output only. System generated globally unique ID for the task. This ID will be different if the task is deleted and re-created with the same name. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the task was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_lakes_tasks_get" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId, tasksId" /> | Get task resource. |
| <CopyableCode code="projects_locations_lakes_tasks_list" /> | `SELECT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Lists tasks under the given lake. |
| <CopyableCode code="projects_locations_lakes_tasks_create" /> | `INSERT` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Creates a task resource within a lake. |
| <CopyableCode code="projects_locations_lakes_tasks_delete" /> | `DELETE` | <CopyableCode code="lakesId, locationsId, projectsId, tasksId" /> | Delete the task resource. |
| <CopyableCode code="projects_locations_lakes_tasks_patch" /> | `UPDATE` | <CopyableCode code="lakesId, locationsId, projectsId, tasksId" /> | Update the task resource. |
| <CopyableCode code="projects_locations_lakes_tasks_run" /> | `EXEC` | <CopyableCode code="lakesId, locationsId, projectsId, tasksId" /> | Run an on demand execution of a Task. |

## `SELECT` examples

Lists tasks under the given lake.

```sql
SELECT
name,
description,
createTime,
displayName,
executionSpec,
executionStatus,
labels,
notebook,
spark,
state,
triggerSpec,
uid,
updateTime
FROM google.dataplex.tasks
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tasks</code> resource.

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
INSERT INTO google.dataplex.tasks (
lakesId,
locationsId,
projectsId,
description,
displayName,
labels,
triggerSpec,
executionSpec,
spark,
notebook
)
SELECT 
'{{ lakesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ displayName }}',
'{{ labels }}',
'{{ triggerSpec }}',
'{{ executionSpec }}',
'{{ spark }}',
'{{ notebook }}'
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
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: description
      value: string
    - name: displayName
      value: string
    - name: state
      value: string
    - name: labels
      value: object
    - name: triggerSpec
      value:
        - name: type
          value: string
        - name: startTime
          value: string
        - name: disabled
          value: boolean
        - name: maxRetries
          value: integer
        - name: schedule
          value: string
    - name: executionSpec
      value:
        - name: args
          value: object
        - name: serviceAccount
          value: string
        - name: project
          value: string
        - name: maxJobExecutionLifetime
          value: string
        - name: kmsKey
          value: string
    - name: executionStatus
      value:
        - name: updateTime
          value: string
        - name: latestJob
          value:
            - name: name
              value: string
            - name: uid
              value: string
            - name: startTime
              value: string
            - name: endTime
              value: string
            - name: state
              value: string
            - name: retryCount
              value: integer
            - name: service
              value: string
            - name: serviceJob
              value: string
            - name: message
              value: string
            - name: labels
              value: object
            - name: trigger
              value: string
    - name: spark
      value:
        - name: mainJarFileUri
          value: string
        - name: mainClass
          value: string
        - name: pythonScriptFile
          value: string
        - name: sqlScriptFile
          value: string
        - name: sqlScript
          value: string
        - name: fileUris
          value:
            - string
        - name: archiveUris
          value:
            - string
        - name: infrastructureSpec
          value:
            - name: batch
              value:
                - name: executorsCount
                  value: integer
                - name: maxExecutorsCount
                  value: integer
            - name: containerImage
              value:
                - name: image
                  value: string
                - name: javaJars
                  value:
                    - string
                - name: pythonPackages
                  value:
                    - string
                - name: properties
                  value: object
            - name: vpcNetwork
              value:
                - name: network
                  value: string
                - name: subNetwork
                  value: string
                - name: networkTags
                  value:
                    - string
    - name: notebook
      value:
        - name: notebook
          value: string
        - name: fileUris
          value:
            - string
        - name: archiveUris
          value:
            - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tasks</code> resource.

```sql
/*+ update */
UPDATE google.dataplex.tasks
SET 
description = '{{ description }}',
displayName = '{{ displayName }}',
labels = '{{ labels }}',
triggerSpec = '{{ triggerSpec }}',
executionSpec = '{{ executionSpec }}',
spark = '{{ spark }}',
notebook = '{{ notebook }}'
WHERE 
lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tasksId = '{{ tasksId }}';
```

## `DELETE` example

Deletes the specified <code>tasks</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataplex.tasks
WHERE lakesId = '{{ lakesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND tasksId = '{{ tasksId }}';
```

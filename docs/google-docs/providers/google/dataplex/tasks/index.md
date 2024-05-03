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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The relative resource name of the task, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;/ tasks/&#123;task_id&#125;. |
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
| <CopyableCode code="_projects_locations_lakes_tasks_list" /> | `EXEC` | <CopyableCode code="lakesId, locationsId, projectsId" /> | Lists tasks under the given lake. |
| <CopyableCode code="projects_locations_lakes_tasks_patch" /> | `EXEC` | <CopyableCode code="lakesId, locationsId, projectsId, tasksId" /> | Update the task resource. |
| <CopyableCode code="projects_locations_lakes_tasks_run" /> | `EXEC` | <CopyableCode code="lakesId, locationsId, projectsId, tasksId" /> | Run an on demand execution of a Task. |

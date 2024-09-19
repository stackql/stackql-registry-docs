---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - run
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.run.tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The unique name of this Task. |
| <CopyableCode code="annotations" /> | `object` | Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects. |
| <CopyableCode code="completionTime" /> | `string` | Output only. Represents time when the Task was completed. It is not guaranteed to be set in happens-before order across separate operations. |
| <CopyableCode code="conditions" /> | `array` | Output only. The Condition of this Task, containing its readiness status, and detailed error information in case it did not reach the desired state. |
| <CopyableCode code="containers" /> | `array` | Holds the single container that defines the unit of execution for this task. |
| <CopyableCode code="createTime" /> | `string` | Output only. Represents time when the task was created by the system. It is not guaranteed to be set in happens-before order across separate operations. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request. |
| <CopyableCode code="encryptionKey" /> | `string` | Output only. A reference to a customer managed encryption key (CMEK) to use to encrypt this container image. For more information, go to https://cloud.google.com/run/docs/securing/using-cmek |
| <CopyableCode code="etag" /> | `string` | Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. |
| <CopyableCode code="execution" /> | `string` | Output only. The name of the parent Execution. |
| <CopyableCode code="executionEnvironment" /> | `string` | The execution environment being used to host this Task. |
| <CopyableCode code="expireTime" /> | `string` | Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request. |
| <CopyableCode code="generation" /> | `string` | Output only. A number that monotonically increases every time the user modifies the desired state. |
| <CopyableCode code="index" /> | `integer` | Output only. Index of the Task, unique per execution, and beginning at 0. |
| <CopyableCode code="job" /> | `string` | Output only. The name of the parent Job. |
| <CopyableCode code="labels" /> | `object` | Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit https://cloud.google.com/resource-manager/docs/creating-managing-labels or https://cloud.google.com/run/docs/configuring/labels |
| <CopyableCode code="lastAttemptResult" /> | `object` | Result of a task attempt. |
| <CopyableCode code="logUri" /> | `string` | Output only. URI where logs for this execution can be found in Cloud Console. |
| <CopyableCode code="maxRetries" /> | `integer` | Number of retries allowed per Task, before marking this Task failed. |
| <CopyableCode code="observedGeneration" /> | `string` | Output only. The generation of this Task. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run. |
| <CopyableCode code="retried" /> | `integer` | Output only. The number of times this Task was retried. Tasks are retried when they fail up to the maxRetries limit. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="scheduledTime" /> | `string` | Output only. Represents time when the task was scheduled to run by the system. It is not guaranteed to be set in happens-before order across separate operations. |
| <CopyableCode code="serviceAccount" /> | `string` | Email address of the IAM service account associated with the Task of a Job. The service account represents the identity of the running task, and determines what permissions the task has. If not provided, the task will use the project's default service account. |
| <CopyableCode code="startTime" /> | `string` | Output only. Represents time when the task started to run. It is not guaranteed to be set in happens-before order across separate operations. |
| <CopyableCode code="timeout" /> | `string` | Max allowed time duration the Task may be active before the system will actively try to mark it failed and kill associated containers. This applies per attempt of a task, meaning each retry can run for the full timeout. |
| <CopyableCode code="uid" /> | `string` | Output only. Server assigned unique identifier for the Task. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last-modified time. |
| <CopyableCode code="volumes" /> | `array` | A list of Volumes to make available to containers. |
| <CopyableCode code="vpcAccess" /> | `object` | VPC Access settings. For more information on sending traffic to a VPC network, visit https://cloud.google.com/run/docs/configuring/connecting-vpc. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="executionsId, jobsId, locationsId, projectsId, tasksId" /> | Gets information about a Task. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="executionsId, jobsId, locationsId, projectsId" /> | Lists Tasks from an Execution of a Job. |

## `SELECT` examples

Lists Tasks from an Execution of a Job.

```sql
SELECT
name,
annotations,
completionTime,
conditions,
containers,
createTime,
deleteTime,
encryptionKey,
etag,
execution,
executionEnvironment,
expireTime,
generation,
index,
job,
labels,
lastAttemptResult,
logUri,
maxRetries,
observedGeneration,
reconciling,
retried,
satisfiesPzs,
scheduledTime,
serviceAccount,
startTime,
timeout,
uid,
updateTime,
volumes,
vpcAccess
FROM google.run.tasks
WHERE executionsId = '{{ executionsId }}'
AND jobsId = '{{ jobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```


---
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
  - cloudtasks
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

Creates, updates, deletes or gets an <code>queue</code> resource or lists <code>queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudtasks.queues" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Caller-specified and required in CreateQueue, after which it becomes output only. The queue name. The queue name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the queue's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. |
| <CopyableCode code="appEngineRoutingOverride" /> | `object` | App Engine Routing. Defines routing characteristics specific to App Engine - service, version, and instance. For more information about services, versions, and instances see [An Overview of App Engine](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine), [Microservices Architecture on Google App Engine](https://cloud.google.com/appengine/docs/python/microservices-on-app-engine), [App Engine Standard request routing](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed), and [App Engine Flex request routing](https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed). Using AppEngineRouting requires [`appengine.applications.get`](https://cloud.google.com/appengine/docs/admin-api/access-control) Google IAM permission for the project and the following scope: `https://www.googleapis.com/auth/cloud-platform` |
| <CopyableCode code="httpTarget" /> | `object` | HTTP target. When specified as a Queue, all the tasks with [HttpRequest] will be overridden according to the target. |
| <CopyableCode code="purgeTime" /> | `string` | Output only. The last time this queue was purged. All tasks that were created before this time were purged. A queue can be purged using PurgeQueue, the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue). Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged. |
| <CopyableCode code="rateLimits" /> | `object` | Rate limits. This message determines the maximum rate that tasks can be dispatched by a queue, regardless of whether the dispatch is a first task attempt or a retry. Note: The debugging command, RunTask, will run a task even if the queue has reached its RateLimits. |
| <CopyableCode code="retryConfig" /> | `object` | Retry config. These settings determine when a failed task attempt is retried. |
| <CopyableCode code="stackdriverLoggingConfig" /> | `object` | Configuration options for writing logs to [Stackdriver Logging](https://cloud.google.com/logging/docs/). |
| <CopyableCode code="state" /> | `string` | Output only. The state of the queue. `state` can only be changed by calling PauseQueue, ResumeQueue, or uploading [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref). UpdateQueue cannot be used to change `state`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, queuesId" /> | Gets a queue. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists queues. Queues are returned in lexicographical order. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a queue. Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not. WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, queuesId" /> | Deletes a queue. This command will delete the queue even if it has tasks in it. Note: If you delete a queue, you may be prevented from creating a new queue with the same name as the deleted queue for a tombstone window of up to 3 days. During this window, the CreateQueue operation may appear to recreate the queue, but this can be misleading. If you attempt to create a queue with the same name as one that is in the tombstone window, run GetQueue to confirm that the queue creation was successful. If GetQueue returns 200 response code, your queue was successfully created with the name of the previously deleted queue. Otherwise, your queue did not successfully recreate. WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, queuesId" /> | Updates a queue. This method creates the queue if it does not exist and updates the queue if it does exist. Queues created with this method allow tasks to live for a maximum of 31 days. After a task is 31 days old, the task will be deleted regardless of whether it was dispatched or not. WARNING: Using this method may have unintended side effects if you are using an App Engine `queue.yaml` or `queue.xml` file to manage your queues. Read [Overview of Queue Management and queue.yaml](https://cloud.google.com/tasks/docs/queue-yaml) before using this method. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, queuesId" /> | Pauses the queue. If a queue is paused then the system will stop dispatching tasks until the queue is resumed via ResumeQueue. Tasks can still be added when the queue is paused. A queue is paused if its state is PAUSED. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, queuesId" /> | Purges a queue by deleting all of its tasks. All tasks created before this method is called are permanently deleted. Purge operations can take up to one minute to take effect. Tasks might be dispatched before the purge takes effect. A purge is irreversible. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, queuesId" /> | Resume a queue. This method resumes a queue after it has been PAUSED or DISABLED. The state of a queue is stored in the queue's state; after calling this method it will be set to RUNNING. WARNING: Resuming many high-QPS queues at the same time can lead to target overloading. If you are resuming high-QPS queues, follow the 500/50/5 pattern described in [Managing Cloud Tasks Scaling Risks](https://cloud.google.com/tasks/docs/manage-cloud-task-scaling). |

## `SELECT` examples

Lists queues. Queues are returned in lexicographical order.

```sql
SELECT
name,
appEngineRoutingOverride,
httpTarget,
purgeTime,
rateLimits,
retryConfig,
stackdriverLoggingConfig,
state
FROM google.cloudtasks.queues
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queues</code> resource.

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
INSERT INTO google.cloudtasks.queues (
locationsId,
projectsId,
name,
appEngineRoutingOverride,
httpTarget,
rateLimits,
retryConfig,
state,
purgeTime,
stackdriverLoggingConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ appEngineRoutingOverride }}',
'{{ httpTarget }}',
'{{ rateLimits }}',
'{{ retryConfig }}',
'{{ state }}',
'{{ purgeTime }}',
'{{ stackdriverLoggingConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: appEngineRoutingOverride
        value: '{{ appEngineRoutingOverride }}'
      - name: httpTarget
        value: '{{ httpTarget }}'
      - name: rateLimits
        value: '{{ rateLimits }}'
      - name: retryConfig
        value: '{{ retryConfig }}'
      - name: state
        value: '{{ state }}'
      - name: purgeTime
        value: '{{ purgeTime }}'
      - name: stackdriverLoggingConfig
        value: '{{ stackdriverLoggingConfig }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a queue only if the necessary resources are available.

```sql
UPDATE google.cloudtasks.queues
SET 
name = '{{ name }}',
appEngineRoutingOverride = '{{ appEngineRoutingOverride }}',
httpTarget = '{{ httpTarget }}',
rateLimits = '{{ rateLimits }}',
retryConfig = '{{ retryConfig }}',
state = '{{ state }}',
purgeTime = '{{ purgeTime }}',
stackdriverLoggingConfig = '{{ stackdriverLoggingConfig }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND queuesId = '{{ queuesId }}';
```

## `DELETE` example

Deletes the specified queue resource.

```sql
DELETE FROM google.cloudtasks.queues
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND queuesId = '{{ queuesId }}';
```

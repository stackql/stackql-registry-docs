---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - cloudscheduler
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudscheduler.jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optionally caller-specified in CreateJob, after which it becomes output only. The job name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID`. * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * `LOCATION_ID` is the canonical ID for the job's location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * `JOB_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters. |
| <CopyableCode code="description" /> | `string` | Optionally caller-specified in CreateJob or UpdateJob. A human-readable description for the job. This string must not contain more than 500 characters. |
| <CopyableCode code="appEngineHttpTarget" /> | `object` | App Engine target. The job will be pushed to a job handler by means of an HTTP request via an http_method such as HTTP POST, HTTP GET, etc. The job is acknowledged by means of an HTTP response code in the range [200 - 299]. Error 503 is considered an App Engine system error instead of an application error. Requests returning error 503 will be retried regardless of retry configuration and not counted against retry counts. Any other response code, or a failure to receive a response before the deadline, constitutes a failed attempt. |
| <CopyableCode code="attemptDeadline" /> | `string` | The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled and the attempt is marked as a `DEADLINE_EXCEEDED` failure. The failed attempt can be viewed in execution logs. Cloud Scheduler will retry the job according to the RetryConfig. The default and the allowed values depend on the type of target: * For HTTP targets, the default is 3 minutes. The deadline must be in the interval [15 seconds, 30 minutes]. * For App Engine HTTP targets, 0 indicates that the request has the default deadline. The default deadline depends on the scaling type of the service: 10 minutes for standard apps with automatic scaling, 24 hours for standard apps with manual and basic scaling, and 60 minutes for flex apps. If the request deadline is set, it must be in the interval [15 seconds, 24 hours 15 seconds]. * For Pub/Sub targets, this field is ignored. |
| <CopyableCode code="httpTarget" /> | `object` | Http target. The job will be pushed to the job handler by means of an HTTP request via an http_method such as HTTP POST, HTTP GET, etc. The job is acknowledged by means of an HTTP response code in the range [200 - 299]. A failure to receive a response constitutes a failed execution. For a redirected request, the response returned by the redirected request is considered. |
| <CopyableCode code="lastAttemptTime" /> | `string` | Output only. The time the last job attempt started. |
| <CopyableCode code="pubsubTarget" /> | `object` | Pub/Sub target. The job will be delivered by publishing a message to the given Pub/Sub topic. |
| <CopyableCode code="retryConfig" /> | `object` | Settings that determine the retry behavior. By default, if a job does not complete successfully (meaning that an acknowledgement is not received from the handler, then it will be retried with exponential backoff according to the settings in RetryConfig. |
| <CopyableCode code="schedule" /> | `string` | Required, except when used with UpdateJob. Describes the schedule on which the job will be executed. The schedule can be either of the following types: * [Crontab](https://en.wikipedia.org/wiki/Cron#Overview) * English-like [schedule](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules) As a general rule, execution `n + 1` of a job will not begin until execution `n` has finished. Cloud Scheduler will never allow two simultaneously outstanding executions. For example, this implies that if the `n+1`th execution is scheduled to run at 16:00 but the `n`th execution takes until 16:15, the `n+1`th execution will not start until `16:15`. A scheduled start time will be delayed if the previous execution has not ended when its scheduled time occurs. If retry_count > 0 and a job attempt fails, the job will be tried a total of retry_count times, with exponential backoff, until the next scheduled start time. If retry_count is 0, a job attempt will not be retried if it fails. Instead the Cloud Scheduler system will wait for the next scheduled execution time. Setting retry_count to 0 does not prevent failed jobs from running according to schedule after the failure. |
| <CopyableCode code="scheduleTime" /> | `string` | Output only. The next time the job is scheduled. Note that this may be a retry of a previously failed attempt or the next execution time according to the schedule. |
| <CopyableCode code="state" /> | `string` | Output only. State of the job. |
| <CopyableCode code="status" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="timeZone" /> | `string` | Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the [tz database](http://en.wikipedia.org/wiki/Tz_database). Note that some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen tz. For UTC use the string "utc". If a time zone is not specified, the default will be in UTC (also known as GMT). |
| <CopyableCode code="userUpdateTime" /> | `string` | Output only. The creation time of the job. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Gets a job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Deletes a job. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Updates a job. If successful, the updated Job is returned. If the job does not exist, `NOT_FOUND` is returned. If UpdateJob does not successfully return, it is possible for the job to be in an Job.State.UPDATE_FAILED state. A job in this state may not be executed. If this happens, retry the UpdateJob request until a successful response is received. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Pauses a job. If a job is paused then the system will stop executing the job until it is re-enabled via ResumeJob. The state of the job is stored in state; if paused it will be set to Job.State.PAUSED. A job must be in Job.State.ENABLED to be paused. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Resume a job. This method reenables a job after it has been Job.State.PAUSED. The state of a job is stored in Job.state; after calling this method it will be set to Job.State.ENABLED. A job must be in Job.State.PAUSED to be resumed. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="jobsId, locationsId, projectsId" /> | Forces a job to run now. When this method is called, Cloud Scheduler will dispatch the job, even if the job is already running. |

## `SELECT` examples

Lists jobs.

```sql
SELECT
name,
description,
appEngineHttpTarget,
attemptDeadline,
httpTarget,
lastAttemptTime,
pubsubTarget,
retryConfig,
schedule,
scheduleTime,
state,
status,
timeZone,
userUpdateTime
FROM google.cloudscheduler.jobs
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
INSERT INTO google.cloudscheduler.jobs (
locationsId,
projectsId,
name,
description,
pubsubTarget,
appEngineHttpTarget,
httpTarget,
schedule,
timeZone,
retryConfig,
attemptDeadline
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ pubsubTarget }}',
'{{ appEngineHttpTarget }}',
'{{ httpTarget }}',
'{{ schedule }}',
'{{ timeZone }}',
'{{ retryConfig }}',
'{{ attemptDeadline }}'
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
    - name: pubsubTarget
      value:
        - name: topicName
          value: string
        - name: data
          value: string
        - name: attributes
          value: object
    - name: appEngineHttpTarget
      value:
        - name: httpMethod
          value: string
        - name: appEngineRouting
          value:
            - name: service
              value: string
            - name: version
              value: string
            - name: instance
              value: string
            - name: host
              value: string
        - name: relativeUri
          value: string
        - name: headers
          value: object
        - name: body
          value: string
    - name: httpTarget
      value:
        - name: uri
          value: string
        - name: httpMethod
          value: string
        - name: headers
          value: object
        - name: body
          value: string
        - name: oauthToken
          value:
            - name: serviceAccountEmail
              value: string
            - name: scope
              value: string
        - name: oidcToken
          value:
            - name: serviceAccountEmail
              value: string
            - name: audience
              value: string
    - name: schedule
      value: string
    - name: timeZone
      value: string
    - name: userUpdateTime
      value: string
    - name: state
      value: string
    - name: status
      value:
        - name: code
          value: integer
        - name: message
          value: string
        - name: details
          value:
            - object
    - name: scheduleTime
      value: string
    - name: lastAttemptTime
      value: string
    - name: retryConfig
      value:
        - name: retryCount
          value: integer
        - name: maxRetryDuration
          value: string
        - name: minBackoffDuration
          value: string
        - name: maxBackoffDuration
          value: string
        - name: maxDoublings
          value: integer
    - name: attemptDeadline
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>jobs</code> resource.

```sql
/*+ update */
UPDATE google.cloudscheduler.jobs
SET 
name = '{{ name }}',
description = '{{ description }}',
pubsubTarget = '{{ pubsubTarget }}',
appEngineHttpTarget = '{{ appEngineHttpTarget }}',
httpTarget = '{{ httpTarget }}',
schedule = '{{ schedule }}',
timeZone = '{{ timeZone }}',
retryConfig = '{{ retryConfig }}',
attemptDeadline = '{{ attemptDeadline }}'
WHERE 
jobsId = '{{ jobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudscheduler.jobs
WHERE jobsId = '{{ jobsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

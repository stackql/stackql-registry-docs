---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - scheduler
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scheduler.jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets the job resource identifier. |
| <CopyableCode code="name" /> | `text` | Gets the job resource name. |
| <CopyableCode code="action" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recurrence" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets the job resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the job resource identifier. |
| <CopyableCode code="name" /> | `string` | Gets the job resource name. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Gets the job resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Gets a job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="jobCollectionName, resourceGroupName, subscriptionId" /> | Lists all jobs under the specified job collection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Provisions a new job or updates an existing job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Deletes a job. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Patches an existing job. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="jobCollectionName, jobName, resourceGroupName, subscriptionId" /> | Runs a job. |

## `SELECT` examples

Lists all jobs under the specified job collection.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_jobs', value: 'view', },
        { label: 'jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
action,
jobCollectionName,
jobName,
recurrence,
resourceGroupName,
start_time,
state,
status,
subscriptionId,
type
FROM azure.scheduler.vw_jobs
WHERE jobCollectionName = '{{ jobCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.scheduler.jobs
WHERE jobCollectionName = '{{ jobCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


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
INSERT INTO azure.scheduler.jobs (
jobCollectionName,
jobName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ jobCollectionName }}',
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: type
      value: string
    - name: name
      value: string
    - name: properties
      value:
        - name: startTime
          value: string
        - name: action
          value:
            - name: type
              value: string
            - name: request
              value:
                - name: authentication
                  value:
                    - name: type
                      value: string
                - name: uri
                  value: string
                - name: method
                  value: string
                - name: body
                  value: string
                - name: headers
                  value: object
            - name: queueMessage
              value:
                - name: storageAccount
                  value: string
                - name: queueName
                  value: string
                - name: sasToken
                  value: string
                - name: message
                  value: string
            - name: serviceBusQueueMessage
              value:
                - name: queueName
                  value: string
                - name: authentication
                  value:
                    - name: sasKey
                      value: string
                    - name: sasKeyName
                      value: string
                    - name: type
                      value: string
                - name: brokeredMessageProperties
                  value:
                    - name: contentType
                      value: string
                    - name: correlationId
                      value: string
                    - name: forcePersistence
                      value: boolean
                    - name: label
                      value: string
                    - name: messageId
                      value: string
                    - name: partitionKey
                      value: string
                    - name: replyTo
                      value: string
                    - name: replyToSessionId
                      value: string
                    - name: scheduledEnqueueTimeUtc
                      value: string
                    - name: sessionId
                      value: string
                    - name: timeToLive
                      value: string
                    - name: to
                      value: string
                    - name: viaPartitionKey
                      value: string
                - name: customMessageProperties
                  value: object
                - name: message
                  value: string
                - name: namespace
                  value: string
                - name: transportType
                  value: string
            - name: serviceBusTopicMessage
              value:
                - name: topicPath
                  value: string
                - name: customMessageProperties
                  value: object
                - name: message
                  value: string
                - name: namespace
                  value: string
                - name: transportType
                  value: string
            - name: retryPolicy
              value:
                - name: retryType
                  value: string
                - name: retryInterval
                  value: string
                - name: retryCount
                  value: integer
            - name: errorAction
              value:
                - name: type
                  value: string
        - name: recurrence
          value:
            - name: frequency
              value: string
            - name: interval
              value: integer
            - name: count
              value: integer
            - name: endTime
              value: string
            - name: schedule
              value:
                - name: weekDays
                  value:
                    - string
                - name: hours
                  value:
                    - integer
                - name: minutes
                  value:
                    - integer
                - name: monthDays
                  value:
                    - integer
                - name: monthlyOccurrences
                  value:
                    - - name: day
                        value: string
                      - name: Occurrence
                        value: integer
        - name: state
          value: []
        - name: status
          value:
            - name: executionCount
              value: integer
            - name: failureCount
              value: integer
            - name: faultedCount
              value: integer
            - name: lastExecutionTime
              value: string
            - name: nextExecutionTime
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>jobs</code> resource.

```sql
/*+ update */
UPDATE azure.scheduler.jobs
SET 
properties = '{{ properties }}'
WHERE 
jobCollectionName = '{{ jobCollectionName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.scheduler.jobs
WHERE jobCollectionName = '{{ jobCollectionName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

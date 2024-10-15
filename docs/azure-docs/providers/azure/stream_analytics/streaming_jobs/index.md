---
title: streaming_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_jobs
  - stream_analytics
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

Creates, updates, deletes, gets or lists a <code>streaming_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.streaming_jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_streaming_jobs', value: 'view', },
        { label: 'streaming_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster" /> | `text` | field from the `properties` object |
| <CopyableCode code="compatibility_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_storage_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_locale" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="events_late_arrival_max_delay_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="events_out_of_order_max_delay_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="events_out_of_order_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="functions" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Describes how identity is verified |
| <CopyableCode code="inputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_storage_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_output_event_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="output_error_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_start_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="transformation" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Describes how identity is verified |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with a streaming job. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Gets details about the specified streaming job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the streaming jobs in the given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the streaming jobs in the specified resource group. |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Creates a streaming job or replaces an already existing streaming job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Deletes a streaming job. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Updates an existing streaming job. This can be used to partially update (ie. update one or two properties) a streaming job without affecting the rest the job definition. |
| <CopyableCode code="scale" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Scales a streaming job when the job is running. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Starts a streaming job. Once a job is started it will start processing input events and produce output. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Stops a running streaming job. This will cause a running streaming job to stop processing input events and producing output. |

## `SELECT` examples

Lists all of the streaming jobs in the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_streaming_jobs', value: 'view', },
        { label: 'streaming_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cluster,
compatibility_level,
content_storage_policy,
created_date,
data_locale,
etag,
events_late_arrival_max_delay_in_seconds,
events_out_of_order_max_delay_in_seconds,
events_out_of_order_policy,
functions,
identity,
inputs,
jobName,
job_id,
job_state,
job_storage_account,
job_type,
last_output_event_time,
location,
output_error_policy,
output_start_mode,
output_start_time,
outputs,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
transformation
FROM azure.stream_analytics.vw_streaming_jobs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.stream_analytics.streaming_jobs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>streaming_jobs</code> resource.

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
INSERT INTO azure.stream_analytics.streaming_jobs (
jobName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
identity
)
SELECT 
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: sku
          value:
            - name: name
              value: string
        - name: jobId
          value: string
        - name: provisioningState
          value: string
        - name: jobState
          value: string
        - name: jobType
          value: string
        - name: outputStartMode
          value: []
        - name: outputStartTime
          value: string
        - name: lastOutputEventTime
          value: string
        - name: eventsOutOfOrderPolicy
          value: []
        - name: outputErrorPolicy
          value: []
        - name: eventsOutOfOrderMaxDelayInSeconds
          value: integer
        - name: eventsLateArrivalMaxDelayInSeconds
          value: integer
        - name: dataLocale
          value: string
        - name: compatibilityLevel
          value: []
        - name: createdDate
          value: string
        - name: inputs
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: type
                    value: string
                  - name: serialization
                    value:
                      - name: type
                        value: []
                  - name: diagnostics
                    value:
                      - name: conditions
                        value:
                          - - name: since
                              value: string
                            - name: code
                              value: string
                            - name: message
                              value: string
                  - name: etag
                    value: string
                  - name: compression
                    value:
                      - name: type
                        value: []
                  - name: partitionKey
                    value: string
        - name: transformation
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: type
              value: string
            - name: properties
              value:
                - name: streamingUnits
                  value: integer
                - name: validStreamingUnits
                  value:
                    - integer
                - name: query
                  value: string
                - name: etag
                  value: string
        - name: outputs
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: datasource
                    value:
                      - name: type
                        value: string
                  - name: timeWindow
                    value: string
                  - name: sizeWindow
                    value: integer
                  - name: etag
                    value: string
        - name: functions
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: type
                    value: string
                  - name: etag
                    value: string
                  - name: properties
                    value:
                      - name: inputs
                        value:
                          - - name: dataType
                              value: string
                            - name: isConfigurationParameter
                              value: boolean
                      - name: output
                        value:
                          - name: dataType
                            value: string
                      - name: binding
                        value:
                          - name: type
                            value: string
        - name: etag
          value: string
        - name: jobStorageAccount
          value:
            - name: accountName
              value: string
            - name: accountKey
              value: string
            - name: authenticationMode
              value: []
        - name: contentStoragePolicy
          value: string
        - name: cluster
          value:
            - name: id
              value: string
    - name: identity
      value:
        - name: tenantId
          value: string
        - name: principalId
          value: string
        - name: type
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>streaming_jobs</code> resource.

```sql
/*+ update */
UPDATE azure.stream_analytics.streaming_jobs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>streaming_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.stream_analytics.streaming_jobs
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

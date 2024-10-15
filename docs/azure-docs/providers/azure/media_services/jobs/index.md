---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - media_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.jobs" /></td></tr>
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
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="input" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputs" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="transformName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the Job. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId, transformName" /> | Gets a Job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, transformName" /> | Lists all of the Jobs for the Transform. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId, transformName" /> | Creates a Job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId, transformName" /> | Deletes a Job. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId, transformName" /> | Update is only supported for description and priority. Updating Priority will take effect when the Job state is Queued or Scheduled and depending on the timing the priority update may be ignored. |
| <CopyableCode code="cancel_job" /> | `EXEC` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId, transformName" /> | Cancel a Job. |

## `SELECT` examples

Lists all of the Jobs for the Transform.

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
description,
accountName,
correlation_data,
created,
end_time,
input,
jobName,
last_modified,
outputs,
priority,
resourceGroupName,
start_time,
state,
subscriptionId,
system_data,
transformName
FROM azure.media_services.vw_jobs
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND transformName = '{{ transformName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.media_services.jobs
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND transformName = '{{ transformName }}';
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
INSERT INTO azure.media_services.jobs (
accountName,
jobName,
resourceGroupName,
subscriptionId,
transformName,
properties
)
SELECT 
'{{ accountName }}',
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ transformName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: created
          value: string
        - name: state
          value: string
        - name: description
          value: string
        - name: input
          value:
            - name: '@odata.type'
              value: string
        - name: lastModified
          value: string
        - name: outputs
          value:
            - - name: '@odata.type'
                value: string
              - name: error
                value:
                  - name: code
                    value: string
                  - name: message
                    value: string
                  - name: category
                    value: string
                  - name: retry
                    value: string
                  - name: details
                    value:
                      - - name: code
                          value: string
                        - name: message
                          value: string
              - name: presetOverride
                value:
                  - name: '@odata.type'
                    value: string
              - name: state
                value: string
              - name: progress
                value: integer
              - name: label
                value: string
              - name: startTime
                value: string
              - name: endTime
                value: string
        - name: priority
          value: string
        - name: correlationData
          value: object
        - name: startTime
          value: string
        - name: endTime
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>jobs</code> resource.

```sql
/*+ update */
UPDATE azure.media_services.jobs
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND transformName = '{{ transformName }}';
```

## `DELETE` example

Deletes the specified <code>jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.jobs
WHERE accountName = '{{ accountName }}'
AND jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND transformName = '{{ transformName }}';
```

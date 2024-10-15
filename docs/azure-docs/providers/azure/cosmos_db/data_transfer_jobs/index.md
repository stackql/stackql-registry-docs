---
title: data_transfer_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - data_transfer_jobs
  - cosmos_db
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

Creates, updates, deletes, gets or lists a <code>data_transfer_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_transfer_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.data_transfer_jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_transfer_jobs', value: 'view', },
        { label: 'data_transfer_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `text` | The name of the database account. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_utc_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="processed_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of Azure resource. |
| <CopyableCode code="worker_count" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | The properties of a DataTransfer Job |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId" /> | Get a Data Transfer Job. |
| <CopyableCode code="list_by_database_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get a list of Data Transfer jobs. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Data Transfer Job. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId" /> | Cancels a Data Transfer Job. |
| <CopyableCode code="complete" /> | `EXEC` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId" /> | Completes a Data Transfer Online Job. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId" /> | Pause a Data Transfer Job. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="accountName, jobName, resourceGroupName, subscriptionId" /> | Resumes a Data Transfer Job. |

## `SELECT` examples

Get a list of Data Transfer jobs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_transfer_jobs', value: 'view', },
        { label: 'data_transfer_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
destination,
duration,
error,
jobName,
job_name,
last_updated_utc_time,
mode,
processed_count,
resourceGroupName,
source,
status,
subscriptionId,
total_count,
type,
worker_count
FROM azure.cosmos_db.vw_data_transfer_jobs
WHERE accountName = '{{ accountName }}'
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
FROM azure.cosmos_db.data_transfer_jobs
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_transfer_jobs</code> resource.

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
INSERT INTO azure.cosmos_db.data_transfer_jobs (
accountName,
jobName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ accountName }}',
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: jobName
          value: string
        - name: source
          value:
            - name: component
              value: string
        - name: status
          value: string
        - name: processedCount
          value: integer
        - name: totalCount
          value: integer
        - name: lastUpdatedUtcTime
          value: string
        - name: workerCount
          value: integer
        - name: error
          value:
            - name: code
              value: string
            - name: message
              value: string
        - name: duration
          value: string
        - name: mode
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

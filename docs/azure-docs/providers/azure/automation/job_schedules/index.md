---
title: job_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - job_schedules
  - automation
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

Creates, updates, deletes, gets or lists a <code>job_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.job_schedules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_schedules', value: 'view', },
        { label: 'job_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets the id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets the name of the variable. |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobScheduleId" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_schedule_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="runbook" /> | `text` | field from the `properties` object |
| <CopyableCode code="schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets the name of the variable. |
| <CopyableCode code="properties" /> | `object` | Definition of job schedule parameters. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, jobScheduleId, resourceGroupName, subscriptionId" /> | Retrieve the job schedule identified by job schedule name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of job schedules. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="automationAccountName, jobScheduleId, resourceGroupName, subscriptionId, data__properties" /> | Create a job schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, jobScheduleId, resourceGroupName, subscriptionId" /> | Delete the job schedule identified by job schedule name. |

## `SELECT` examples

Retrieve a list of job schedules.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_schedules', value: 'view', },
        { label: 'job_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
automationAccountName,
jobScheduleId,
job_schedule_id,
parameters,
resourceGroupName,
run_on,
runbook,
schedule,
subscriptionId,
type
FROM azure.automation.vw_job_schedules
WHERE automationAccountName = '{{ automationAccountName }}'
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
FROM azure.automation.job_schedules
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_schedules</code> resource.

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
INSERT INTO azure.automation.job_schedules (
automationAccountName,
jobScheduleId,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ automationAccountName }}',
'{{ jobScheduleId }}',
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
        - name: schedule
          value:
            - name: name
              value: string
        - name: runbook
          value:
            - name: name
              value: string
        - name: runOn
          value: string
        - name: parameters
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>job_schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.job_schedules
WHERE automationAccountName = '{{ automationAccountName }}'
AND jobScheduleId = '{{ jobScheduleId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

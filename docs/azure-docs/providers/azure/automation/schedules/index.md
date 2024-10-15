---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
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

Creates, updates, deletes, gets or lists a <code>schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.schedules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_schedules', value: 'view', },
        { label: 'schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="advanced_schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiry_time_offset_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="frequency" /> | `text` | field from the `properties` object |
| <CopyableCode code="interval" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_run" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_run_offset_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time_offset_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Definition of schedule parameters. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, scheduleName, subscriptionId" /> | Retrieve the schedule identified by schedule name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of schedules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, scheduleName, subscriptionId, data__name, data__properties" /> | Create a schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, scheduleName, subscriptionId" /> | Delete the schedule identified by schedule name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, resourceGroupName, scheduleName, subscriptionId" /> | Update the schedule identified by schedule name. |

## `SELECT` examples

Retrieve a list of schedules.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_schedules', value: 'view', },
        { label: 'schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
advanced_schedule,
automationAccountName,
creation_time,
expiry_time,
expiry_time_offset_minutes,
frequency,
interval,
is_enabled,
last_modified_time,
next_run,
next_run_offset_minutes,
resourceGroupName,
scheduleName,
start_time,
start_time_offset_minutes,
subscriptionId,
time_zone
FROM azure.automation.vw_schedules
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.automation.schedules
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>schedules</code> resource.

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
INSERT INTO azure.automation.schedules (
automationAccountName,
resourceGroupName,
scheduleName,
subscriptionId,
data__name,
data__properties,
name,
properties
)
SELECT 
'{{ automationAccountName }}',
'{{ resourceGroupName }}',
'{{ scheduleName }}',
'{{ subscriptionId }}',
'{{ data__name }}',
'{{ data__properties }}',
'{{ name }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: properties
      value:
        - name: description
          value: string
        - name: startTime
          value: string
        - name: expiryTime
          value: string
        - name: interval
          value: string
        - name: frequency
          value: []
        - name: timeZone
          value: string
        - name: advancedSchedule
          value:
            - name: weekDays
              value:
                - string
            - name: monthDays
              value:
                - integer
            - name: monthlyOccurrences
              value:
                - - name: occurrence
                    value: integer
                  - name: day
                    value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>schedules</code> resource.

```sql
/*+ update */
UPDATE azure.automation.schedules
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scheduleName = '{{ scheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.schedules
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scheduleName = '{{ scheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

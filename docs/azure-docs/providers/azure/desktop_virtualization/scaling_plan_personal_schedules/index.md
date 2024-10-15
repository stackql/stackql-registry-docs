---
title: scaling_plan_personal_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_plan_personal_schedules
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>scaling_plan_personal_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_plan_personal_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.scaling_plan_personal_schedules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scaling_plan_personal_schedules', value: 'view', },
        { label: 'scaling_plan_personal_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="days_of_week" /> | `text` | field from the `properties` object |
| <CopyableCode code="off_peak_action_on_disconnect" /> | `text` | field from the `properties` object |
| <CopyableCode code="off_peak_action_on_logoff" /> | `text` | field from the `properties` object |
| <CopyableCode code="off_peak_minutes_to_wait_on_disconnect" /> | `text` | field from the `properties` object |
| <CopyableCode code="off_peak_minutes_to_wait_on_logoff" /> | `text` | field from the `properties` object |
| <CopyableCode code="off_peak_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="off_peak_start_vm_on_connect" /> | `text` | field from the `properties` object |
| <CopyableCode code="peak_action_on_disconnect" /> | `text` | field from the `properties` object |
| <CopyableCode code="peak_action_on_logoff" /> | `text` | field from the `properties` object |
| <CopyableCode code="peak_minutes_to_wait_on_disconnect" /> | `text` | field from the `properties` object |
| <CopyableCode code="peak_minutes_to_wait_on_logoff" /> | `text` | field from the `properties` object |
| <CopyableCode code="peak_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="peak_start_vm_on_connect" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_action_on_disconnect" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_action_on_logoff" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_minutes_to_wait_on_disconnect" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_minutes_to_wait_on_logoff" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_start_vm_on_connect" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_action_on_disconnect" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_action_on_logoff" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_auto_start_hosts" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_minutes_to_wait_on_disconnect" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_minutes_to_wait_on_logoff" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_start_vm_on_connect" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scalingPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scalingPlanScheduleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A ScalingPlanPersonalSchedule. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId" /> | Get a ScalingPlanPersonalSchedule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, scalingPlanName, subscriptionId" /> | List ScalingPlanPersonalSchedules. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId, data__properties" /> | Create or update a ScalingPlanPersonalSchedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId" /> | Remove a ScalingPlanPersonalSchedule. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId" /> | Update a ScalingPlanPersonalSchedule. |

## `SELECT` examples

List ScalingPlanPersonalSchedules.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scaling_plan_personal_schedules', value: 'view', },
        { label: 'scaling_plan_personal_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
days_of_week,
off_peak_action_on_disconnect,
off_peak_action_on_logoff,
off_peak_minutes_to_wait_on_disconnect,
off_peak_minutes_to_wait_on_logoff,
off_peak_start_time,
off_peak_start_vm_on_connect,
peak_action_on_disconnect,
peak_action_on_logoff,
peak_minutes_to_wait_on_disconnect,
peak_minutes_to_wait_on_logoff,
peak_start_time,
peak_start_vm_on_connect,
ramp_down_action_on_disconnect,
ramp_down_action_on_logoff,
ramp_down_minutes_to_wait_on_disconnect,
ramp_down_minutes_to_wait_on_logoff,
ramp_down_start_time,
ramp_down_start_vm_on_connect,
ramp_up_action_on_disconnect,
ramp_up_action_on_logoff,
ramp_up_auto_start_hosts,
ramp_up_minutes_to_wait_on_disconnect,
ramp_up_minutes_to_wait_on_logoff,
ramp_up_start_time,
ramp_up_start_vm_on_connect,
resourceGroupName,
scalingPlanName,
scalingPlanScheduleName,
subscriptionId
FROM azure.desktop_virtualization.vw_scaling_plan_personal_schedules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.desktop_virtualization.scaling_plan_personal_schedules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scaling_plan_personal_schedules</code> resource.

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
INSERT INTO azure.desktop_virtualization.scaling_plan_personal_schedules (
resourceGroupName,
scalingPlanName,
scalingPlanScheduleName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ scalingPlanName }}',
'{{ scalingPlanScheduleName }}',
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
        - name: daysOfWeek
          value:
            - string
        - name: rampUpStartTime
          value:
            - name: hour
              value: integer
            - name: minute
              value: integer
        - name: rampUpAutoStartHosts
          value: string
        - name: rampUpStartVMOnConnect
          value: string
        - name: rampUpActionOnDisconnect
          value: string
        - name: rampUpMinutesToWaitOnDisconnect
          value: integer
        - name: rampUpActionOnLogoff
          value: string
        - name: rampUpMinutesToWaitOnLogoff
          value: integer
        - name: peakStartVMOnConnect
          value: string
        - name: peakActionOnDisconnect
          value: string
        - name: peakMinutesToWaitOnDisconnect
          value: integer
        - name: peakActionOnLogoff
          value: string
        - name: peakMinutesToWaitOnLogoff
          value: integer
        - name: rampDownStartVMOnConnect
          value: string
        - name: rampDownActionOnDisconnect
          value: string
        - name: rampDownMinutesToWaitOnDisconnect
          value: integer
        - name: rampDownActionOnLogoff
          value: string
        - name: rampDownMinutesToWaitOnLogoff
          value: integer
        - name: offPeakStartVMOnConnect
          value: string
        - name: offPeakActionOnDisconnect
          value: string
        - name: offPeakMinutesToWaitOnDisconnect
          value: integer
        - name: offPeakActionOnLogoff
          value: string
        - name: offPeakMinutesToWaitOnLogoff
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>scaling_plan_personal_schedules</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.scaling_plan_personal_schedules
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND scalingPlanScheduleName = '{{ scalingPlanScheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>scaling_plan_personal_schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.scaling_plan_personal_schedules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND scalingPlanScheduleName = '{{ scalingPlanScheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

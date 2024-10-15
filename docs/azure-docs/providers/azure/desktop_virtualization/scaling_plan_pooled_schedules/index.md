---
title: scaling_plan_pooled_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_plan_pooled_schedules
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

Creates, updates, deletes, gets or lists a <code>scaling_plan_pooled_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_plan_pooled_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.scaling_plan_pooled_schedules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scaling_plan_pooled_schedules', value: 'view', },
        { label: 'scaling_plan_pooled_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="days_of_week" /> | `text` | field from the `properties` object |
| <CopyableCode code="off_peak_load_balancing_algorithm" /> | `text` | field from the `properties` object |
| <CopyableCode code="off_peak_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="peak_load_balancing_algorithm" /> | `text` | field from the `properties` object |
| <CopyableCode code="peak_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_capacity_threshold_pct" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_force_logoff_users" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_load_balancing_algorithm" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_minimum_hosts_pct" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_notification_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_stop_hosts_when" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_down_wait_time_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_capacity_threshold_pct" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_load_balancing_algorithm" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_minimum_hosts_pct" /> | `text` | field from the `properties` object |
| <CopyableCode code="ramp_up_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scalingPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scalingPlanScheduleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | A ScalingPlanPooledSchedule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId" /> | Get a ScalingPlanPooledSchedule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, scalingPlanName, subscriptionId" /> | List ScalingPlanPooledSchedules. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId, data__properties" /> | Create or update a ScalingPlanPooledSchedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId" /> | Remove a ScalingPlanPooledSchedule. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, scalingPlanName, scalingPlanScheduleName, subscriptionId" /> | Update a ScalingPlanPooledSchedule. |

## `SELECT` examples

List ScalingPlanPooledSchedules.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scaling_plan_pooled_schedules', value: 'view', },
        { label: 'scaling_plan_pooled_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
days_of_week,
off_peak_load_balancing_algorithm,
off_peak_start_time,
peak_load_balancing_algorithm,
peak_start_time,
ramp_down_capacity_threshold_pct,
ramp_down_force_logoff_users,
ramp_down_load_balancing_algorithm,
ramp_down_minimum_hosts_pct,
ramp_down_notification_message,
ramp_down_start_time,
ramp_down_stop_hosts_when,
ramp_down_wait_time_minutes,
ramp_up_capacity_threshold_pct,
ramp_up_load_balancing_algorithm,
ramp_up_minimum_hosts_pct,
ramp_up_start_time,
resourceGroupName,
scalingPlanName,
scalingPlanScheduleName,
subscriptionId,
system_data,
type
FROM azure.desktop_virtualization.vw_scaling_plan_pooled_schedules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.desktop_virtualization.scaling_plan_pooled_schedules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scaling_plan_pooled_schedules</code> resource.

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
INSERT INTO azure.desktop_virtualization.scaling_plan_pooled_schedules (
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
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
        - name: rampUpLoadBalancingAlgorithm
          value: string
        - name: rampUpMinimumHostsPct
          value: integer
        - name: rampUpCapacityThresholdPct
          value: integer
        - name: peakLoadBalancingAlgorithm
          value: string
        - name: rampDownLoadBalancingAlgorithm
          value: string
        - name: rampDownMinimumHostsPct
          value: integer
        - name: rampDownCapacityThresholdPct
          value: integer
        - name: rampDownForceLogoffUsers
          value: boolean
        - name: rampDownStopHostsWhen
          value: string
        - name: rampDownWaitTimeMinutes
          value: integer
        - name: rampDownNotificationMessage
          value: string
        - name: offPeakLoadBalancingAlgorithm
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>scaling_plan_pooled_schedules</code> resource.

```sql
/*+ update */
UPDATE azure.desktop_virtualization.scaling_plan_pooled_schedules
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND scalingPlanScheduleName = '{{ scalingPlanScheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>scaling_plan_pooled_schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.desktop_virtualization.scaling_plan_pooled_schedules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND scalingPlanName = '{{ scalingPlanName }}'
AND scalingPlanScheduleName = '{{ scalingPlanScheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

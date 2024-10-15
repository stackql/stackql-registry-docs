---
title: virtual_machine_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_schedules
  - dev_test_labs
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.virtual_machine_schedules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_schedules', value: 'view', },
        { label: 'virtual_machine_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="daily_recurrence" /> | `text` | field from the `properties` object |
| <CopyableCode code="hourly_recurrence" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="notification_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="target_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="task_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualMachineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="weekly_recurrence" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a schedule. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, virtualMachineName" /> | Get schedule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId, virtualMachineName" /> | List schedules in a given virtual machine. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, virtualMachineName, data__properties" /> | Create or replace an existing schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, virtualMachineName" /> | Delete schedule. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, virtualMachineName" /> | Allows modifying tags of schedules. All other properties will be ignored. |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, virtualMachineName" /> | Execute a schedule. This operation can take a while to complete. |

## `SELECT` examples

List schedules in a given virtual machine.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_schedules', value: 'view', },
        { label: 'virtual_machine_schedules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
created_date,
daily_recurrence,
hourly_recurrence,
labName,
location,
notification_settings,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
tags,
target_resource_id,
task_type,
time_zone_id,
type,
unique_identifier,
virtualMachineName,
weekly_recurrence
FROM azure.dev_test_labs.vw_virtual_machine_schedules
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.dev_test_labs.virtual_machine_schedules
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_schedules</code> resource.

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
INSERT INTO azure.dev_test_labs.virtual_machine_schedules (
labName,
name,
resourceGroupName,
subscriptionId,
virtualMachineName,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ labName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualMachineName }}',
'{{ data__properties }}',
'{{ location }}',
'{{ tags }}',
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
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: status
          value: string
        - name: taskType
          value: string
        - name: weeklyRecurrence
          value:
            - name: weekdays
              value:
                - string
            - name: time
              value: string
        - name: dailyRecurrence
          value:
            - name: time
              value: string
        - name: hourlyRecurrence
          value:
            - name: minute
              value: integer
        - name: timeZoneId
          value: string
        - name: notificationSettings
          value:
            - name: status
              value: string
            - name: timeInMinutes
              value: integer
            - name: webhookUrl
              value: string
            - name: emailRecipient
              value: string
            - name: notificationLocale
              value: string
        - name: createdDate
          value: string
        - name: targetResourceId
          value: string
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_schedules</code> resource.

```sql
/*+ update */
UPDATE azure.dev_test_labs.virtual_machine_schedules
SET 
tags = '{{ tags }}'
WHERE 
labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_test_labs.virtual_machine_schedules
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```

---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - lab_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.schedules" /></td></tr>
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
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="recurrence_pattern" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_operation_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="stop_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Schedule resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, scheduleName, subscriptionId" /> | Returns the properties of a lab Schedule. |
| <CopyableCode code="list_by_lab" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | Returns a list of all schedules for a lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, resourceGroupName, scheduleName, subscriptionId, data__properties" /> | Operation to create or update a lab schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, resourceGroupName, scheduleName, subscriptionId" /> | Operation to delete a schedule resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, resourceGroupName, scheduleName, subscriptionId" /> | Operation to update a lab schedule. |

## `SELECT` examples

Returns a list of all schedules for a lab.

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
labName,
notes,
provisioning_state,
recurrence_pattern,
resourceGroupName,
resource_operation_error,
scheduleName,
start_at,
stop_at,
subscriptionId,
system_data,
time_zone_id
FROM azure.lab_services.vw_schedules
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.lab_services.schedules
WHERE labName = '{{ labName }}'
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
INSERT INTO azure.lab_services.schedules (
labName,
resourceGroupName,
scheduleName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ labName }}',
'{{ resourceGroupName }}',
'{{ scheduleName }}',
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
        - name: startAt
          value: string
        - name: stopAt
          value: string
        - name: recurrencePattern
          value:
            - name: frequency
              value: []
            - name: weekDays
              value:
                - []
            - name: interval
              value: integer
            - name: expirationDate
              value: string
        - name: timeZoneId
          value: string
        - name: notes
          value: string
        - name: provisioningState
          value: []
        - name: resourceOperationError
          value:
            - name: timestamp
              value: string
            - name: code
              value: string
            - name: message
              value: string
            - name: action
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>schedules</code> resource.

```sql
/*+ update */
UPDATE azure.lab_services.schedules
SET 
properties = '{{ properties }}'
WHERE 
labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scheduleName = '{{ scheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.lab_services.schedules
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scheduleName = '{{ scheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

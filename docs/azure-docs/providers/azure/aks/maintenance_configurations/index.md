---
title: maintenance_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_configurations
  - aks
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

Creates, updates, deletes, gets or lists a <code>maintenance_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenance_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.maintenance_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_maintenance_configurations', value: 'view', },
        { label: 'maintenance_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="configName" /> | `text` | field from the `properties` object |
| <CopyableCode code="maintenance_window" /> | `text` | field from the `properties` object |
| <CopyableCode code="not_allowed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_in_week" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="properties" /> | `object` | Properties used to configure planned maintenance for a Managed Cluster. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="list_by_managed_cluster" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configName, resourceGroupName, resourceName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_maintenance_configurations', value: 'view', },
        { label: 'maintenance_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configName,
maintenance_window,
not_allowed_time,
resourceGroupName,
resourceName,
subscriptionId,
system_data,
time_in_week,
type
FROM azure.aks.vw_maintenance_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
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
FROM azure.aks.maintenance_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>maintenance_configurations</code> resource.

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
INSERT INTO azure.aks.maintenance_configurations (
configName,
resourceGroupName,
resourceName,
subscriptionId,
properties
)
SELECT 
'{{ configName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
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
        - name: timeInWeek
          value:
            - - name: day
                value: []
              - name: hourSlots
                value:
                  - []
        - name: notAllowedTime
          value:
            - - name: start
                value: string
              - name: end
                value: string
        - name: maintenanceWindow
          value:
            - name: schedule
              value:
                - name: daily
                  value:
                    - name: intervalDays
                      value: integer
                - name: weekly
                  value:
                    - name: intervalWeeks
                      value: integer
                - name: absoluteMonthly
                  value:
                    - name: intervalMonths
                      value: integer
                    - name: dayOfMonth
                      value: integer
                - name: relativeMonthly
                  value:
                    - name: intervalMonths
                      value: integer
                    - name: weekIndex
                      value: string
            - name: durationHours
              value: integer
            - name: utcOffset
              value: string
            - name: startDate
              value: string
            - name: startTime
              value: string
            - name: notAllowedDates
              value:
                - - name: start
                    value: string
                  - name: end
                    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>maintenance_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.aks.maintenance_configurations
WHERE configName = '{{ configName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

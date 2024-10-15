---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
  - dev_center
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.schedules" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="frequency" /> | `text` | field from the `properties` object |
| <CopyableCode code="poolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="time" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The Schedule properties defining when and what to execute. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="poolName, projectName, resourceGroupName, scheduleName, subscriptionId" /> | Gets a schedule resource. |
| <CopyableCode code="list_by_pool" /> | `SELECT` | <CopyableCode code="poolName, projectName, resourceGroupName, subscriptionId" /> | Lists schedules for a pool |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="poolName, projectName, resourceGroupName, scheduleName, subscriptionId" /> | Creates or updates a Schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="poolName, projectName, resourceGroupName, scheduleName, subscriptionId" /> | Deletes a Scheduled. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="poolName, projectName, resourceGroupName, scheduleName, subscriptionId" /> | Partially updates a Scheduled. |

## `SELECT` examples

Lists schedules for a pool

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
id,
name,
frequency,
poolName,
projectName,
provisioning_state,
resourceGroupName,
scheduleName,
state,
subscriptionId,
system_data,
time,
time_zone,
type
FROM azure.dev_center.vw_schedules
WHERE poolName = '{{ poolName }}'
AND projectName = '{{ projectName }}'
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
systemData,
type
FROM azure.dev_center.schedules
WHERE poolName = '{{ poolName }}'
AND projectName = '{{ projectName }}'
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
INSERT INTO azure.dev_center.schedules (
poolName,
projectName,
resourceGroupName,
scheduleName,
subscriptionId,
properties
)
SELECT 
'{{ poolName }}',
'{{ projectName }}',
'{{ resourceGroupName }}',
'{{ scheduleName }}',
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
        - name: type
          value: []
        - name: frequency
          value: []
        - name: time
          value: string
        - name: timeZone
          value: string
        - name: state
          value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>schedules</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.schedules
SET 
properties = '{{ properties }}'
WHERE 
poolName = '{{ poolName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scheduleName = '{{ scheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>schedules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.schedules
WHERE poolName = '{{ poolName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND scheduleName = '{{ scheduleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

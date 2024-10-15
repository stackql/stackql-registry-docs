---
title: snapshot_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_policies
  - netapp
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

Creates, updates, deletes, gets or lists a <code>snapshot_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshot_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.snapshot_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshot_policies', value: 'view', },
        { label: 'snapshot_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="daily_schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="hourly_schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="monthly_schedule" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshotPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="weekly_schedule" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Snapshot policy properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, snapshotPolicyName, subscriptionId" /> | Get a snapshot Policy |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List snapshot policy |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, snapshotPolicyName, subscriptionId, data__location, data__properties" /> | Create a snapshot policy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, snapshotPolicyName, subscriptionId" /> | Delete snapshot policy |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, snapshotPolicyName, subscriptionId" /> | Patch a snapshot policy |

## `SELECT` examples

List snapshot policy

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_snapshot_policies', value: 'view', },
        { label: 'snapshot_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
daily_schedule,
enabled,
etag,
hourly_schedule,
location,
monthly_schedule,
provisioning_state,
resourceGroupName,
snapshotPolicyName,
subscriptionId,
tags,
weekly_schedule
FROM azure_isv.netapp.vw_snapshot_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure_isv.netapp.snapshot_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>snapshot_policies</code> resource.

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
INSERT INTO azure_isv.netapp.snapshot_policies (
accountName,
resourceGroupName,
snapshotPolicyName,
subscriptionId,
data__location,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ snapshotPolicyName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: etag
      value: string
    - name: properties
      value:
        - name: hourlySchedule
          value:
            - name: snapshotsToKeep
              value: integer
            - name: minute
              value: integer
            - name: usedBytes
              value: integer
        - name: dailySchedule
          value:
            - name: snapshotsToKeep
              value: integer
            - name: hour
              value: integer
            - name: minute
              value: integer
            - name: usedBytes
              value: integer
        - name: weeklySchedule
          value:
            - name: snapshotsToKeep
              value: integer
            - name: day
              value: string
            - name: hour
              value: integer
            - name: minute
              value: integer
            - name: usedBytes
              value: integer
        - name: monthlySchedule
          value:
            - name: snapshotsToKeep
              value: integer
            - name: daysOfMonth
              value: string
            - name: hour
              value: integer
            - name: minute
              value: integer
            - name: usedBytes
              value: integer
        - name: enabled
          value: boolean
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>snapshot_policies</code> resource.

```sql
/*+ update */
UPDATE azure_isv.netapp.snapshot_policies
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND snapshotPolicyName = '{{ snapshotPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>snapshot_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.netapp.snapshot_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND snapshotPolicyName = '{{ snapshotPolicyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

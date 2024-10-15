---
title: update_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs
  - azure_stack_hci
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

Creates, updates, deletes, gets or lists a <code>update_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>update_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.update_runs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_runs', value: 'view', },
        { label: 'update_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_started" /> | `text` | field from the `properties` object |
| <CopyableCode code="updateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="updateRunName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of an Update run |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName, updateRunName" /> | Get the Update run for a specified update |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | List all Update runs for a specified update |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName, updateRunName" /> | Delete specified Update Run |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName, updateRunName" /> | Put Update runs for a specified update |

## `SELECT` examples

List all Update runs for a specified update

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_runs', value: 'view', },
        { label: 'update_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
clusterName,
duration,
last_updated_time,
location,
progress,
provisioning_state,
resourceGroupName,
state,
subscriptionId,
time_started,
updateName,
updateRunName
FROM azure_stack.azure_stack_hci.vw_update_runs
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateName = '{{ updateName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties
FROM azure_stack.azure_stack_hci.update_runs
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateName = '{{ updateName }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>update_runs</code> resource.

```sql
/*+ update */
REPLACE azure_stack.azure_stack_hci.update_runs
SET 
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateName = '{{ updateName }}'
AND updateRunName = '{{ updateRunName }}';
```

## `DELETE` example

Deletes the specified <code>update_runs</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack_hci.update_runs
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateName = '{{ updateName }}'
AND updateRunName = '{{ updateRunName }}';
```

---
title: update_runs_top_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs_top_levels
  - update_admin
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

Creates, updates, deletes, gets or lists a <code>update_runs_top_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>update_runs_top_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.update_admin.update_runs_top_levels" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_runs_top_levels', value: 'view', },
        { label: 'update_runs_top_levels', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Region location of resource. |
| <CopyableCode code="progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="time_started" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="updateLocation" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Region location of resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an update run. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, runName, subscriptionId, updateLocation" /> | Get an instance of update run using the ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, updateLocation" /> | Get the list of update runs. |

## `SELECT` examples

Get the list of update runs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_runs_top_levels', value: 'view', },
        { label: 'update_runs_top_levels', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
duration,
location,
progress,
resourceGroupName,
runName,
state,
subscriptionId,
tags,
time_started,
type,
updateLocation
FROM azure_stack.update_admin.vw_update_runs_top_levels
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateLocation = '{{ updateLocation }}';
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
FROM azure_stack.update_admin.update_runs_top_levels
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateLocation = '{{ updateLocation }}';
```
</TabItem></Tabs>


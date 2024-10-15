---
title: health_monitors_state_changes
hide_title: false
hide_table_of_contents: false
keywords:
  - health_monitors_state_changes
  - workload_monitor
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

Creates, updates, deletes, gets or lists a <code>health_monitors_state_changes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_monitors_state_changes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.workload_monitor.health_monitors_state_changes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_health_monitors_state_changes', value: 'view', },
        { label: 'health_monitors_state_changes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource Id. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="current_monitor_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_state_first_observed_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="evaluation_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="evidence" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorId" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitor_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitor_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitor_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitored_object" /> | `text` | field from the `properties` object |
| <CopyableCode code="previous_monitor_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="timestampUnix" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource Id. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | Properties of the monitor. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorId, providerName, resourceCollectionName, resourceGroupName, resourceName, subscriptionId, timestampUnix" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorId, providerName, resourceCollectionName, resourceGroupName, resourceName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_health_monitors_state_changes', value: 'view', },
        { label: 'health_monitors_state_changes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
current_monitor_state,
current_state_first_observed_timestamp,
evaluation_timestamp,
evidence,
monitorId,
monitor_configuration,
monitor_name,
monitor_type,
monitored_object,
previous_monitor_state,
providerName,
resourceCollectionName,
resourceGroupName,
resourceName,
subscriptionId,
timestampUnix,
type
FROM azure.workload_monitor.vw_health_monitors_state_changes
WHERE monitorId = '{{ monitorId }}'
AND providerName = '{{ providerName }}'
AND resourceCollectionName = '{{ resourceCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
type
FROM azure.workload_monitor.health_monitors_state_changes
WHERE monitorId = '{{ monitorId }}'
AND providerName = '{{ providerName }}'
AND resourceCollectionName = '{{ resourceCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


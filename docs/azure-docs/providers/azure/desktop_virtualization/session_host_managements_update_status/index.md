---
title: session_host_managements_update_status
hide_title: false
hide_table_of_contents: false
keywords:
  - session_host_managements_update_status
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

Creates, updates, deletes, gets or lists a <code>session_host_managements_update_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session_host_managements_update_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.session_host_managements_update_status" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_session_host_managements_update_status', value: 'view', },
        { label: 'session_host_managements_update_status', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified ID for the async operation. |
| <CopyableCode code="name" /> | `text` | Name of the async operation. |
| <CopyableCode code="correlation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | The error detail. |
| <CopyableCode code="hostPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="percent_complete" /> | `text` | field from the `properties` object |
| <CopyableCode code="progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scheduled_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="session_host_management" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | Operation status. Current defined values are < Error \| Scheduled \| UpdatingSessionHosts \| ValidatingSessionHostUpdate \| Paused \| Pausing \| Cancelling > \| Succeeded \| Failed \| Canceled |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID for the async operation. |
| <CopyableCode code="name" /> | `string` | Name of the async operation. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="percentComplete" /> | `number` | Percent of the operation that is complete. |
| <CopyableCode code="properties" /> | `object` | Properties bag to hold custom RP properties for sessionHostManagement Update Statuses. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | Operation status. Current defined values are < Error \| Scheduled \| UpdatingSessionHosts \| ValidatingSessionHostUpdate \| Paused \| Pausing \| Cancelling > \| Succeeded \| Failed \| Canceled |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Get the session host update status for a given hostpool. |

## `SELECT` examples

Get the session host update status for a given hostpool.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_session_host_managements_update_status', value: 'view', },
        { label: 'session_host_managements_update_status', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
correlation_id,
end_time,
error,
hostPoolName,
percent_complete,
progress,
resourceGroupName,
scheduled_date_time,
session_host_management,
start_time,
status,
subscriptionId
FROM azure.desktop_virtualization.vw_session_host_managements_update_status
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
endTime,
error,
percentComplete,
properties,
startTime,
status
FROM azure.desktop_virtualization.session_host_managements_update_status
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


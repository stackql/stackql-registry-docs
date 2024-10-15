---
title: devices_update_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_update_summaries
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>devices_update_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices_update_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.devices_update_summaries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_devices_update_summaries', value: 'view', },
        { label: 'devices_update_summaries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_last_scanned_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_progress_download_job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_progress_download_job_started_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_progress_install_job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_progress_install_job_started_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_progress_scan_started_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_completed_download_job_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_completed_install_job_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_completed_scan_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="reboot_required_for_install" /> | `text` | field from the `properties` object |
| <CopyableCode code="regular_updates_available" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_items_pending_for_download" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_items_pending_for_install" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Properties of the update profile |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Returns the update summary of the specified device name. |

## `SELECT` examples

Returns the update summary of the specified device name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_devices_update_summaries', value: 'view', },
        { label: 'devices_update_summaries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
deviceName,
device_last_scanned_time,
device_version,
in_progress_download_job_id,
in_progress_download_job_started_time,
in_progress_install_job_id,
in_progress_install_job_started_time,
in_progress_scan_started_time,
last_completed_download_job_time,
last_completed_install_job_time,
last_completed_scan_time,
managerName,
reboot_required_for_install,
regular_updates_available,
resourceGroupName,
status,
subscriptionId,
total_items_pending_for_download,
total_items_pending_for_install,
type
FROM azure_extras.storsimple_1200_series.vw_devices_update_summaries
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
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
type
FROM azure_extras.storsimple_1200_series.devices_update_summaries
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


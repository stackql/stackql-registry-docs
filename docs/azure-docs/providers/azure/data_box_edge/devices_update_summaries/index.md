---
title: devices_update_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_update_summaries
  - data_box_edge
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.devices_update_summaries" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The object name. |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_last_scanned_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_version_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_device_version_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_progress_download_job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_progress_download_job_started_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_progress_install_job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="in_progress_install_job_started_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_completed_download_job_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_completed_download_job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_completed_install_job_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_completed_install_job_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_completed_scan_job_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_download_job_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_install_job_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_install_job_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_scan_job_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="ongoing_update_operation" /> | `text` | field from the `properties` object |
| <CopyableCode code="reboot_behavior" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_number_of_updates_available" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_number_of_updates_pending_download" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_number_of_updates_pending_install" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_time_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_update_size_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="update_titles" /> | `text` | field from the `properties` object |
| <CopyableCode code="updates" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="properties" /> | `object` | The device update information summary. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



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
device_last_scanned_date_time,
device_version_number,
friendly_device_version_name,
in_progress_download_job_id,
in_progress_download_job_started_date_time,
in_progress_install_job_id,
in_progress_install_job_started_date_time,
last_completed_download_job_date_time,
last_completed_download_job_id,
last_completed_install_job_date_time,
last_completed_install_job_id,
last_completed_scan_job_date_time,
last_download_job_status,
last_install_job_status,
last_successful_install_job_date_time,
last_successful_scan_job_time,
ongoing_update_operation,
reboot_behavior,
resourceGroupName,
subscriptionId,
system_data,
total_number_of_updates_available,
total_number_of_updates_pending_download,
total_number_of_updates_pending_install,
total_time_in_minutes,
total_update_size_in_bytes,
type,
update_titles,
updates
FROM azure.data_box_edge.vw_devices_update_summaries
WHERE deviceName = '{{ deviceName }}'
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
FROM azure.data_box_edge.devices_update_summaries
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


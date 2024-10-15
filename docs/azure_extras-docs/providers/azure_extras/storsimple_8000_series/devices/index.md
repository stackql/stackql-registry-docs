---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.devices" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_devices', value: 'view', },
        { label: 'devices', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The name of the object. |
| <CopyableCode code="activation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="active_controller" /> | `text` | field from the `properties` object |
| <CopyableCode code="agent_group_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_local_storage_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_tiered_storage_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="culture" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_configuration_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_software_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_software_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_software_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="model_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_interface_card_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioned_local_storage_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioned_tiered_storage_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioned_volume_size_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rollover_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_iqn" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_tiered_storage_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
| <CopyableCode code="using_storage_in_bytes" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machine_api_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The properties of the StorSimple device. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified device. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Returns the list of devices for the specified manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the device. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Patches the device. |
| <CopyableCode code="authorize_for_service_encryption_key_rollover" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Authorizes the specified device for service data encryption key rollover. |
| <CopyableCode code="configure" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId, data__properties" /> | Complete minimal setup before using the device. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Deactivates the device. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, sourceDeviceName, subscriptionId" /> | Failovers a set of volume containers from a specified source device to a target device. |
| <CopyableCode code="install_updates" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Downloads and installs the updates on the device. |
| <CopyableCode code="scan_for_updates" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Scans for updates on the device. |

## `SELECT` examples

Returns the list of devices for the specified manager.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_devices', value: 'view', },
        { label: 'devices', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
activation_time,
active_controller,
agent_group_version,
available_local_storage_in_bytes,
available_tiered_storage_in_bytes,
culture,
details,
deviceName,
device_configuration_status,
device_description,
device_location,
device_software_version,
device_type,
friendly_name,
friendly_software_name,
friendly_software_version,
kind,
managerName,
model_description,
network_interface_card_count,
provisioned_local_storage_in_bytes,
provisioned_tiered_storage_in_bytes,
provisioned_volume_size_in_bytes,
resourceGroupName,
rollover_details,
serial_number,
status,
subscriptionId,
target_iqn,
total_tiered_storage_in_bytes,
type,
using_storage_in_bytes,
virtual_machine_api_type
FROM azure_extras.storsimple_8000_series.vw_devices
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure_extras.storsimple_8000_series.devices
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>devices</code> resource.

```sql
/*+ update */
UPDATE azure_extras.storsimple_8000_series.devices
SET 
properties = '{{ properties }}'
WHERE 
deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__properties = '{{ data__properties }}';
```

## `DELETE` example

Deletes the specified <code>devices</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_8000_series.devices
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

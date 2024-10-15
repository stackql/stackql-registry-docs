---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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

Creates, updates, deletes, gets or lists a <code>devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.devices" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | The identifier. |
| <CopyableCode code="name" /> | `text` | The name. |
| <CopyableCode code="activation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="allowed_device_operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="culture" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_configuration_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_software_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_software_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="managerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="model_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier. |
| <CopyableCode code="name" /> | `string` | The name. |
| <CopyableCode code="properties" /> | `object` | Encases all the properties of the Device |
| <CopyableCode code="type" /> | `string` | The type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified device name. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Retrieves all the devices in a manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Deletes the device. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Patches the device. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Deactivates the device. |
| <CopyableCode code="download_updates" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Downloads updates on the device. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Fails over the device to another device. |
| <CopyableCode code="install_updates" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Installs the updates on the device. |
| <CopyableCode code="scan_for_updates" /> | `EXEC` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Scans for updates on the device. |

## `SELECT` examples

Retrieves all the devices in a manager.

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
allowed_device_operations,
culture,
details,
deviceName,
device_capabilities,
device_configuration_status,
device_description,
device_software_version,
domain_name,
friendly_software_name,
managerName,
model_description,
resourceGroupName,
status,
subscriptionId,
type
FROM azure_extras.storsimple_1200_series.vw_devices
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
properties,
type
FROM azure_extras.storsimple_1200_series.devices
WHERE managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>devices</code> resource.

```sql
/*+ update */
UPDATE azure_extras.storsimple_1200_series.devices
SET 
deviceDescription = '{{ deviceDescription }}'
WHERE 
deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>devices</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.storsimple_1200_series.devices
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

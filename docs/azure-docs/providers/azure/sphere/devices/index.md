---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - sphere
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.devices" /></td></tr>
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
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="chip_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="device_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_available_os_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_installed_os_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_os_update_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_update_request_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="productName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of device |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId" /> | Get a Device. Use '.unassigned' or '.default' for the device group and product names when a device does not belong to a device group and product. |
| <CopyableCode code="list_by_device_group" /> | `SELECT` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | List Device resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId" /> | Create a Device. Use '.unassigned' or '.default' for the device group and product names to claim a device to the catalog only. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId" /> | Delete a Device |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId" /> | Update a Device. Use '.unassigned' or '.default' for the device group and product names to move a device to the catalog level. |
| <CopyableCode code="generate_capability_image" /> | `EXEC` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId, data__capabilities" /> | Generates the capability image for the device. Use '.unassigned' or '.default' for the device group and product names to generate the image for a device that does not belong to a specific device group and product. |

## `SELECT` examples

List Device resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.

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
catalogName,
chip_sku,
deviceGroupName,
deviceName,
device_id,
last_available_os_version,
last_installed_os_version,
last_os_update_utc,
last_update_request_utc,
productName,
provisioning_state,
resourceGroupName,
subscriptionId
FROM azure.sphere.vw_devices
WHERE catalogName = '{{ catalogName }}'
AND deviceGroupName = '{{ deviceGroupName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sphere.devices
WHERE catalogName = '{{ catalogName }}'
AND deviceGroupName = '{{ deviceGroupName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>devices</code> resource.

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
INSERT INTO azure.sphere.devices (
catalogName,
deviceGroupName,
deviceName,
productName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ catalogName }}',
'{{ deviceGroupName }}',
'{{ deviceName }}',
'{{ productName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: deviceId
          value: string
        - name: chipSku
          value: string
        - name: lastAvailableOsVersion
          value: string
        - name: lastInstalledOsVersion
          value: string
        - name: lastOsUpdateUtc
          value: string
        - name: lastUpdateRequestUtc
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>devices</code> resource.

```sql
/*+ update */
UPDATE azure.sphere.devices
SET 
properties = '{{ properties }}'
WHERE 
catalogName = '{{ catalogName }}'
AND deviceGroupName = '{{ deviceGroupName }}'
AND deviceName = '{{ deviceName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>devices</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sphere.devices
WHERE catalogName = '{{ catalogName }}'
AND deviceGroupName = '{{ deviceGroupName }}'
AND deviceName = '{{ deviceName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

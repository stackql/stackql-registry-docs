---
title: device_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - device_groups
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

Creates, updates, deletes, gets or lists a <code>device_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.device_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_device_groups', value: 'view', },
        { label: 'device_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_crash_dumps_collection" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalogName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_deployment" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_feed_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="productName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="regional_data_boundary" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="update_policy" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of deviceGroup |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Get a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | List DeviceGroup resources by Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Create a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Delete a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Update a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="claim_devices" /> | `EXEC` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId, data__deviceIdentifiers" /> | Bulk claims the devices. Use '.unassigned' or '.default' for the device group and product names when bulk claiming devices to a catalog only. |
| <CopyableCode code="count_devices" /> | `EXEC` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Counts devices in device group. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |

## `SELECT` examples

List DeviceGroup resources by Product. '.default' and '.unassigned' are system defined values and cannot be used for product name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_device_groups', value: 'view', },
        { label: 'device_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
allow_crash_dumps_collection,
catalogName,
deviceGroupName,
has_deployment,
os_feed_type,
productName,
provisioning_state,
regional_data_boundary,
resourceGroupName,
subscriptionId,
update_policy
FROM azure.sphere.vw_device_groups
WHERE catalogName = '{{ catalogName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sphere.device_groups
WHERE catalogName = '{{ catalogName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>device_groups</code> resource.

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
INSERT INTO azure.sphere.device_groups (
catalogName,
deviceGroupName,
productName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ catalogName }}',
'{{ deviceGroupName }}',
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
        - name: description
          value: string
        - name: osFeedType
          value: []
        - name: updatePolicy
          value: []
        - name: allowCrashDumpsCollection
          value: []
        - name: regionalDataBoundary
          value: []
        - name: hasDeployment
          value: boolean
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>device_groups</code> resource.

```sql
/*+ update */
UPDATE azure.sphere.device_groups
SET 
properties = '{{ properties }}'
WHERE 
catalogName = '{{ catalogName }}'
AND deviceGroupName = '{{ deviceGroupName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>device_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sphere.device_groups
WHERE catalogName = '{{ catalogName }}'
AND deviceGroupName = '{{ deviceGroupName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

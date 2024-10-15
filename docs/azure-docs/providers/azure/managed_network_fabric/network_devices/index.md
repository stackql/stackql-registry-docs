---
title: network_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - network_devices
  - managed_network_fabric
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

Creates, updates, deletes, gets or lists a <code>network_devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_devices" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_devices', value: 'view', },
        { label: 'network_devices', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="management_ipv4_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_ipv6_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkDeviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_device_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_device_sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_rack_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Device Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Gets the Network Device resource details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the Network Device resources in a given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the Network Device resources in a given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId, data__properties" /> | Create a Network Device resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Delete the Network Device resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network Device resource. |
| <CopyableCode code="reboot" /> | `EXEC` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Reboot the Network Device. |
| <CopyableCode code="refresh_configuration" /> | `EXEC` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Refreshes the configuration the Network Device. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="networkDeviceName, resourceGroupName, subscriptionId" /> | Upgrades the version of the Network Device. |

## `SELECT` examples

List all the Network Device resources in a given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_devices', value: 'view', },
        { label: 'network_devices', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
configuration_state,
host_name,
location,
management_ipv4_address,
management_ipv6_address,
networkDeviceName,
network_device_role,
network_device_sku,
network_rack_id,
provisioning_state,
resourceGroupName,
serial_number,
subscriptionId,
tags,
version
FROM azure.managed_network_fabric.vw_network_devices
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.network_devices
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_devices</code> resource.

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
INSERT INTO azure.managed_network_fabric.network_devices (
networkDeviceName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ networkDeviceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: annotation
          value: string
        - name: hostName
          value: string
        - name: serialNumber
          value: string
        - name: version
          value: string
        - name: networkDeviceSku
          value: string
        - name: networkDeviceRole
          value: string
        - name: networkRackId
          value: string
        - name: managementIpv4Address
          value: string
        - name: managementIpv6Address
          value: string
        - name: configurationState
          value: []
        - name: provisioningState
          value: []
        - name: administrativeState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_devices</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.network_devices
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
networkDeviceName = '{{ networkDeviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_devices</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.network_devices
WHERE networkDeviceName = '{{ networkDeviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

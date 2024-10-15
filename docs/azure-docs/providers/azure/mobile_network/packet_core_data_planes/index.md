---
title: packet_core_data_planes
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_core_data_planes
  - mobile_network
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

Creates, updates, deletes, gets or lists a <code>packet_core_data_planes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packet_core_data_planes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.packet_core_data_planes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packet_core_data_planes', value: 'view', },
        { label: 'packet_core_data_planes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="packetCoreControlPlaneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="packetCoreDataPlaneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_plane_access_interface" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_plane_access_virtual_ipv4_addresses" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Packet core data plane properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId" /> | Gets information about the specified packet core data plane. |
| <CopyableCode code="list_by_packet_core_control_plane" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Lists all the packet core data planes associated with a packet core control plane. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a packet core data plane. Must be created in the same location as its parent packet core control plane. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId" /> | Deletes the specified packet core data plane. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId" /> | Updates packet core data planes tags. |

## `SELECT` examples

Lists all the packet core data planes associated with a packet core control plane.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packet_core_data_planes', value: 'view', },
        { label: 'packet_core_data_planes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
packetCoreControlPlaneName,
packetCoreDataPlaneName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
user_plane_access_interface,
user_plane_access_virtual_ipv4_addresses
FROM azure.mobile_network.vw_packet_core_data_planes
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.mobile_network.packet_core_data_planes
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>packet_core_data_planes</code> resource.

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
INSERT INTO azure.mobile_network.packet_core_data_planes (
packetCoreControlPlaneName,
packetCoreDataPlaneName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ packetCoreControlPlaneName }}',
'{{ packetCoreDataPlaneName }}',
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
        - name: provisioningState
          value: []
        - name: userPlaneAccessInterface
          value:
            - name: name
              value: string
            - name: ipv4Address
              value: []
            - name: ipv4Subnet
              value: []
            - name: vlanId
              value: integer
            - name: ipv4AddressList
              value:
                - []
            - name: bfdIpv4Endpoints
              value:
                - []
        - name: userPlaneAccessVirtualIpv4Addresses
          value:
            - []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>packet_core_data_planes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.packet_core_data_planes
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND packetCoreDataPlaneName = '{{ packetCoreDataPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: attached_data_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_data_networks
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

Creates, updates, deletes, gets or lists a <code>attached_data_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attached_data_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.attached_data_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_attached_data_networks', value: 'view', },
        { label: 'attached_data_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attachedDataNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="napt_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="packetCoreControlPlaneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="packetCoreDataPlaneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_equipment_address_pool_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_equipment_static_address_pool_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_plane_data_interface" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Data network properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId" /> | Gets information about the specified attached data network. |
| <CopyableCode code="list_by_packet_core_data_plane" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId" /> | Gets all the attached data networks associated with a packet core data plane. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an attached data network. Must be created in the same location as its parent packet core data plane. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId" /> | Deletes the specified attached data network. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId" /> | Updates an attached data network tags. |

## `SELECT` examples

Gets all the attached data networks associated with a packet core data plane.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_attached_data_networks', value: 'view', },
        { label: 'attached_data_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
attachedDataNetworkName,
dns_addresses,
location,
napt_configuration,
packetCoreControlPlaneName,
packetCoreDataPlaneName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
user_equipment_address_pool_prefix,
user_equipment_static_address_pool_prefix,
user_plane_data_interface
FROM azure.mobile_network.vw_attached_data_networks
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND packetCoreDataPlaneName = '{{ packetCoreDataPlaneName }}'
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
FROM azure.mobile_network.attached_data_networks
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND packetCoreDataPlaneName = '{{ packetCoreDataPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>attached_data_networks</code> resource.

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
INSERT INTO azure.mobile_network.attached_data_networks (
attachedDataNetworkName,
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
'{{ attachedDataNetworkName }}',
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
        - name: userPlaneDataInterface
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
        - name: dnsAddresses
          value:
            - []
        - name: naptConfiguration
          value:
            - name: enabled
              value: []
            - name: portRange
              value:
                - name: minPort
                  value: integer
                - name: maxPort
                  value: integer
            - name: portReuseHoldTime
              value:
                - name: tcp
                  value: integer
                - name: udp
                  value: integer
            - name: pinholeLimits
              value: integer
            - name: pinholeTimeouts
              value:
                - name: tcp
                  value: integer
                - name: udp
                  value: integer
                - name: icmp
                  value: integer
        - name: userEquipmentAddressPoolPrefix
          value:
            - []
        - name: userEquipmentStaticAddressPoolPrefix
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

Deletes the specified <code>attached_data_networks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.attached_data_networks
WHERE attachedDataNetworkName = '{{ attachedDataNetworkName }}'
AND packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND packetCoreDataPlaneName = '{{ packetCoreDataPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: network_packet_brokers
hide_title: false
hide_table_of_contents: false
keywords:
  - network_packet_brokers
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

Creates, updates, deletes, gets or lists a <code>network_packet_brokers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_packet_brokers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_packet_brokers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_packet_brokers', value: 'view', },
        { label: 'network_packet_brokers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="neighbor_group_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkPacketBrokerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_device_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_tap_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_interface_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Packet Broker Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkPacketBrokerName, resourceGroupName, subscriptionId" /> | Retrieves details of this Network Packet Broker. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays NetworkPacketBrokers list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays Network Packet Brokers list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkPacketBrokerName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Network Packet Broker. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkPacketBrokerName, resourceGroupName, subscriptionId" /> | Deletes Network Packet Broker. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkPacketBrokerName, resourceGroupName, subscriptionId" /> | API to update certain properties of the Network Packet Broker resource. |

## `SELECT` examples

Displays Network Packet Brokers list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_packet_brokers', value: 'view', },
        { label: 'network_packet_brokers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
neighbor_group_ids,
networkPacketBrokerName,
network_device_ids,
network_fabric_id,
network_tap_ids,
provisioning_state,
resourceGroupName,
source_interface_ids,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_network_packet_brokers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.network_packet_brokers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_packet_brokers</code> resource.

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
INSERT INTO azure.managed_network_fabric.network_packet_brokers (
networkPacketBrokerName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ networkPacketBrokerName }}',
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
        - name: networkFabricId
          value: []
        - name: networkDeviceIds
          value:
            - []
        - name: sourceInterfaceIds
          value:
            - []
        - name: networkTapIds
          value:
            - []
        - name: neighborGroupIds
          value:
            - []
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>network_packet_brokers</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.network_packet_brokers
SET 
tags = '{{ tags }}'
WHERE 
networkPacketBrokerName = '{{ networkPacketBrokerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_packet_brokers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.network_packet_brokers
WHERE networkPacketBrokerName = '{{ networkPacketBrokerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

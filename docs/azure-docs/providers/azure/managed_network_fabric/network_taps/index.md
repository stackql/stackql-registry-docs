---
title: network_taps
hide_title: false
hide_table_of_contents: false
keywords:
  - network_taps
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

Creates, updates, deletes, gets or lists a <code>network_taps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_taps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_taps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_taps', value: 'view', },
        { label: 'network_taps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrative_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotation" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="destinations" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="networkTapName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_packet_broker_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="polling_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_tap_rule_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Tap Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId" /> | Retrieves details of this Network Tap. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays Network Taps list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays Network Taps list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Network Tap. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId" /> | Deletes Network Tap. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId" /> | API to update certain properties of the Network Tap resource. |
| <CopyableCode code="resync" /> | `EXEC` | <CopyableCode code="networkTapName, resourceGroupName, subscriptionId" /> | Implements the operation to the underlying resources. |

## `SELECT` examples

Displays Network Taps list by subscription GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_network_taps', value: 'view', },
        { label: 'network_taps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrative_state,
annotation,
configuration_state,
destinations,
location,
networkTapName,
network_packet_broker_id,
polling_type,
provisioning_state,
resourceGroupName,
source_tap_rule_id,
subscriptionId,
tags
FROM azure.managed_network_fabric.vw_network_taps
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_network_fabric.network_taps
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_taps</code> resource.

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
INSERT INTO azure.managed_network_fabric.network_taps (
networkTapName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ networkTapName }}',
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
        - name: networkPacketBrokerId
          value: []
        - name: sourceTapRuleId
          value: string
        - name: destinations
          value:
            - object
        - name: pollingType
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

Updates a <code>network_taps</code> resource.

```sql
/*+ update */
UPDATE azure.managed_network_fabric.network_taps
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
networkTapName = '{{ networkTapName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>network_taps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network_fabric.network_taps
WHERE networkTapName = '{{ networkTapName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

---
title: packet_captures
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_captures
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

Creates, updates, deletes, gets or lists a <code>packet_captures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packet_captures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.packet_captures" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packet_captures', value: 'view', },
        { label: 'packet_captures', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bytes_to_capture_per_packet" /> | `text` | field from the `properties` object |
| <CopyableCode code="capture_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_interfaces" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_files" /> | `text` | field from the `properties` object |
| <CopyableCode code="packetCaptureName" /> | `text` | field from the `properties` object |
| <CopyableCode code="packetCoreControlPlaneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_limit_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_bytes_per_session" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Packet capture session properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="packetCaptureName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Gets information about the specified packet capture session. |
| <CopyableCode code="list_by_packet_core_control_plane" /> | `SELECT` | <CopyableCode code="packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Lists all the packet capture sessions under a packet core control plane. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="packetCaptureName, packetCoreControlPlaneName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a packet capture. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="packetCaptureName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Deletes the specified packet capture. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="packetCaptureName, packetCoreControlPlaneName, resourceGroupName, subscriptionId" /> | Stop a packet capture session. |

## `SELECT` examples

Lists all the packet capture sessions under a packet core control plane.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_packet_captures', value: 'view', },
        { label: 'packet_captures', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
bytes_to_capture_per_packet,
capture_start_time,
network_interfaces,
output_files,
packetCaptureName,
packetCoreControlPlaneName,
provisioning_state,
reason,
resourceGroupName,
status,
subscriptionId,
time_limit_in_seconds,
total_bytes_per_session
FROM azure.mobile_network.vw_packet_captures
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.mobile_network.packet_captures
WHERE packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>packet_captures</code> resource.

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
INSERT INTO azure.mobile_network.packet_captures (
packetCaptureName,
packetCoreControlPlaneName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ packetCaptureName }}',
'{{ packetCoreControlPlaneName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: provisioningState
          value: []
        - name: status
          value: string
        - name: reason
          value: string
        - name: captureStartTime
          value: string
        - name: networkInterfaces
          value:
            - string
        - name: bytesToCapturePerPacket
          value: integer
        - name: totalBytesPerSession
          value: integer
        - name: timeLimitInSeconds
          value: integer
        - name: outputFiles
          value:
            - string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>packet_captures</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.packet_captures
WHERE packetCaptureName = '{{ packetCaptureName }}'
AND packetCoreControlPlaneName = '{{ packetCoreControlPlaneName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

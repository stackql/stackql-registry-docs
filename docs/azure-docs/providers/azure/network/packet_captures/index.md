---
title: packet_captures
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_captures
  - network
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.packet_captures" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | ID of the packet capture operation. |
| <CopyableCode code="name" /> | `text` | Name of the packet capture session. |
| <CopyableCode code="bytes_to_capture_per_packet" /> | `text` | field from the `properties` object |
| <CopyableCode code="capture_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="continuous_capture" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="filters" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkWatcherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="packetCaptureName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_limit_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_bytes_per_session" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the packet capture operation. |
| <CopyableCode code="name" /> | `string` | Name of the packet capture session. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | The properties of a packet capture session. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId" /> | Gets a packet capture session by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | Lists all packet capture sessions within the specified resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId, data__properties" /> | Create and start a packet capture on the specified VM. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId" /> | Deletes the specified packet capture session. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId" /> | Stops a specified packet capture session. |

## `SELECT` examples

Lists all packet capture sessions within the specified resource group.

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
id,
name,
bytes_to_capture_per_packet,
capture_settings,
continuous_capture,
etag,
filters,
networkWatcherName,
packetCaptureName,
provisioning_state,
resourceGroupName,
scope,
storage_location,
subscriptionId,
target,
target_type,
time_limit_in_seconds,
total_bytes_per_session
FROM azure.network.vw_packet_captures
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties
FROM azure.network.packet_captures
WHERE networkWatcherName = '{{ networkWatcherName }}'
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
INSERT INTO azure.network.packet_captures (
networkWatcherName,
packetCaptureName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ networkWatcherName }}',
'{{ packetCaptureName }}',
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
        - name: target
          value: string
        - name: scope
          value:
            - name: include
              value:
                - string
            - name: exclude
              value:
                - string
        - name: targetType
          value: string
        - name: bytesToCapturePerPacket
          value: integer
        - name: totalBytesPerSession
          value: integer
        - name: timeLimitInSeconds
          value: integer
        - name: storageLocation
          value:
            - name: storageId
              value: string
            - name: storagePath
              value: string
            - name: filePath
              value: string
            - name: localPath
              value: string
        - name: filters
          value:
            - - name: protocol
                value: string
              - name: localIPAddress
                value: string
              - name: remoteIPAddress
                value: string
              - name: localPort
                value: string
              - name: remotePort
                value: string
        - name: continuousCapture
          value: boolean
        - name: captureSettings
          value:
            - name: fileCount
              value: integer
            - name: fileSizeInBytes
              value: integer
            - name: sessionTimeLimitInSeconds
              value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>packet_captures</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.packet_captures
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND packetCaptureName = '{{ packetCaptureName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

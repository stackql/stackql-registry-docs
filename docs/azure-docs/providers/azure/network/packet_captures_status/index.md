---
title: packet_captures_status
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_captures_status
  - network
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packet_captures_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.packet_captures_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the packet capture resource. |
| `name` | `string` | The name of the packet capture resource. |
| `captureStartTime` | `string` | The start time of the packet capture session. |
| `packetCaptureError` | `array` | List of errors of packet capture session. |
| `packetCaptureStatus` | `string` | The status of the packet capture session. |
| `stopReason` | `string` | The reason the current packet capture session was stopped. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId` |

---
title: packet_captures_status
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_captures_status
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

Creates, updates, deletes, gets or lists a <code>packet_captures_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>packet_captures_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.packet_captures_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the packet capture resource. |
| <CopyableCode code="name" /> | `string` | The name of the packet capture resource. |
| <CopyableCode code="captureStartTime" /> | `string` | The start time of the packet capture session. |
| <CopyableCode code="packetCaptureError" /> | `array` | List of errors of packet capture session. |
| <CopyableCode code="packetCaptureStatus" /> | `string` | The status of the packet capture session. |
| <CopyableCode code="stopReason" /> | `string` | The reason the current packet capture session was stopped. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId" /> | Query the status of a running packet capture session. |

## `SELECT` examples

Query the status of a running packet capture session.


```sql
SELECT
id,
name,
captureStartTime,
packetCaptureError,
packetCaptureStatus,
stopReason
FROM azure.network.packet_captures_status
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND packetCaptureName = '{{ packetCaptureName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
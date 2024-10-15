---
title: live_events_get_stream_events
hide_title: false
hide_table_of_contents: false
keywords:
  - live_events_get_stream_events
  - media_services
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

Creates, updates, deletes, gets or lists a <code>live_events_get_stream_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_events_get_stream_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.live_events_get_stream_events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` | The live event stream event data. |
| <CopyableCode code="eventLevel" /> | `string` | Event level. |
| <CopyableCode code="eventTime" /> | `string` | The time event raised. |
| <CopyableCode code="eventType" /> | `string` | The type of the stream event. Format: StreamEvent/{eventType} |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, liveEventName, resourceGroupName, subscriptionId" /> | Get stream events telemetry of a live event. |

## `SELECT` examples

Get stream events telemetry of a live event.


```sql
SELECT
data,
eventLevel,
eventTime,
eventType
FROM azure.media_services.live_events_get_stream_events
WHERE accountName = '{{ accountName }}'
AND liveEventName = '{{ liveEventName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
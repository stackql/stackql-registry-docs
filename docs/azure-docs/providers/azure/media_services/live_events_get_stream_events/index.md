---
title: live_events_get_stream_events
hide_title: false
hide_table_of_contents: false
keywords:
  - live_events_get_stream_events
  - media_services
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




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
| <CopyableCode code="eventType" /> | `string` | The type of the stream event. Format: StreamEvent/&#123;eventType&#125; |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> |

---
title: live_events_get_status
hide_title: false
hide_table_of_contents: false
keywords:
  - live_events_get_status
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
<tr><td><b>Name</b></td><td><code>live_events_get_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.live_events_get_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="healthDescriptions" /> | `array` | List of strings justifying the health status. |
| <CopyableCode code="healthStatus" /> | `string` | Health status of last 20 seconds. |
| <CopyableCode code="ingestion" /> | `object` | The live event ingestion telemetry data. |
| <CopyableCode code="lastUpdatedTime" /> | `string` | Last updated UTC time of this status. |
| <CopyableCode code="state" /> | `string` | Current state of the live event. See https://go.microsoft.com/fwlink/?linkid=2139012 for more information. |
| <CopyableCode code="trackStatus" /> | `array` | Track entry list. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, liveEventName, resourceGroupName, subscriptionId" /> |

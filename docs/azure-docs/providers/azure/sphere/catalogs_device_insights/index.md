---
title: catalogs_device_insights
hide_title: false
hide_table_of_contents: false
keywords:
  - catalogs_device_insights
  - sphere
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
<tr><td><b>Name</b></td><td><code>catalogs_device_insights</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.catalogs_device_insights" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Event description |
| <CopyableCode code="deviceId" /> | `string` | Device ID |
| <CopyableCode code="endTimestampUtc" /> | `string` | Event end timestamp |
| <CopyableCode code="eventCategory" /> | `string` | Event category |
| <CopyableCode code="eventClass" /> | `string` | Event class |
| <CopyableCode code="eventCount" /> | `integer` | Event count |
| <CopyableCode code="eventType" /> | `string` | Event type |
| <CopyableCode code="startTimestampUtc" /> | `string` | Event start timestamp |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> |

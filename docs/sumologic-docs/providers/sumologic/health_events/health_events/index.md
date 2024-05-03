---
title: health_events
hide_title: false
hide_table_of_contents: false
keywords:
  - health_events
  - health_events
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.health_events.health_events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="details" /> | `object` |  |
| <CopyableCode code="eventId" /> | `string` | The unique identifier of the event. |
| <CopyableCode code="eventName" /> | `string` | The name of the event. |
| <CopyableCode code="eventTime" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="resourceIdentity" /> | `object` |  |
| <CopyableCode code="severityLevel" /> | `string` | The criticality of the event. It is either `Error` or `Warning` |
| <CopyableCode code="subsystem" /> | `string` | The product area of the event. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="listAllHealthEvents" /> | `SELECT` | <CopyableCode code="region" /> |

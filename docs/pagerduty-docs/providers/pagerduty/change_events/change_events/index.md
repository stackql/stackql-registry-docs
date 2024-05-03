---
title: change_events
hide_title: false
hide_table_of_contents: false
keywords:
  - change_events
  - change_events
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>change_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.change_events.change_events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="_summary" /> | `string` | A brief text summary of the event. Displayed in PagerDuty to provide information about the change. The maximum permitted length of this property is 1024 characters. |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="custom_details" /> | `object` | Additional details about the change event. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="images" /> | `array` |  |
| <CopyableCode code="integration" /> | `` |  |
| <CopyableCode code="links" /> | `array` | List of links to include. |
| <CopyableCode code="routing_key" /> | `string` | This is the 32 character Integration Key for an Integration on a Service. The same Integration Key can be used for both alert and change events. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="services" /> | `array` | An array containing Service objects that this change event is associated with. |
| <CopyableCode code="source" /> | `string` | The unique name of the location where the Change Event occurred. |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="timestamp" /> | `string` | The time at which the emitting tool detected or generated the event. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_change_event" /> | `SELECT` | <CopyableCode code="id" /> | Get details about an existing Change Event.<br /><br />Scoped OAuth requires: `change_events.read`<br /> |
| <CopyableCode code="list_change_events" /> | `SELECT` |  | List all of the existing Change Events.<br /><br />Scoped OAuth requires: `change_events.read`<br /> |
| <CopyableCode code="create_change_event" /> | `INSERT` |  | Sending Change Events is documented as part of the V2 Events API. See [`Send Change Event`](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODI2Ng-send-change-events-to-the-pager-duty-events-api).<br /> |
| <CopyableCode code="_get_change_event" /> | `EXEC` | <CopyableCode code="id" /> | Get details about an existing Change Event.<br /><br />Scoped OAuth requires: `change_events.read`<br /> |
| <CopyableCode code="_list_change_events" /> | `EXEC` |  | List all of the existing Change Events.<br /><br />Scoped OAuth requires: `change_events.read`<br /> |
| <CopyableCode code="update_change_event" /> | `EXEC` | <CopyableCode code="id, data__change_event" /> | Update an existing Change Event<br /><br />Scoped OAuth requires: `change_events.write`<br /> |

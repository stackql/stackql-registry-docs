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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>change_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.change_events.change_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `_summary` | `string` | A brief text summary of the event. Displayed in PagerDuty to provide information about the change. The maximum permitted length of this property is 1024 characters. |
| `_type` | `string` | The type of object being created. |
| `custom_details` | `object` | Additional details about the change event. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `images` | `array` |  |
| `integration` | `` |  |
| `links` | `array` | List of links to include. |
| `routing_key` | `string` | This is the 32 character Integration Key for an Integration on a Service. The same Integration Key can be used for both alert and change events. |
| `self` | `string` | the API show URL at which the object is accessible |
| `services` | `array` | An array containing Service objects that this change event is associated with. |
| `source` | `string` | The unique name of the location where the Change Event occurred. |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `timestamp` | `string` | The time at which the emitting tool detected or generated the event. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_change_event` | `SELECT` | `id` | Get details about an existing Change Event.<br /><br />Scoped OAuth requires: `change_events.read`<br /> |
| `list_change_events` | `SELECT` |  | List all of the existing Change Events.<br /><br />Scoped OAuth requires: `change_events.read`<br /> |
| `create_change_event` | `INSERT` |  | Sending Change Events is documented as part of the V2 Events API. See [`Send Change Event`](https://developer.pagerduty.com/api-reference/b3A6Mjc0ODI2Ng-send-change-events-to-the-pager-duty-events-api).<br /> |
| `_get_change_event` | `EXEC` | `id` | Get details about an existing Change Event.<br /><br />Scoped OAuth requires: `change_events.read`<br /> |
| `_list_change_events` | `EXEC` |  | List all of the existing Change Events.<br /><br />Scoped OAuth requires: `change_events.read`<br /> |
| `update_change_event` | `EXEC` | `id, data__change_event` | Update an existing Change Event<br /><br />Scoped OAuth requires: `change_events.write`<br /> |

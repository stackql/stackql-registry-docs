---
title: field_values
hide_title: false
hide_table_of_contents: false
keywords:
  - field_values
  - incidents
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
<tr><td><b>Name</b></td><td><code>field_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.incidents.field_values</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the field. |
| `name` | `string` | The name of the field. May include ASCII characters, specifically lowercase letters, digits, and underescores. The `name` for a Field must be unique. |
| `description` | `string` | A description of the data this field contains. |
| `datatype` | `string` | The kind of data the custom field is allowed to contain. |
| `display_name` | `string` | The human-readable name of the field. This must be unique across an account. |
| `fixed_options` | `boolean` | If `true`, restricts the values allowed to be stored in the custom field to a limited set of options (configured via the Field Option sub-resource). Must be `false` if `datatype` is "boolean", "url", or "datetime" |
| `multi_value` | `boolean` | If `true`, allows the custom field to store a set of multiple values. Must be `false` if `datatype` is not "string" or "url" |
| `type` | `string` | Determines the type of the reference. |
| `value` | `` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_field_values` | `SELECT` | `X-EARLY-ACCESS, id` | Get field values for an incident<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_get_incident_field_values` | `EXEC` | `X-EARLY-ACCESS, id` | Get field values for an incident<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `set_incident_field_values` | `EXEC` | `id, data__field_values` | Set field values for an incident<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

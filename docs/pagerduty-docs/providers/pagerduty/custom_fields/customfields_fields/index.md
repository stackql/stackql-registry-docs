---
title: customfields_fields
hide_title: false
hide_table_of_contents: false
keywords:
  - customfields_fields
  - custom_fields
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
<tr><td><b>Name</b></td><td><code>customfields_fields</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.custom_fields.customfields_fields</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `description` | `string` | A description of the data this field contains. |
| `created_at` | `string` | The date/time the object was created at. |
| `datatype` | `string` | The kind of data the custom field is allowed to contain. |
| `display_name` | `string` | The human-readable name of the field. This must be unique across an account. |
| `field_options` | `array` | The fixed list of value options that may be stored in this field. |
| `fixed_options` | `boolean` | If `true`, restricts the values allowed to be stored in the custom field to a limited set of options (configured via the Field Option sub-resource). Must be `false` if `datatype` is "boolean", "url", or "datetime" |
| `multi_value` | `boolean` | If `true`, allows the custom field to store a set of multiple values. Must be `false` if `datatype` is not "string" or "url" |
| `self` | `string` | The API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `type` | `string` |  |
| `updated_at` | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_custom_fields_field` | `SELECT` | `X-EARLY-ACCESS, field_id` | Show detailed information about a field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `list_custom_fields_fields` | `SELECT` | `X-EARLY-ACCESS` | List fields.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `create_custom_fields_field` | `INSERT` | `X-EARLY-ACCESS, data__field` | Create a new Field, along with the Field Options if provided. An account may have up to 1000 Fields.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `delete_custom_fields_field` | `DELETE` | `X-EARLY-ACCESS, field_id` | Delete a Field. Fields may not be deleted if they are used by a Field Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_get_custom_fields_field` | `EXEC` | `X-EARLY-ACCESS, field_id` | Show detailed information about a field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_list_custom_fields_fields` | `EXEC` | `X-EARLY-ACCESS` | List fields.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `update_custom_fields_field` | `EXEC` | `X-EARLY-ACCESS, field_id, data__field` | Update a field.<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

---
title: customfields_fields_field_options
hide_title: false
hide_table_of_contents: false
keywords:
  - customfields_fields_field_options
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
<tr><td><b>Name</b></td><td><code>customfields_fields_field_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.custom_fields.customfields_fields_field_options</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `created_at` | `string` | The date/time the object was created at. |
| `data` | `` |  |
| `type` | `string` |  |
| `updated_at` | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_custom_fields_field_option` | `SELECT` | `X-EARLY-ACCESS, field_id, field_option_id` | Get a Field Option.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `list_custom_fields_field_options` | `SELECT` | `X-EARLY-ACCESS, field_id` | List all enabled Field Options for a Field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `create_custom_fields_field_option` | `INSERT` | `X-EARLY-ACCESS, field_id, data__field_option` | Create a new Field Option. Field Options may only be created for Fields where `fixed_options` is `true`. A Field may have no more than 10 enabled options.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `delete_custom_fields_field_option` | `DELETE` | `X-EARLY-ACCESS, field_id, field_option_id` | Delete a Field Option.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_get_custom_fields_field_option` | `EXEC` | `X-EARLY-ACCESS, field_id, field_option_id` | Get a Field Option.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_list_custom_fields_field_options` | `EXEC` | `X-EARLY-ACCESS, field_id` | List all enabled Field Options for a Field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `update_custom_fields_field_option` | `EXEC` | `X-EARLY-ACCESS, field_id, field_option_id, data__field_option` | Update Field Option for a Field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

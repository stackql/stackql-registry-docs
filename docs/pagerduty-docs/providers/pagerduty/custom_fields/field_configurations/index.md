---
title: field_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - field_configurations
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
<tr><td><b>Name</b></td><td><code>field_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.custom_fields.field_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `_type` | `string` |  |
| `created_at` | `string` | The date/time the object was created at. |
| `default_value` | `object` | The value to use for this field if none is provided. It must be specified if `required` is `true`. |
| `field` | `` | The Field to be included in this schema. Each Field may only be used in one Field Configuration per schema. |
| `required` | `boolean` | If `true`, this Field must always have a value set for objects using this schema. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `updated_at` | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_custom_fields_field_configuration` | `SELECT` | `X-EARLY-ACCESS, field_configuration_id, schema_id` | Show detailed information about a Field Configuration.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `list_custom_fields_field_configurations` | `SELECT` | `X-EARLY-ACCESS, schema_id` | List all Field Configurations for the given Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `create_custom_fields_field_configuration` | `INSERT` | `X-EARLY-ACCESS, schema_id, data__field_configuration` | Add a new Field Configuration to an existing Schema. A Schema may use at most 20 Fields, and so may have at most 20 Field Configurations.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `delete_custom_fields_field_configuration` | `DELETE` | `X-EARLY-ACCESS, field_configuration_id, schema_id` | Remove a Field Configuration and its associated Field from a Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_get_custom_fields_field_configuration` | `EXEC` | `X-EARLY-ACCESS, field_configuration_id, schema_id` | Show detailed information about a Field Configuration.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_list_custom_fields_field_configurations` | `EXEC` | `X-EARLY-ACCESS, schema_id` | List all Field Configurations for the given Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `update_custom_fields_field_configuration` | `EXEC` | `X-EARLY-ACCESS, field_configuration_id, schema_id, data__field_configuration` | Update settings for Field Configuration in Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

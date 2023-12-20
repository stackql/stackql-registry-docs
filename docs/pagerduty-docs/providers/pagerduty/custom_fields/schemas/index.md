---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
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
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.custom_fields.schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `description` | `string` | A description of this schema. |
| `created_at` | `string` | The date/time the object was created at. |
| `field_configurations` | `array` |  |
| `self` | `string` | The API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `title` | `string` | The name of the schema. |
| `type` | `string` |  |
| `updated_at` | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_custom_fields_schema` | `SELECT` | `X-EARLY-ACCESS, schema_id` | Get detailed information about a Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `list_custom_fields_schemas` | `SELECT` | `X-EARLY-ACCESS` | List all Schemas.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `create_custom_fields_schema` | `INSERT` | `X-EARLY-ACCESS, data__schema` | Create a new Schema, along with the Field Configurations if provided. An account may have up to 100 Schemas.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `delete_custom_fields_schema` | `DELETE` | `X-EARLY-ACCESS, schema_id` | Delete a Schema. Schemas may not be deleted if they are in use by any Service.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_get_custom_fields_schema` | `EXEC` | `X-EARLY-ACCESS, schema_id` | Get detailed information about a Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_list_custom_fields_schemas` | `EXEC` | `X-EARLY-ACCESS` | List all Schemas.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `update_custom_fields_schema` | `EXEC` | `X-EARLY-ACCESS, schema_id, data__schema` | Update a Schema, along with the Field Configurations if provided.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

---
title: schema_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_assignments
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
<tr><td><b>Name</b></td><td><code>schema_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.custom_fields.schema_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `created_at` | `string` | The date/time the object was created at. |
| `schema` | `object` |  |
| `service` | `object` |  |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `updated_at` | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_schema_assignments` | `SELECT` | `X-EARLY-ACCESS, filter` | List Schema Assignments by `service_id` or `schema_id`<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `create_custom_fields_schema_assignment` | `INSERT` | `X-EARLY-ACCESS, data__schema_assignment` | Assign a new Schema to a service<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `delete_schema_assignment` | `DELETE` | `X-EARLY-ACCESS, id` | Remove the Schema assigned to a service<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| `_list_schema_assignments` | `EXEC` | `X-EARLY-ACCESS, filter` | List Schema Assignments by `service_id` or `schema_id`<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

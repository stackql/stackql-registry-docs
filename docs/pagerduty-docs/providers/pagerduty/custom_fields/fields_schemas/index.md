---
title: fields_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - fields_schemas
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
<tr><td><b>Name</b></td><td><code>fields_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.custom_fields.fields_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `description` | `string` | A description of this schema. |
| `created_at` | `string` | The date/time the object was created at. |
| `self` | `string` | The API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `title` | `string` | The name of the schema. |
| `type` | `string` |  |
| `updated_at` | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_custom_fields_schemas_using_field` | `SELECT` | `X-EARLY-ACCESS, field_id` |
| `_list_custom_fields_schemas_using_field` | `EXEC` | `X-EARLY-ACCESS, field_id` |

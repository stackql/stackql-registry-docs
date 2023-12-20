---
title: templates
hide_title: false
hide_table_of_contents: false
keywords:
  - templates
  - templates
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
<tr><td><b>Name</b></td><td><code>templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.templates.templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The name of the template |
| `description` | `string` | Description of the template |
| `created_by` | `` | User/Account object reference of the creator |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `self` | `string` | the API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `template_type` | `string` | The type of template (`status_update` is the only supported template at this time) |
| `templated_fields` | `object` |  |
| `type` | `string` |  |
| `updated_by` | `` | User/Account object reference of the updator |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_template` | `SELECT` | `id` | Get a single template on the account<br /><br />Scoped OAuth requires: `templates.read`<br /> |
| `get_templates` | `SELECT` |  | Get a list of all the template on an account<br /><br />Scoped OAuth requires: `templates.read`<br /> |
| `create_template` | `INSERT` | `data__template` | Create a new template<br /><br />Scoped OAuth requires: `templates.write`<br /> |
| `delete_template` | `DELETE` | `id` | Delete a specific of templates on the account<br /><br />Scoped OAuth requires: `templates.write`<br /> |
| `_get_template` | `EXEC` | `id` | Get a single template on the account<br /><br />Scoped OAuth requires: `templates.read`<br /> |
| `_get_templates` | `EXEC` |  | Get a list of all the template on an account<br /><br />Scoped OAuth requires: `templates.read`<br /> |
| `render_template` | `EXEC` | `id` | Render a template. This endpoint has a variable request body depending on the template type. For the `status_update` template type, the caller will provide the incident id, and a status update message.<br /><br />Scoped OAuth requires: `templates.read`<br /> |
| `update_template` | `EXEC` | `id, data__template` | Update an existing template<br /><br />Scoped OAuth requires: `templates.write`<br /> |

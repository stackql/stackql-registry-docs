---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - tags
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
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.tags.tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `_type` | `string` | The type of object being created. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `label` | `string` | The label of the tag. |
| `self` | `string` | the API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_entity_type_by_id_tags` | `SELECT` | `entity_type, id` | Get related tags for Users, Teams or Escalation Policies.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| `get_tag` | `SELECT` | `id` | Get details about an existing Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| `get_tags_by_entity_type` | `SELECT` | `entity_type, id` | Get related Users, Teams or Escalation Policies for the Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| `list_tags` | `SELECT` |  | List all of your account's tags.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| `create_entity_type_by_id_change_tags` | `INSERT` | `entity_type, id` | Assign existing or new tags.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.write`<br /> |
| `create_tags` | `INSERT` | `data__tag` | Create a Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.write`<br /> |
| `delete_tag` | `DELETE` | `id` | Remove an existing Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.write`<br /> |
| `_get_entity_type_by_id_tags` | `EXEC` | `entity_type, id` | Get related tags for Users, Teams or Escalation Policies.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| `_get_tag` | `EXEC` | `id` | Get details about an existing Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| `_get_tags_by_entity_type` | `EXEC` | `entity_type, id` | Get related Users, Teams or Escalation Policies for the Tag.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |
| `_list_tags` | `EXEC` |  | List all of your account's tags.<br /><br />A Tag is applied to Escalation Policies, Teams or Users and can be used to filter them.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#tags)<br /><br />Scoped OAuth requires: `tags.read`<br /> |

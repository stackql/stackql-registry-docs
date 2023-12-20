---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - extensions
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.extensions.extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The name of the extension. |
| `_type` | `string` | The type of object being created. |
| `config` | `object` | The object that contains extension configuration values depending on the extension schema specification. |
| `endpoint_url` | `string` | The url of the extension. |
| `extension_objects` | `array` | The objects for which the extension applies |
| `extension_schema` | `object` |  |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `self` | `string` | the API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `temporarily_disabled` | `boolean` | Whether or not this extension is temporarily disabled; for example, a webhook extension that is repeatedly rejected by the server. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_extension` | `SELECT` | `id` | Get details about an existing extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.read`<br /> |
| `list_extensions` | `SELECT` |  | List existing extensions.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.read`<br /> |
| `create_extension` | `INSERT` | `data__extension` | Create a new Extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.write`<br /> |
| `delete_extension` | `DELETE` | `id` | Delete an existing extension.<br /><br />Once the extension is deleted, it will not be accessible from the web UI and new incidents won't be able to be created for this extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.write`<br /> |
| `_get_extension` | `EXEC` | `id` | Get details about an existing extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.read`<br /> |
| `_list_extensions` | `EXEC` |  | List existing extensions.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.read`<br /> |
| `enable_extension` | `EXEC` | `id` | Enable an extension that is temporarily disabled. (This API does not require a request body.)<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.write`<br /> |
| `update_extension` | `EXEC` | `id, data__extension` | Update an existing extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.write`<br /> |

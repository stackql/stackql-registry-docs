---
title: addons
hide_title: false
hide_table_of_contents: false
keywords:
  - addons
  - add_ons
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
<tr><td><b>Name</b></td><td><code>addons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.add_ons.addons</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The name of the Add-on. |
| `_type` | `string` | The type of Add-on. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `self` | `string` | the API show URL at which the object is accessible |
| `src` | `string` | The source URL to display in a frame in the PagerDuty UI. HTTPS is required. |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_addon` | `SELECT` | `id` | Get details about an existing Add-on.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.read`<br /> |
| `list_addon` | `SELECT` |  | List all of the Add-ons installed on your account.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.read`<br /> |
| `create_addon` | `INSERT` | `data__addon` | Install an Add-on for your account.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />Given a configuration containing a `src` parameter, that URL will be embedded in an `iframe` on a page that's available to users from a drop-down menu.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.write`<br /> |
| `delete_addon` | `DELETE` | `id` | Remove an existing Add-on.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.write`<br /> |
| `_get_addon` | `EXEC` | `id` | Get details about an existing Add-on.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.read`<br /> |
| `_list_addon` | `EXEC` |  | List all of the Add-ons installed on your account.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.read`<br /> |
| `update_addon` | `EXEC` | `id, data__addon` | Update an existing Add-on.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />Given a configuration containing a `src` parameter, that URL will be embedded in an `iframe` on a page that's available to users from a drop-down menu.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.write`<br /> |

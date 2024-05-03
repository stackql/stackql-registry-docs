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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addons</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.add_ons.addons" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of the Add-on. |
| <CopyableCode code="_type" /> | `string` | The type of Add-on. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="src" /> | `string` | The source URL to display in a frame in the PagerDuty UI. HTTPS is required. |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_addon" /> | `SELECT` | <CopyableCode code="id" /> | Get details about an existing Add-on.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.read`<br /> |
| <CopyableCode code="list_addon" /> | `SELECT` |  | List all of the Add-ons installed on your account.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.read`<br /> |
| <CopyableCode code="create_addon" /> | `INSERT` | <CopyableCode code="data__addon" /> | Install an Add-on for your account.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />Given a configuration containing a `src` parameter, that URL will be embedded in an `iframe` on a page that's available to users from a drop-down menu.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.write`<br /> |
| <CopyableCode code="delete_addon" /> | `DELETE` | <CopyableCode code="id" /> | Remove an existing Add-on.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.write`<br /> |
| <CopyableCode code="_get_addon" /> | `EXEC` | <CopyableCode code="id" /> | Get details about an existing Add-on.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.read`<br /> |
| <CopyableCode code="_list_addon" /> | `EXEC` |  | List all of the Add-ons installed on your account.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.read`<br /> |
| <CopyableCode code="update_addon" /> | `EXEC` | <CopyableCode code="id, data__addon" /> | Update an existing Add-on.<br /><br />Addon's are pieces of functionality that developers can write to insert new functionality into PagerDuty's UI.<br /><br />Given a configuration containing a `src` parameter, that URL will be embedded in an `iframe` on a page that's available to users from a drop-down menu.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#add-ons)<br /><br />Scoped OAuth requires: `addons.write`<br /> |

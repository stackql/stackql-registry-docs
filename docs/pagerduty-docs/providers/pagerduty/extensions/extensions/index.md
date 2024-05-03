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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.extensions.extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of the extension. |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="config" /> | `object` | The object that contains extension configuration values depending on the extension schema specification. |
| <CopyableCode code="endpoint_url" /> | `string` | The url of the extension. |
| <CopyableCode code="extension_objects" /> | `array` | The objects for which the extension applies |
| <CopyableCode code="extension_schema" /> | `object` |  |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="temporarily_disabled" /> | `boolean` | Whether or not this extension is temporarily disabled; for example, a webhook extension that is repeatedly rejected by the server. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_extension" /> | `SELECT` | <CopyableCode code="id" /> | Get details about an existing extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.read`<br /> |
| <CopyableCode code="list_extensions" /> | `SELECT` |  | List existing extensions.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.read`<br /> |
| <CopyableCode code="create_extension" /> | `INSERT` | <CopyableCode code="data__extension" /> | Create a new Extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.write`<br /> |
| <CopyableCode code="delete_extension" /> | `DELETE` | <CopyableCode code="id" /> | Delete an existing extension.<br /><br />Once the extension is deleted, it will not be accessible from the web UI and new incidents won't be able to be created for this extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.write`<br /> |
| <CopyableCode code="_get_extension" /> | `EXEC` | <CopyableCode code="id" /> | Get details about an existing extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.read`<br /> |
| <CopyableCode code="_list_extensions" /> | `EXEC` |  | List existing extensions.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.read`<br /> |
| <CopyableCode code="enable_extension" /> | `EXEC` | <CopyableCode code="id" /> | Enable an extension that is temporarily disabled. (This API does not require a request body.)<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.write`<br /> |
| <CopyableCode code="update_extension" /> | `EXEC` | <CopyableCode code="id, data__extension" /> | Update an existing extension.<br /><br />Extensions are representations of Extension Schema objects that are attached to Services.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#extensions)<br /><br />Scoped OAuth requires: `extensions.write`<br /> |

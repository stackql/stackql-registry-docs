---
title: customfields_fields
hide_title: false
hide_table_of_contents: false
keywords:
  - customfields_fields
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customfields_fields</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.custom_fields.customfields_fields" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="description" /> | `string` | A description of the data this field contains. |
| <CopyableCode code="created_at" /> | `string` | The date/time the object was created at. |
| <CopyableCode code="datatype" /> | `string` | The kind of data the custom field is allowed to contain. |
| <CopyableCode code="display_name" /> | `string` | The human-readable name of the field. This must be unique across an account. |
| <CopyableCode code="field_options" /> | `array` | The fixed list of value options that may be stored in this field. |
| <CopyableCode code="fixed_options" /> | `boolean` | If `true`, restricts the values allowed to be stored in the custom field to a limited set of options (configured via the Field Option sub-resource). Must be `false` if `datatype` is "boolean", "url", or "datetime" |
| <CopyableCode code="multi_value" /> | `boolean` | If `true`, allows the custom field to store a set of multiple values. Must be `false` if `datatype` is not "string" or "url" |
| <CopyableCode code="self" /> | `string` | The API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_custom_fields_field" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, field_id" /> | Show detailed information about a field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="list_custom_fields_fields" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS" /> | List fields.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="create_custom_fields_field" /> | `INSERT` | <CopyableCode code="X-EARLY-ACCESS, data__field" /> | Create a new Field, along with the Field Options if provided. An account may have up to 1000 Fields.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="delete_custom_fields_field" /> | `DELETE` | <CopyableCode code="X-EARLY-ACCESS, field_id" /> | Delete a Field. Fields may not be deleted if they are used by a Field Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="_get_custom_fields_field" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, field_id" /> | Show detailed information about a field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="_list_custom_fields_fields" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS" /> | List fields.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="update_custom_fields_field" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, field_id, data__field" /> | Update a field.<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

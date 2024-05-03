---
title: customfields_fields_field_options
hide_title: false
hide_table_of_contents: false
keywords:
  - customfields_fields_field_options
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
<tr><td><b>Name</b></td><td><code>customfields_fields_field_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.custom_fields.customfields_fields_field_options" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="created_at" /> | `string` | The date/time the object was created at. |
| <CopyableCode code="data" /> | `` |  |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_custom_fields_field_option" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, field_id, field_option_id" /> | Get a Field Option.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="list_custom_fields_field_options" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, field_id" /> | List all enabled Field Options for a Field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="create_custom_fields_field_option" /> | `INSERT` | <CopyableCode code="X-EARLY-ACCESS, field_id, data__field_option" /> | Create a new Field Option. Field Options may only be created for Fields where `fixed_options` is `true`. A Field may have no more than 10 enabled options.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="delete_custom_fields_field_option" /> | `DELETE` | <CopyableCode code="X-EARLY-ACCESS, field_id, field_option_id" /> | Delete a Field Option.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="_get_custom_fields_field_option" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, field_id, field_option_id" /> | Get a Field Option.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="_list_custom_fields_field_options" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, field_id" /> | List all enabled Field Options for a Field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="update_custom_fields_field_option" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, field_id, field_option_id, data__field_option" /> | Update Field Option for a Field.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

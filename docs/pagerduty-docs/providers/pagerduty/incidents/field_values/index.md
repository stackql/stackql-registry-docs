---
title: field_values
hide_title: false
hide_table_of_contents: false
keywords:
  - field_values
  - incidents
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
<tr><td><b>Name</b></td><td><code>field_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.incidents.field_values" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the field. |
| <CopyableCode code="name" /> | `string` | The name of the field. May include ASCII characters, specifically lowercase letters, digits, and underescores. The `name` for a Field must be unique. |
| <CopyableCode code="description" /> | `string` | A description of the data this field contains. |
| <CopyableCode code="datatype" /> | `string` | The kind of data the custom field is allowed to contain. |
| <CopyableCode code="display_name" /> | `string` | The human-readable name of the field. This must be unique across an account. |
| <CopyableCode code="fixed_options" /> | `boolean` | If `true`, restricts the values allowed to be stored in the custom field to a limited set of options (configured via the Field Option sub-resource). Must be `false` if `datatype` is "boolean", "url", or "datetime" |
| <CopyableCode code="multi_value" /> | `boolean` | If `true`, allows the custom field to store a set of multiple values. Must be `false` if `datatype` is not "string" or "url" |
| <CopyableCode code="type" /> | `string` | Determines the type of the reference. |
| <CopyableCode code="value" /> | `` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_incident_field_values" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, id" /> | Get field values for an incident<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="_get_incident_field_values" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, id" /> | Get field values for an incident<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="set_incident_field_values" /> | `EXEC` | <CopyableCode code="id, data__field_values" /> | Set field values for an incident<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

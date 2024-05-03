---
title: field_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - field_configurations
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
<tr><td><b>Name</b></td><td><code>field_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.custom_fields.field_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` | The date/time the object was created at. |
| <CopyableCode code="default_value" /> | `object` | The value to use for this field if none is provided. It must be specified if `required` is `true`. |
| <CopyableCode code="field" /> | `` | The Field to be included in this schema. Each Field may only be used in one Field Configuration per schema. |
| <CopyableCode code="required" /> | `boolean` | If `true`, this Field must always have a value set for objects using this schema. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="updated_at" /> | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_custom_fields_field_configuration" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, field_configuration_id, schema_id" /> | Show detailed information about a Field Configuration.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="list_custom_fields_field_configurations" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, schema_id" /> | List all Field Configurations for the given Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="create_custom_fields_field_configuration" /> | `INSERT` | <CopyableCode code="X-EARLY-ACCESS, schema_id, data__field_configuration" /> | Add a new Field Configuration to an existing Schema. A Schema may use at most 20 Fields, and so may have at most 20 Field Configurations.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="delete_custom_fields_field_configuration" /> | `DELETE` | <CopyableCode code="X-EARLY-ACCESS, field_configuration_id, schema_id" /> | Remove a Field Configuration and its associated Field from a Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="_get_custom_fields_field_configuration" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, field_configuration_id, schema_id" /> | Show detailed information about a Field Configuration.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="_list_custom_fields_field_configurations" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, schema_id" /> | List all Field Configurations for the given Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="update_custom_fields_field_configuration" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, field_configuration_id, schema_id, data__field_configuration" /> | Update settings for Field Configuration in Schema.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

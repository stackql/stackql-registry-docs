---
title: schema_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_assignments
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
<tr><td><b>Name</b></td><td><code>schema_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.custom_fields.schema_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="created_at" /> | `string` | The date/time the object was created at. |
| <CopyableCode code="schema" /> | `object` |  |
| <CopyableCode code="service" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="updated_at" /> | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_schema_assignments" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, filter" /> | List Schema Assignments by `service_id` or `schema_id`<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="create_custom_fields_schema_assignment" /> | `INSERT` | <CopyableCode code="X-EARLY-ACCESS, data__schema_assignment" /> | Assign a new Schema to a service<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="delete_schema_assignment" /> | `DELETE` | <CopyableCode code="X-EARLY-ACCESS, id" /> | Remove the Schema assigned to a service<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |
| <CopyableCode code="_list_schema_assignments" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, filter" /> | List Schema Assignments by `service_id` or `schema_id`<br /><br />&lt;!-- theme: warning --&gt;<br /><br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /> |

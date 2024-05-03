---
title: fields_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - fields_schemas
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
<tr><td><b>Name</b></td><td><code>fields_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.custom_fields.fields_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="description" /> | `string` | A description of this schema. |
| <CopyableCode code="created_at" /> | `string` | The date/time the object was created at. |
| <CopyableCode code="self" /> | `string` | The API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="title" /> | `string` | The name of the schema. |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` | The date/time the object was last updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_custom_fields_schemas_using_field" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, field_id" /> |
| <CopyableCode code="_list_custom_fields_schemas_using_field" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, field_id" /> |

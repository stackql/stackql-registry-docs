---
title: builtin
hide_title: false
hide_table_of_contents: false
keywords:
  - builtin
  - fields
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>builtin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.fields.builtin" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataType" /> | `string` | Field type. Possible values are `String`, `Long`, `Int`, `Double`, and `Boolean`. |
| <CopyableCode code="fieldId" /> | `string` | Identifier of the field. |
| <CopyableCode code="fieldName" /> | `string` | Field name. |
| <CopyableCode code="state" /> | `string` | Indicates whether the field is enabled and its values are being accepted. Possible values are `Enabled` and `Disabled`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getBuiltInField" /> | `SELECT` | <CopyableCode code="id, region" /> | Get the details of a built-in field. |
| <CopyableCode code="listBuiltInFields" /> | `SELECT` | <CopyableCode code="region" /> | Built-in fields are created automatically by Sumo Logic for standard configuration purposes. They include `_sourceHost` and `_sourceCategory`. Built-in fields can't be deleted or disabled. |

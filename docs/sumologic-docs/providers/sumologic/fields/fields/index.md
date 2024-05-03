---
title: fields
hide_title: false
hide_table_of_contents: false
keywords:
  - fields
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
<tr><td><b>Name</b></td><td><code>fields</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.fields.fields" /></td></tr>
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
| <CopyableCode code="getCustomField" /> | `SELECT` | <CopyableCode code="id, region" /> | Get the details of a custom field. |
| <CopyableCode code="listCustomFields" /> | `SELECT` | <CopyableCode code="region" /> | Request a list of all the custom fields configured in your account. |
| <CopyableCode code="createField" /> | `INSERT` | <CopyableCode code="data__fieldName, region" /> | Adding a field will define it in the Fields schema allowing it to be assigned as metadata to your logs. |
| <CopyableCode code="deleteField" /> | `DELETE` | <CopyableCode code="id, region" /> | Deleting a field does not delete historical data assigned with that field. If you  delete a field by mistake and one or more of those dependencies break, you can  re-add the field to get things working properly again. You should always disable  a field and ensure things are behaving as expected before deleting a field. |

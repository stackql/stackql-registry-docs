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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fields</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.fields.fields</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `fieldId` | `string` | Identifier of the field. |
| `state` | `string` | Indicates whether the field is enabled and its values are being accepted. Possible values are `Enabled` and `Disabled`. |
| `fieldName` | `string` | Field name. |
| `dataType` | `string` | Field type. Possible values are `String`, `Long`, `Int`, `Double`, and `Boolean`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getCustomField` | `SELECT` | `id, region` | Get the details of a custom field. |
| `listCustomFields` | `SELECT` | `region` | Request a list of all the custom fields configured in your account. |
| `createField` | `INSERT` | `data__fieldName, region` | Adding a field will define it in the Fields schema allowing it to be assigned as metadata to your logs. |
| `deleteField` | `DELETE` | `id, region` | Deleting a field does not delete historical data assigned with that field. If you  delete a field by mistake and one or more of those dependencies break, you can  re-add the field to get things working properly again. You should always disable  a field and ensure things are behaving as expected before deleting a field. |

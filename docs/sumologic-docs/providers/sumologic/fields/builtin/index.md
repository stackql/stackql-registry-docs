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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>builtin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.fields.builtin</code></td></tr>
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
| `getBuiltInField` | `SELECT` | `id, region` | Get the details of a built-in field. |
| `listBuiltInFields` | `SELECT` | `region` | Built-in fields are created automatically by Sumo Logic for standard configuration purposes. They include `_sourceHost` and `_sourceCategory`. Built-in fields can't be deleted or disabled. |

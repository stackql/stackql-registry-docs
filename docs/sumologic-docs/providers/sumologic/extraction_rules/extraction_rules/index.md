---
title: extraction_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - extraction_rules
  - extraction_rules
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
<tr><td><b>Name</b></td><td><code>extraction_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.extraction_rules.extraction_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the field extraction rule. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `fieldNames` | `array` | List of extracted fields from "parseExpression". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getExtractionRule` | `SELECT` | `id` | Get a field extraction rule with the given identifier. |
| `listExtractionRules` | `SELECT` |  | Get a list of all field extraction rules. The response is paginated with a default limit of 100 field extraction rules per page. |
| `createExtractionRule` | `INSERT` |  | Create a new field extraction rule. |
| `deleteExtractionRule` | `DELETE` | `id` | Delete a field extraction rule with the given identifier. |
| `updateExtractionRule` | `EXEC` | `id` | Update an existing field extraction rule. All properties specified in the request are replaced. Missing properties are set to their default values. |

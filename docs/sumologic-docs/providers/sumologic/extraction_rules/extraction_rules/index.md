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
| `name` | `string` | Name of the field extraction rule. Use a name that makes it easy to identify the rule. |
| `fieldNames` | `array` | List of extracted fields from "parseExpression". |
| `parseExpression` | `string` | Describes the fields to be parsed. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `enabled` | `boolean` | Is the field extraction rule enabled. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `scope` | `string` | Scope of the field extraction rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( \| ). You'll use the Scope to run a search against the rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getExtractionRule` | `SELECT` | `id` | Get a field extraction rule with the given identifier. |
| `listExtractionRules` | `SELECT` |  | Get a list of all field extraction rules. The response is paginated with a default limit of 100 field extraction rules per page. |
| `createExtractionRule` | `INSERT` |  | Create a new field extraction rule. |
| `deleteExtractionRule` | `DELETE` | `id` | Delete a field extraction rule with the given identifier. |
| `updateExtractionRule` | `EXEC` | `id` | Update an existing field extraction rule. All properties specified in the request are replaced. Missing properties are set to their default values. |

---
title: transformation_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - transformation_rules
  - transformation_rules
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
<tr><td><b>Name</b></td><td><code>transformation_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.transformation_rules.transformation_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the transformation rule. |
| `ruleDefinition` | `object` | The properties that define a transformation rule. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `enabled` | `boolean` | True if the rule is enabled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getTransformationRule` | `SELECT` | `id` | Get a transformation rule with the given identifier. |
| `getTransformationRules` | `SELECT` |  | Get a list of transformation rules in the organization. The response is paginated with a default limit of 100 rules per page. |
| `createRule` | `INSERT` | `data__enabled, data__ruleDefinition` | Create a new transformation rule. |
| `deleteRule` | `DELETE` | `id` | Delete a transformation rule with the given identifier. |
| `updateTransformationRule` | `EXEC` | `id, data__enabled, data__ruleDefinition` | Update an existing transformation rule. All properties specified in the request are replaced. Missing properties will remain the same. |

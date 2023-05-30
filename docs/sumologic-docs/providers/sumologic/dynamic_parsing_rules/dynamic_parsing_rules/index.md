---
title: dynamic_parsing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - dynamic_parsing_rules
  - dynamic_parsing_rules
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
<tr><td><b>Name</b></td><td><code>dynamic_parsing_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.dynamic_parsing_rules.dynamic_parsing_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the dynamic parsing rule. |
| `name` | `string` | Name of the dynamic parsing rule. Use a name that makes it easy to identify the rule. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `isSystemRule` | `boolean` | Whether the rule has been defined by the system, rather than by a user. |
| `enabled` | `boolean` | Is the dynamic parsing rule enabled. |
| `scope` | `string` | Scope of the dynamic parsing rule. This could be a sourceCategory, sourceHost, or any other metadata that describes the data you want to extract from. Think of the Scope as the first portion of an ad hoc search, before the first pipe ( \| ). You'll use the Scope to run a search against the rule. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDynamicParsingRule` | `SELECT` | `id, region` | Get a dynamic parsing rule with the given identifier. |
| `listDynamicParsingRules` | `SELECT` | `region` | Get a list of all dynamic parsing rules. The response is paginated with a default limit of 100 dynamic parsing rules per page. |
| `createDynamicParsingRule` | `INSERT` | `data__enabled, data__name, data__scope, region` | Create a new dynamic parsing rule. |
| `deleteDynamicParsingRule` | `DELETE` | `id, region` | Delete a dynamic parsing rule with the given identifier. |
| `updateDynamicParsingRule` | `EXEC` | `id, data__enabled, data__name, data__scope, region` | Update an existing dynamic parsing rule. All properties specified in the request are replaced. Missing properties are set to their default values. |

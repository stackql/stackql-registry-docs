---
title: security_monitoring_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_monitoring_rules
  - security_monitoring
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_monitoring_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.security_monitoring.security_monitoring_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the rule. |
| `name` | `string` | The name of the rule. |
| `SecurityMonitoringSignalRuleResponse_cases` | `array` | Cases for generating signals. |
| `SecurityMonitoringSignalRuleResponse_createdAt` | `integer` | When the rule was created, timestamp in milliseconds. |
| `SecurityMonitoringSignalRuleResponse_creationAuthorId` | `integer` | User ID of the user who created the rule. |
| `SecurityMonitoringSignalRuleResponse_deprecationDate` | `integer` | When the rule will be deprecated, timestamp in milliseconds. |
| `SecurityMonitoringSignalRuleResponse_filters` | `array` | Additional queries to filter matched events before they are processed. |
| `SecurityMonitoringSignalRuleResponse_hasExtendedTitle` | `boolean` | Whether the notifications include the triggering group-by values in their title. |
| `SecurityMonitoringSignalRuleResponse_id` | `string` | The ID of the rule. |
| `SecurityMonitoringSignalRuleResponse_isDefault` | `boolean` | Whether the rule is included by default. |
| `SecurityMonitoringSignalRuleResponse_isDeleted` | `boolean` | Whether the rule has been deleted. |
| `SecurityMonitoringSignalRuleResponse_isEnabled` | `boolean` | Whether the rule is enabled. |
| `SecurityMonitoringSignalRuleResponse_message` | `string` | Message for generated signals. |
| `SecurityMonitoringSignalRuleResponse_name` | `string` | The name of the rule. |
| `SecurityMonitoringSignalRuleResponse_options` | `object` | Options on rules. |
| `SecurityMonitoringSignalRuleResponse_queries` | `array` | Queries for selecting logs which are part of the rule. |
| `SecurityMonitoringSignalRuleResponse_tags` | `array` | Tags for generated signals. |
| `SecurityMonitoringSignalRuleResponse_type` | `string` | The rule type. |
| `SecurityMonitoringSignalRuleResponse_updateAuthorId` | `integer` | User ID of the user who updated the rule. |
| `SecurityMonitoringSignalRuleResponse_version` | `integer` | The version of the rule. |
| `cases` | `array` | Cases for generating signals. |
| `complianceSignalOptions` | `object` | How to generate compliance signals. Useful for cloud_configuration rules only. |
| `createdAt` | `integer` | When the rule was created, timestamp in milliseconds. |
| `creationAuthorId` | `integer` | User ID of the user who created the rule. |
| `deprecationDate` | `integer` | When the rule will be deprecated, timestamp in milliseconds. |
| `filters` | `array` | Additional queries to filter matched events before they are processed. |
| `hasExtendedTitle` | `boolean` | Whether the notifications include the triggering group-by values in their title. |
| `isDefault` | `boolean` | Whether the rule is included by default. |
| `isDeleted` | `boolean` | Whether the rule has been deleted. |
| `isEnabled` | `boolean` | Whether the rule is enabled. |
| `message` | `string` | Message for generated signals. |
| `options` | `object` | Options on rules. |
| `queries` | `array` | Queries for selecting logs which are part of the rule. |
| `tags` | `array` | Tags for generated signals. |
| `type` | `string` | The rule type. |
| `updateAuthorId` | `integer` | User ID of the user who updated the rule. |
| `version` | `integer` | The version of the rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_security_monitoring_rule` | `SELECT` | `rule_id, dd_site` | Get a rule's details. |
| `list_security_monitoring_rules` | `SELECT` | `dd_site` | List rules. |
| `create_security_monitoring_rule` | `INSERT` | `dd_site` | Create a detection rule. |
| `delete_security_monitoring_rule` | `DELETE` | `rule_id, dd_site` | Delete an existing rule. Default rules cannot be deleted. |
| `update_security_monitoring_rule` | `EXEC` | `rule_id, dd_site` | Update an existing rule. When updating `cases`, `queries` or `options`, the whole field<br />must be included. For example, when modifying a query all queries must be included.<br />Default rules can only be updated to be enabled and to change notifications. |

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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_monitoring_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.security_monitoring.security_monitoring_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the rule. |
| <CopyableCode code="name" /> | `string` | The name of the rule. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_cases" /> | `array` | Cases for generating signals. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_createdAt" /> | `integer` | When the rule was created, timestamp in milliseconds. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_creationAuthorId" /> | `integer` | User ID of the user who created the rule. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_deprecationDate" /> | `integer` | When the rule will be deprecated, timestamp in milliseconds. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_filters" /> | `array` | Additional queries to filter matched events before they are processed. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_hasExtendedTitle" /> | `boolean` | Whether the notifications include the triggering group-by values in their title. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_id" /> | `string` | The ID of the rule. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_isDefault" /> | `boolean` | Whether the rule is included by default. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_isDeleted" /> | `boolean` | Whether the rule has been deleted. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_isEnabled" /> | `boolean` | Whether the rule is enabled. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_message" /> | `string` | Message for generated signals. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_name" /> | `string` | The name of the rule. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_options" /> | `object` | Options on rules. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_queries" /> | `array` | Queries for selecting logs which are part of the rule. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_tags" /> | `array` | Tags for generated signals. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_type" /> | `string` | The rule type. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_updateAuthorId" /> | `integer` | User ID of the user who updated the rule. |
| <CopyableCode code="SecurityMonitoringSignalRuleResponse_version" /> | `integer` | The version of the rule. |
| <CopyableCode code="cases" /> | `array` | Cases for generating signals. |
| <CopyableCode code="complianceSignalOptions" /> | `object` | How to generate compliance signals. Useful for cloud_configuration rules only. |
| <CopyableCode code="createdAt" /> | `integer` | When the rule was created, timestamp in milliseconds. |
| <CopyableCode code="creationAuthorId" /> | `integer` | User ID of the user who created the rule. |
| <CopyableCode code="deprecationDate" /> | `integer` | When the rule will be deprecated, timestamp in milliseconds. |
| <CopyableCode code="filters" /> | `array` | Additional queries to filter matched events before they are processed. |
| <CopyableCode code="hasExtendedTitle" /> | `boolean` | Whether the notifications include the triggering group-by values in their title. |
| <CopyableCode code="isDefault" /> | `boolean` | Whether the rule is included by default. |
| <CopyableCode code="isDeleted" /> | `boolean` | Whether the rule has been deleted. |
| <CopyableCode code="isEnabled" /> | `boolean` | Whether the rule is enabled. |
| <CopyableCode code="message" /> | `string` | Message for generated signals. |
| <CopyableCode code="options" /> | `object` | Options on rules. |
| <CopyableCode code="queries" /> | `array` | Queries for selecting logs which are part of the rule. |
| <CopyableCode code="tags" /> | `array` | Tags for generated signals. |
| <CopyableCode code="type" /> | `string` | The rule type. |
| <CopyableCode code="updateAuthorId" /> | `integer` | User ID of the user who updated the rule. |
| <CopyableCode code="version" /> | `integer` | The version of the rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_security_monitoring_rule" /> | `SELECT` | <CopyableCode code="rule_id, dd_site" /> | Get a rule's details. |
| <CopyableCode code="list_security_monitoring_rules" /> | `SELECT` | <CopyableCode code="dd_site" /> | List rules. |
| <CopyableCode code="create_security_monitoring_rule" /> | `INSERT` | <CopyableCode code="dd_site" /> | Create a detection rule. |
| <CopyableCode code="delete_security_monitoring_rule" /> | `DELETE` | <CopyableCode code="rule_id, dd_site" /> | Delete an existing rule. Default rules cannot be deleted. |
| <CopyableCode code="update_security_monitoring_rule" /> | `EXEC` | <CopyableCode code="rule_id, dd_site" /> | Update an existing rule. When updating `cases`, `queries` or `options`, the whole field<br />must be included. For example, when modifying a query all queries must be included.<br />Default rules can only be updated to be enabled and to change notifications. |

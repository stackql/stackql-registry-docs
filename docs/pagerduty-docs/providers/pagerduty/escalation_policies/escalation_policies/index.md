---
title: escalation_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - escalation_policies
  - escalation_policies
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>escalation_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.escalation_policies.escalation_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The name of the escalation policy. |
| `description` | `string` | Escalation policy description. |
| `_type` | `string` | The type of object being created. |
| `escalation_rules` | `array` |  |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `num_loops` | `integer` | The number of times the escalation policy will repeat after reaching the end of its escalation. |
| `on_call_handoff_notifications` | `string` | Determines how on call handoff notifications will be sent for users on the escalation policy. Defaults to "if_has_services". |
| `self` | `string` | the API show URL at which the object is accessible |
| `services` | `array` |  |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `teams` | `array` | Team associated with the policy. Account must have the `teams` ability to use this parameter. Only one team may be associated with the policy. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_escalation_policy` | `SELECT` | `id` | Get information about an existing escalation policy and its rules.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.read`<br /> |
| `list_escalation_policies` | `SELECT` |  | List all of the existing escalation policies.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.read`<br /> |
| `create_escalation_policy` | `INSERT` | `data__escalation_policy` | Creates a new escalation policy. At least one escalation rule must be provided.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.write`<br /> |
| `delete_escalation_policy` | `DELETE` | `id` | Deletes an existing escalation policy and rules. The escalation policy must not be in use by any services.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.write`<br /> |
| `_get_escalation_policy` | `EXEC` | `id` | Get information about an existing escalation policy and its rules.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.read`<br /> |
| `_list_escalation_policies` | `EXEC` |  | List all of the existing escalation policies.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.read`<br /> |
| `update_escalation_policy` | `EXEC` | `id, data__escalation_policy` | Updates an existing escalation policy and rules.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.write`<br /> |

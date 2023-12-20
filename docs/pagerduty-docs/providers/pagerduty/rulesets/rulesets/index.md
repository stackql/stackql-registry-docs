---
title: rulesets
hide_title: false
hide_table_of_contents: false
keywords:
  - rulesets
  - rulesets
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
<tr><td><b>Name</b></td><td><code>rulesets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.rulesets.rulesets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the Ruleset. |
| `name` | `string` | Name of the Ruleset. |
| `created_at` | `string` | The date the Ruleset was created at. |
| `creator` | `object` | Reference to the user that has created the Ruleset. |
| `routing_keys` | `array` | Routing keys routed to this Ruleset. |
| `self` | `string` | the API show URL at which the object is accessible |
| `team` | `object` | Reference to the team that owns the Ruleset. If none is specified, only admins have access. |
| `type` | `string` |  |
| `updated_at` | `string` | The date the Ruleset was last updated. |
| `updater` | `object` | Reference to the user that has updated the Ruleset last. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_ruleset` | `SELECT` | `id` | Get a Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.read`<br /> |
| `list_rulesets` | `SELECT` |  | List all Rulesets<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.read`<br /> |
| `create_ruleset` | `INSERT` | `data__ruleset` | Create a new Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.write`<br /> |
| `delete_ruleset` | `DELETE` | `id` | Delete a Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.write`<br /> |
| `_get_ruleset` | `EXEC` | `id` | Get a Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.read`<br /> |
| `_list_rulesets` | `EXEC` |  | List all Rulesets<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.read`<br /> |
| `update_ruleset` | `EXEC` | `id, data__ruleset` | Update a Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.write`<br /> |

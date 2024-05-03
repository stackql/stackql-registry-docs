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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rulesets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.rulesets.rulesets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the Ruleset. |
| <CopyableCode code="name" /> | `string` | Name of the Ruleset. |
| <CopyableCode code="created_at" /> | `string` | The date the Ruleset was created at. |
| <CopyableCode code="creator" /> | `object` | Reference to the user that has created the Ruleset. |
| <CopyableCode code="routing_keys" /> | `array` | Routing keys routed to this Ruleset. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="team" /> | `object` | Reference to the team that owns the Ruleset. If none is specified, only admins have access. |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` | The date the Ruleset was last updated. |
| <CopyableCode code="updater" /> | `object` | Reference to the user that has updated the Ruleset last. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_ruleset" /> | `SELECT` | <CopyableCode code="id" /> | Get a Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.read`<br /> |
| <CopyableCode code="list_rulesets" /> | `SELECT` |  | List all Rulesets<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.read`<br /> |
| <CopyableCode code="create_ruleset" /> | `INSERT` | <CopyableCode code="data__ruleset" /> | Create a new Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.write`<br /> |
| <CopyableCode code="delete_ruleset" /> | `DELETE` | <CopyableCode code="id" /> | Delete a Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.write`<br /> |
| <CopyableCode code="_get_ruleset" /> | `EXEC` | <CopyableCode code="id" /> | Get a Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.read`<br /> |
| <CopyableCode code="_list_rulesets" /> | `EXEC` |  | List all Rulesets<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.read`<br /> |
| <CopyableCode code="update_ruleset" /> | `EXEC` | <CopyableCode code="id, data__ruleset" /> | Update a Ruleset.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Rulesets allow you to route events to an endpoint and create collections of Event Rules, which define sets of actions to take based on event content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#rulesets)<br /><br />Scoped OAuth requires: `event_rules.write`<br /> |

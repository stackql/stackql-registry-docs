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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>escalation_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.escalation_policies.escalation_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of the escalation policy. |
| <CopyableCode code="description" /> | `string` | Escalation policy description. |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="escalation_rules" /> | `array` |  |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="num_loops" /> | `integer` | The number of times the escalation policy will repeat after reaching the end of its escalation. |
| <CopyableCode code="on_call_handoff_notifications" /> | `string` | Determines how on call handoff notifications will be sent for users on the escalation policy. Defaults to "if_has_services". |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="services" /> | `array` |  |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="teams" /> | `array` | Team associated with the policy. Account must have the `teams` ability to use this parameter. Only one team may be associated with the policy. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_escalation_policy" /> | `SELECT` | <CopyableCode code="id" /> | Get information about an existing escalation policy and its rules.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.read`<br /> |
| <CopyableCode code="list_escalation_policies" /> | `SELECT` |  | List all of the existing escalation policies.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.read`<br /> |
| <CopyableCode code="create_escalation_policy" /> | `INSERT` | <CopyableCode code="data__escalation_policy" /> | Creates a new escalation policy. At least one escalation rule must be provided.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.write`<br /> |
| <CopyableCode code="delete_escalation_policy" /> | `DELETE` | <CopyableCode code="id" /> | Deletes an existing escalation policy and rules. The escalation policy must not be in use by any services.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.write`<br /> |
| <CopyableCode code="_get_escalation_policy" /> | `EXEC` | <CopyableCode code="id" /> | Get information about an existing escalation policy and its rules.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.read`<br /> |
| <CopyableCode code="_list_escalation_policies" /> | `EXEC` |  | List all of the existing escalation policies.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.read`<br /> |
| <CopyableCode code="update_escalation_policy" /> | `EXEC` | <CopyableCode code="id, data__escalation_policy" /> | Updates an existing escalation policy and rules.<br /><br />Escalation policies define which user should be alerted at which time.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#escalation-policies)<br /><br />Scoped OAuth requires: `escalation_policies.write`<br /> |

---
title: org_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - org_rules
  - repos
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>org_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.org_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The ID of the ruleset |
| <CopyableCode code="name" /> | `string` | The name of the ruleset |
| <CopyableCode code="_links" /> | `object` |  |
| <CopyableCode code="bypass_actors" /> | `array` | The actors that can bypass the rules in this ruleset |
| <CopyableCode code="conditions" /> | `object` | Parameters for a repository ruleset ref name condition |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="current_user_can_bypass" /> | `string` | The bypass type of the user making the API request for this ruleset. This field is only returned when<br />querying the repository-level endpoint. |
| <CopyableCode code="enforcement" /> | `string` | The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page (`evaluate` is only available with GitHub Enterprise). |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="rules" /> | `array` |  |
| <CopyableCode code="source" /> | `string` | The name of the source |
| <CopyableCode code="source_type" /> | `string` | The type of the source of the ruleset |
| <CopyableCode code="target" /> | `string` | The target of the ruleset |
| <CopyableCode code="updated_at" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_org_ruleset" /> | `SELECT` | <CopyableCode code="org, ruleset_id" /> | Get a repository ruleset for an organization. |
| <CopyableCode code="get_org_rulesets" /> | `SELECT` | <CopyableCode code="org" /> | Get all the repository rulesets for an organization. |
| <CopyableCode code="create_org_ruleset" /> | `INSERT` | <CopyableCode code="org, data__enforcement, data__name" /> | Create a repository ruleset for an organization. |
| <CopyableCode code="delete_org_ruleset" /> | `DELETE` | <CopyableCode code="org, ruleset_id" /> | Delete a ruleset for an organization. |
| <CopyableCode code="update_org_ruleset" /> | `EXEC` | <CopyableCode code="org, ruleset_id" /> | Update a ruleset for an organization. |

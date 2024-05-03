---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.rules" /></td></tr>
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
| <CopyableCode code="get_repo_ruleset" /> | `SELECT` | <CopyableCode code="owner, repo, ruleset_id" /> | Get a ruleset for a repository. |
| <CopyableCode code="get_repo_rulesets" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Get all the rulesets for a repository. |
| <CopyableCode code="create_repo_ruleset" /> | `INSERT` | <CopyableCode code="owner, repo, data__enforcement, data__name" /> | Create a ruleset for a repository. |
| <CopyableCode code="delete_repo_ruleset" /> | `DELETE` | <CopyableCode code="owner, repo, ruleset_id" /> | Delete a ruleset for a repository. |
| <CopyableCode code="get_branch_rules" /> | `EXEC` | <CopyableCode code="branch, owner, repo" /> | Returns all active rules that apply to the specified branch. The branch does not need to exist; rules that would apply<br />to a branch with that name will be returned. All active rules that apply will be returned, regardless of the level<br />at which they are configured (e.g. repository or organization). Rules in rulesets with "evaluate" or "disabled"<br />enforcement statuses are not returned. |
| <CopyableCode code="update_repo_ruleset" /> | `EXEC` | <CopyableCode code="owner, repo, ruleset_id" /> | Update a ruleset for a repository. |

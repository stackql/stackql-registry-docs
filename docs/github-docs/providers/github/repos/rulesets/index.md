---
title: rulesets
hide_title: false
hide_table_of_contents: false
keywords:
  - rulesets
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rulesets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.rulesets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the ruleset |
| `name` | `string` | The name of the ruleset |
| `bypass_actors` | `array` | The actors that can bypass the rules in this ruleset |
| `target` | `string` | The target of the ruleset |
| `enforcement` | `string` | The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page (`evaluate` is only available with GitHub Enterprise). |
| `_links` | `object` |  |
| `current_user_can_bypass` | `string` | The bypass type of the user making the API request for this ruleset. This field is only returned when<br />querying the repository-level endpoint. |
| `rules` | `array` |  |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `source_type` | `string` | The type of the source of the ruleset |
| `conditions` | `object` | Parameters for a repository ruleset ref name condition |
| `source` | `string` | The name of the source |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_repo_ruleset` | `SELECT` | `owner, repo, ruleset_id` | Get a ruleset for a repository. |
| `get_repo_rulesets` | `SELECT` | `owner, repo` | Get all the rulesets for a repository. |
| `create_repo_ruleset` | `INSERT` | `owner, repo, data__enforcement, data__name` | Create a ruleset for a repository. |
| `delete_repo_ruleset` | `DELETE` | `owner, repo, ruleset_id` | Delete a ruleset for a repository. |
| `update_repo_ruleset` | `EXEC` | `owner, repo, ruleset_id` | Update a ruleset for a repository. |

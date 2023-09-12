---
title: orgs_rulesets
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_rulesets
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
<tr><td><b>Name</b></td><td><code>orgs_rulesets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.orgs_rulesets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the ruleset |
| `name` | `string` | The name of the ruleset |
| `bypass_actors` | `array` | The actors that can bypass the rules in this ruleset |
| `conditions` | `object` | Parameters for a repository ruleset ref name condition |
| `source` | `string` | The name of the source |
| `updated_at` | `string` |  |
| `_links` | `object` |  |
| `target` | `string` | The target of the ruleset |
| `enforcement` | `string` | The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page (`evaluate` is only available with GitHub Enterprise). |
| `source_type` | `string` | The type of the source of the ruleset |
| `node_id` | `string` |  |
| `current_user_can_bypass` | `string` | The bypass type of the user making the API request for this ruleset. This field is only returned when<br />querying the repository-level endpoint. |
| `rules` | `array` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_org_ruleset` | `SELECT` | `org, ruleset_id` | Get a repository ruleset for an organization. |
| `get_org_rulesets` | `SELECT` | `org` | Get all the repository rulesets for an organization. |
| `create_org_ruleset` | `INSERT` | `org, data__enforcement, data__name` | Create a repository ruleset for an organization. |
| `delete_org_ruleset` | `DELETE` | `org, ruleset_id` | Delete a ruleset for an organization. |
| `update_org_ruleset` | `EXEC` | `org, ruleset_id` | Update a ruleset for an organization. |

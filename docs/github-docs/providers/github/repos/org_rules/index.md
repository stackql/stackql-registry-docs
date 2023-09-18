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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>org_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.org_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the ruleset |
| `name` | `string` | The name of the ruleset |
| `_links` | `object` |  |
| `source` | `string` | The name of the source |
| `created_at` | `string` |  |
| `enforcement` | `string` | The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page (`evaluate` is only available with GitHub Enterprise). |
| `rules` | `array` |  |
| `node_id` | `string` |  |
| `bypass_actors` | `array` | The actors that can bypass the rules in this ruleset |
| `current_user_can_bypass` | `string` | The bypass type of the user making the API request for this ruleset. This field is only returned when<br />querying the repository-level endpoint. |
| `conditions` | `object` | Parameters for a repository ruleset ref name condition |
| `updated_at` | `string` |  |
| `source_type` | `string` | The type of the source of the ruleset |
| `target` | `string` | The target of the ruleset |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_org_ruleset` | `SELECT` | `org, ruleset_id` | Get a repository ruleset for an organization. |
| `get_org_rulesets` | `SELECT` | `org` | Get all the repository rulesets for an organization. |
| `create_org_ruleset` | `INSERT` | `org, data__enforcement, data__name` | Create a repository ruleset for an organization. |
| `delete_org_ruleset` | `DELETE` | `org, ruleset_id` | Delete a ruleset for an organization. |
| `update_org_ruleset` | `EXEC` | `org, ruleset_id` | Update a ruleset for an organization. |

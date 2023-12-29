---
title: scorecard_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - scorecard_rules
  - service_scorecards
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scorecard_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.service_scorecards.scorecard_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID for a scorecard rule. |
| `attributes` | `object` | Details of a rule. |
| `relationships` | `object` | Scorecard create rule response relationship. |
| `type` | `string` | The JSON:API type for scorecard rules. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_scorecard_rules` | `SELECT` | `dd_site` | Fetch all rules. |
| `create_scorecard_rule` | `INSERT` | `dd_site` | Creates a new rule. |
| `delete_scorecard_rule` | `DELETE` | `rule_id, dd_site` | Deletes a single rule. |
| `_list_scorecard_rules` | `EXEC` | `dd_site` | Fetch all rules. |

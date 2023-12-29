---
title: scorecard_outcomes
hide_title: false
hide_table_of_contents: false
keywords:
  - scorecard_outcomes
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
<tr><td><b>Name</b></td><td><code>scorecard_outcomes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.service_scorecards.scorecard_outcomes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID for a rule outcome. |
| `attributes` | `object` | The JSON:API attributes for an outcome. |
| `relationships` | `object` | The JSON:API relationship to a scorecard rule. |
| `type` | `string` | The JSON:API type for an outcome. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_scorecard_outcomes` | `SELECT` | `dd_site` | Fetches all rule outcomes. |
| `create_scorecard_outcomes_batch` | `INSERT` | `dd_site` | Sets multiple service-rule outcomes in a single batched request. |
| `_list_scorecard_outcomes` | `EXEC` | `dd_site` | Fetches all rule outcomes. |

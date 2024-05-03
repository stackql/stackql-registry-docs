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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scorecard_outcomes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.service_scorecards.scorecard_outcomes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID for a rule outcome. |
| <CopyableCode code="attributes" /> | `object` | The JSON:API attributes for an outcome. |
| <CopyableCode code="relationships" /> | `object` | The JSON:API relationship to a scorecard rule. |
| <CopyableCode code="type" /> | `string` | The JSON:API type for an outcome. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_scorecard_outcomes" /> | `SELECT` | <CopyableCode code="dd_site" /> | Fetches all rule outcomes. |
| <CopyableCode code="create_scorecard_outcomes_batch" /> | `INSERT` | <CopyableCode code="dd_site" /> | Sets multiple service-rule outcomes in a single batched request. |
| <CopyableCode code="_list_scorecard_outcomes" /> | `EXEC` | <CopyableCode code="dd_site" /> | Fetches all rule outcomes. |

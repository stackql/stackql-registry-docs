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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scorecard_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.service_scorecards.scorecard_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID for a scorecard rule. |
| <CopyableCode code="attributes" /> | `object` | Details of a rule. |
| <CopyableCode code="relationships" /> | `object` | Scorecard create rule response relationship. |
| <CopyableCode code="type" /> | `string` | The JSON:API type for scorecard rules. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_scorecard_rules" /> | `SELECT` | <CopyableCode code="dd_site" /> | Fetch all rules. |
| <CopyableCode code="create_scorecard_rule" /> | `INSERT` | <CopyableCode code="dd_site" /> | Creates a new rule. |
| <CopyableCode code="delete_scorecard_rule" /> | `DELETE` | <CopyableCode code="rule_id, dd_site" /> | Deletes a single rule. |
| <CopyableCode code="_list_scorecard_rules" /> | `EXEC` | <CopyableCode code="dd_site" /> | Fetch all rules. |

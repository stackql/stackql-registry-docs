---
title: deployment_rule_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_rule_integrations
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
<tr><td><b>Name</b></td><td><code>deployment_rule_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.deployment_rule_integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="available_custom_deployment_protection_rule_integrations" /> | `array` |  |
| <CopyableCode code="total_count" /> | `integer` | The total number of custom deployment protection rule integrations available for this environment. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_custom_deployment_rule_integrations" /> | `SELECT` | <CopyableCode code="environment_name, owner, repo" /> |

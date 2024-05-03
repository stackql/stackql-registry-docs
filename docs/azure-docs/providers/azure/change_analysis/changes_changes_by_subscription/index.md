---
title: changes_changes_by_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - changes_changes_by_subscription
  - change_analysis
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>changes_changes_by_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.change_analysis.changes_changes_by_subscription" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$endTime, $startTime, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="$endTime, $startTime, subscriptionId" /> |

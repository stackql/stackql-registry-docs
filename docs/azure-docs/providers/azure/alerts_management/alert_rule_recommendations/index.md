---
title: alert_rule_recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rule_recommendations
  - alerts_management
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
<tr><td><b>Name</b></td><td><code>alert_rule_recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.alert_rule_recommendations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Retrieve alert rule recommendations for a resource. |
| <CopyableCode code="list_by_target_type" /> | `SELECT` | <CopyableCode code="subscriptionId, targetType" /> | Retrieve alert rule recommendations for a target type. |
| <CopyableCode code="_list_by_resource" /> | `EXEC` | <CopyableCode code="resourceUri" /> | Retrieve alert rule recommendations for a resource. |
| <CopyableCode code="_list_by_target_type" /> | `EXEC` | <CopyableCode code="subscriptionId, targetType" /> | Retrieve alert rule recommendations for a target type. |

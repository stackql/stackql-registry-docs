---
title: component_current_billing_features
hide_title: false
hide_table_of_contents: false
keywords:
  - component_current_billing_features
  - application_insights
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
<tr><td><b>Name</b></td><td><code>component_current_billing_features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.component_current_billing_features" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="CurrentBillingFeatures" /> | `array` | Current enabled pricing plan. When the component is in the Enterprise plan, this will list both 'Basic' and 'Application Insights Enterprise'. |
| <CopyableCode code="DataVolumeCap" /> | `object` | An Application Insights component daily data volume cap |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns current billing features for an Application Insights component. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Update current billing features for an Application Insights component. |

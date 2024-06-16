---
title: predictions_training_results
hide_title: false
hide_table_of_contents: false
keywords:
  - predictions_training_results
  - customer_insights
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>predictions_training_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.predictions_training_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="canonicalProfiles" /> | `array` | Canonical profiles. |
| <CopyableCode code="predictionDistribution" /> | `object` | The definition of the prediction distribution. |
| <CopyableCode code="primaryProfileInstanceCount" /> | `integer` | Instance count of the primary profile. |
| <CopyableCode code="scoreName" /> | `string` | Score name. |
| <CopyableCode code="tenantId" /> | `string` | The hub name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, predictionName, resourceGroupName, subscriptionId" /> |

---
title: commitment_plans_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - commitment_plans_plan
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>commitment_plans_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.commitment_plans_plan" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="kind" /> | `string` | The kind (type) of cognitive service account. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of Cognitive Services account commitment plan. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="commitmentPlanName, resourceGroupName, subscriptionId" /> | Returns a Cognitive Services commitment plan specified by the parameters. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="commitmentPlanName, resourceGroupName, subscriptionId" /> | Create Cognitive Services commitment plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="commitmentPlanName, resourceGroupName, subscriptionId" /> | Deletes a Cognitive Services commitment plan from the resource group.  |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="commitmentPlanName, resourceGroupName, subscriptionId" /> | Create Cognitive Services commitment plan. |

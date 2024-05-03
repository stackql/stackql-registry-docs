---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - time_series_insights
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.time_series_insights.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The kind of the environment. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="sku" /> | `object` | The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Gets the environment with the specified name in the specified subscription and resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the available environments associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the available environments within a subscription, irrespective of the resource groups. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId, data__kind, data__sku" /> | Create or update an environment in the specified subscription and resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Deletes the environment with the specified name in the specified subscription and resource group. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the available environments associated with the subscription and within the specified resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the available environments within a subscription, irrespective of the resource groups. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId, data__kind" /> | Updates the environment with the specified name in the specified subscription and resource group. |

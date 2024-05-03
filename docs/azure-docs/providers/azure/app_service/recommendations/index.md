---
title: recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendations
  - app_service
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
<tr><td><b>Name</b></td><td><code>recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.recommendations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Recommendation resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for List all recommendations for a subscription. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for List all recommendations for a subscription. |
| <CopyableCode code="disable_all_for_hosting_environment" /> | `EXEC` | <CopyableCode code="environmentName, hostingEnvironmentName, resourceGroupName, subscriptionId" /> | Description for Disable all recommendations for an app. |
| <CopyableCode code="disable_all_for_web_app" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Description for Disable all recommendations for an app. |
| <CopyableCode code="disable_recommendation_for_hosting_environment" /> | `EXEC` | <CopyableCode code="environmentName, hostingEnvironmentName, name, resourceGroupName, subscriptionId" /> | Description for Disables the specific rule for a web site permanently. |
| <CopyableCode code="disable_recommendation_for_site" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, siteName, subscriptionId" /> | Description for Disables the specific rule for a web site permanently. |
| <CopyableCode code="disable_recommendation_for_subscription" /> | `EXEC` | <CopyableCode code="name, subscriptionId" /> | Description for Disables the specified rule so it will not apply to a subscription in the future. |
| <CopyableCode code="reset_all_filters" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for Reset all recommendation opt-out settings for a subscription. |
| <CopyableCode code="reset_all_filters_for_hosting_environment" /> | `EXEC` | <CopyableCode code="environmentName, hostingEnvironmentName, resourceGroupName, subscriptionId" /> | Description for Reset all recommendation opt-out settings for an app. |
| <CopyableCode code="reset_all_filters_for_web_app" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | Description for Reset all recommendation opt-out settings for an app. |

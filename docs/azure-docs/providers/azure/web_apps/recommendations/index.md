---
title: recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendations
  - web_apps
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.recommendations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | Recommendation resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Recommendations_List` | `SELECT` | `subscriptionId` | Description for List all recommendations for a subscription. |
| `Recommendations_DisableAllForHostingEnvironment` | `EXEC` | `environmentName, hostingEnvironmentName, resourceGroupName, subscriptionId` | Description for Disable all recommendations for an app. |
| `Recommendations_DisableAllForWebApp` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | Description for Disable all recommendations for an app. |
| `Recommendations_DisableRecommendationForHostingEnvironment` | `EXEC` | `environmentName, hostingEnvironmentName, name, resourceGroupName, subscriptionId` | Description for Disables the specific rule for a web site permanently. |
| `Recommendations_DisableRecommendationForSite` | `EXEC` | `name, resourceGroupName, siteName, subscriptionId` | Description for Disables the specific rule for a web site permanently. |
| `Recommendations_DisableRecommendationForSubscription` | `EXEC` | `name, subscriptionId` | Description for Disables the specified rule so it will not apply to a subscription in the future. |
| `Recommendations_GetRuleDetailsByHostingEnvironment` | `EXEC` | `hostingEnvironmentName, name, resourceGroupName, subscriptionId` | Description for Get a recommendation rule for an app. |
| `Recommendations_GetRuleDetailsByWebApp` | `EXEC` | `name, resourceGroupName, siteName, subscriptionId` | Description for Get a recommendation rule for an app. |
| `Recommendations_ListHistoryForHostingEnvironment` | `EXEC` | `hostingEnvironmentName, resourceGroupName, subscriptionId` | Description for Get past recommendations for an app, optionally specified by the time range. |
| `Recommendations_ListHistoryForWebApp` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | Description for Get past recommendations for an app, optionally specified by the time range. |
| `Recommendations_ListRecommendedRulesForHostingEnvironment` | `EXEC` | `hostingEnvironmentName, resourceGroupName, subscriptionId` | Description for Get all recommendations for a hosting environment. |
| `Recommendations_ListRecommendedRulesForWebApp` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | Description for Get all recommendations for an app. |
| `Recommendations_ResetAllFilters` | `EXEC` | `subscriptionId` | Description for Reset all recommendation opt-out settings for a subscription. |
| `Recommendations_ResetAllFiltersForHostingEnvironment` | `EXEC` | `environmentName, hostingEnvironmentName, resourceGroupName, subscriptionId` | Description for Reset all recommendation opt-out settings for an app. |
| `Recommendations_ResetAllFiltersForWebApp` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | Description for Reset all recommendation opt-out settings for an app. |

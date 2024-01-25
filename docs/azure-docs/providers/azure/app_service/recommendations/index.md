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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.recommendations</code></td></tr>
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
| `list` | `SELECT` | `subscriptionId` | Description for List all recommendations for a subscription. |
| `_list` | `EXEC` | `subscriptionId` | Description for List all recommendations for a subscription. |
| `disable_all_for_hosting_environment` | `EXEC` | `environmentName, hostingEnvironmentName, resourceGroupName, subscriptionId` | Description for Disable all recommendations for an app. |
| `disable_all_for_web_app` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | Description for Disable all recommendations for an app. |
| `disable_recommendation_for_hosting_environment` | `EXEC` | `environmentName, hostingEnvironmentName, name, resourceGroupName, subscriptionId` | Description for Disables the specific rule for a web site permanently. |
| `disable_recommendation_for_site` | `EXEC` | `name, resourceGroupName, siteName, subscriptionId` | Description for Disables the specific rule for a web site permanently. |
| `disable_recommendation_for_subscription` | `EXEC` | `name, subscriptionId` | Description for Disables the specified rule so it will not apply to a subscription in the future. |
| `reset_all_filters` | `EXEC` | `subscriptionId` | Description for Reset all recommendation opt-out settings for a subscription. |
| `reset_all_filters_for_hosting_environment` | `EXEC` | `environmentName, hostingEnvironmentName, resourceGroupName, subscriptionId` | Description for Reset all recommendation opt-out settings for an app. |
| `reset_all_filters_for_web_app` | `EXEC` | `resourceGroupName, siteName, subscriptionId` | Description for Reset all recommendation opt-out settings for an app. |

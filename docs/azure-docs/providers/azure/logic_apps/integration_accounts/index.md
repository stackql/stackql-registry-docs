---
title: integration_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_accounts
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>integration_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The integration account properties. |
| `sku` | `object` | The integration account sku. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets an integration account. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets a list of integration accounts by resource group. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | Gets a list of integration accounts by subscription. |
| `create_or_update` | `INSERT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Creates or updates an integration account. |
| `delete` | `DELETE` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Deletes an integration account. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Gets a list of integration accounts by resource group. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | Gets a list of integration accounts by subscription. |
| `log_tracking_events` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId, data__events, data__sourceType` | Logs the integration account's tracking events. |
| `regenerate_access_key` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Regenerates the integration account access key. |
| `update` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Updates an integration account. |

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
| `sku` | `object` | The integration account sku. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The integration account properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationAccounts_Get` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets an integration account. |
| `IntegrationAccounts_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets a list of integration accounts by resource group. |
| `IntegrationAccounts_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets a list of integration accounts by subscription. |
| `IntegrationAccounts_CreateOrUpdate` | `INSERT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Creates or updates an integration account. |
| `IntegrationAccounts_Delete` | `DELETE` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Deletes an integration account. |
| `IntegrationAccounts_ListCallbackUrl` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets the integration account callback URL. |
| `IntegrationAccounts_ListKeyVaultKeys` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId, data__keyVault` | Gets the integration account's Key Vault keys. |
| `IntegrationAccounts_LogTrackingEvents` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId, data__events, data__sourceType` | Logs the integration account's tracking events. |
| `IntegrationAccounts_RegenerateAccessKey` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Regenerates the integration account access key. |
| `IntegrationAccounts_Update` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Updates an integration account. |

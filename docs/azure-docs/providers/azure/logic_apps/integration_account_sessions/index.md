---
title: integration_account_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_sessions
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
<tr><td><b>Name</b></td><td><code>integration_account_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_account_sessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The integration account session properties. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationAccountSessions_Get` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, sessionName, subscriptionId` | Gets an integration account session. |
| `IntegrationAccountSessions_List` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets a list of integration account sessions. |
| `IntegrationAccountSessions_CreateOrUpdate` | `INSERT` | `api-version, integrationAccountName, resourceGroupName, sessionName, subscriptionId, data__properties` | Creates or updates an integration account session. |
| `IntegrationAccountSessions_Delete` | `DELETE` | `api-version, integrationAccountName, resourceGroupName, sessionName, subscriptionId` | Deletes an integration account session. |

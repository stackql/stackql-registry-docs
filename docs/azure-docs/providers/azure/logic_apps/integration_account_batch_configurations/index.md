---
title: integration_account_batch_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_batch_configurations
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
<tr><td><b>Name</b></td><td><code>integration_account_batch_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_account_batch_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `type` | `string` | Gets the resource type. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The batch configuration properties definition. |
| `tags` | `object` | The resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationAccountBatchConfigurations_Get` | `SELECT` | `api-version, batchConfigurationName, integrationAccountName, resourceGroupName, subscriptionId` | Get a batch configuration for an integration account. |
| `IntegrationAccountBatchConfigurations_List` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | List the batch configurations for an integration account. |
| `IntegrationAccountBatchConfigurations_CreateOrUpdate` | `INSERT` | `api-version, batchConfigurationName, integrationAccountName, resourceGroupName, subscriptionId, data__properties` | Create or update a batch configuration for an integration account. |
| `IntegrationAccountBatchConfigurations_Delete` | `DELETE` | `api-version, batchConfigurationName, integrationAccountName, resourceGroupName, subscriptionId` | Delete a batch configuration for an integration account. |

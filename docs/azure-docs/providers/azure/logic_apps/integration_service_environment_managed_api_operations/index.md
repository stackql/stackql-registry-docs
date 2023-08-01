---
title: integration_service_environment_managed_api_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environment_managed_api_operations
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
<tr><td><b>Name</b></td><td><code>integration_service_environment_managed_api_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_service_environment_managed_api_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The api operations properties |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `IntegrationServiceEnvironmentManagedApiOperations_List` | `SELECT` | `api-version, apiName, integrationServiceEnvironmentName, resourceGroup, subscriptionId` |

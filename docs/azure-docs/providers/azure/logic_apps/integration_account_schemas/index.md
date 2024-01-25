---
title: integration_account_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_schemas
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
<tr><td><b>Name</b></td><td><code>integration_account_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_account_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The integration account schema properties. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, schemaName, subscriptionId` | Gets an integration account schema. |
| `list` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets a list of integration account schemas. |
| `create_or_update` | `INSERT` | `api-version, integrationAccountName, resourceGroupName, schemaName, subscriptionId, data__properties` | Creates or updates an integration account schema. |
| `delete` | `DELETE` | `api-version, integrationAccountName, resourceGroupName, schemaName, subscriptionId` | Deletes an integration account schema. |
| `_list` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets a list of integration account schemas. |

---
title: api_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - api_schema
  - api_management
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
<tr><td><b>Name</b></td><td><code>api_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_schema</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Get the schema configuration at the API level. |
| `list_by_api` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Get the schema configuration at the API level. |
| `create_or_update` | `INSERT` | `apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Creates or updates schema configuration for the API. |
| `delete` | `DELETE` | `If-Match, apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Deletes the schema configuration at the Api. |
| `_list_by_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Get the schema configuration at the API level. |

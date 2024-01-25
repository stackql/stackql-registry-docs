---
title: global_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - global_schema
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
<tr><td><b>Name</b></td><td><code>global_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.global_schema</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, schemaId, serviceName, subscriptionId` | Gets the details of the Schema specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of schemas registered with service instance. |
| `create_or_update` | `INSERT` | `resourceGroupName, schemaId, serviceName, subscriptionId` | Creates new or updates existing specified Schema of the API Management service instance. |
| `delete` | `DELETE` | `If-Match, resourceGroupName, schemaId, serviceName, subscriptionId` | Deletes specific Schema. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of schemas registered with service instance. |

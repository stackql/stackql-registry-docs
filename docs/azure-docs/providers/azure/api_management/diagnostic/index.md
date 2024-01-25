---
title: diagnostic
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic
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
<tr><td><b>Name</b></td><td><code>diagnostic</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.diagnostic</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `diagnosticId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Diagnostic specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all diagnostics of the API Management service instance. |
| `create_or_update` | `INSERT` | `diagnosticId, resourceGroupName, serviceName, subscriptionId` | Creates a new Diagnostic or updates an existing one. |
| `delete` | `DELETE` | `If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified Diagnostic. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists all diagnostics of the API Management service instance. |
| `update` | `EXEC` | `If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the Diagnostic specified by its identifier. |

---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
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
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.certificate</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the certificate specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of all certificates in the specified service instance. |
| `create_or_update` | `INSERT` | `certificateId, resourceGroupName, serviceName, subscriptionId` | Creates or updates the certificate being used for authentication with the backend. |
| `delete` | `DELETE` | `If-Match, certificateId, resourceGroupName, serviceName, subscriptionId` | Deletes specific certificate. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of all certificates in the specified service instance. |
| `refresh_secret` | `EXEC` | `certificateId, resourceGroupName, serviceName, subscriptionId` | From KeyVault, Refresh the certificate being used for authentication with the backend. |

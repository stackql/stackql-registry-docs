---
title: connector_application
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_application
  - security
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
<tr><td><b>Name</b></td><td><code>connector_application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.connector_application</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Describes properties of an application |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityConnectorApplication_Get` | `SELECT` | `api-version, applicationId, resourceGroupName, securityConnectorName, subscriptionId` | Get a specific application for the requested scope by applicationId |
| `SecurityConnectorApplication_CreateOrUpdate` | `INSERT` | `api-version, applicationId, resourceGroupName, securityConnectorName, subscriptionId` | Creates or update a security Application on the given security connector. |
| `SecurityConnectorApplication_Delete` | `DELETE` | `api-version, applicationId, resourceGroupName, securityConnectorName, subscriptionId` | Delete an Application over a given scope |

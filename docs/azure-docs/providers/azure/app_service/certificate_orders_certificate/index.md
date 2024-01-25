---
title: certificate_orders_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_orders_certificate
  - app_service
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
<tr><td><b>Name</b></td><td><code>certificate_orders_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.certificate_orders_certificate</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Key Vault container for a certificate that is purchased through Azure. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateOrderName, name, resourceGroupName, subscriptionId` | Description for Get the certificate associated with a certificate order. |
| `create_or_update` | `INSERT` | `certificateOrderName, name, resourceGroupName, subscriptionId` | Description for Creates or updates a certificate and associates with key vault secret. |
| `delete` | `DELETE` | `certificateOrderName, name, resourceGroupName, subscriptionId` | Description for Delete the certificate associated with a certificate order. |
| `update` | `EXEC` | `certificateOrderName, name, resourceGroupName, subscriptionId` | Description for Creates or updates a certificate and associates with key vault secret. |

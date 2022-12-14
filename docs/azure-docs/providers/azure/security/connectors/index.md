---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
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
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Describes properties of a connector setting |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Connectors_Get` | `SELECT` | `api-version, connectorName, subscriptionId` | Details of a specific cloud account connector |
| `Connectors_List` | `SELECT` | `api-version, subscriptionId` | Cloud accounts connectors of a subscription |
| `Connectors_CreateOrUpdate` | `INSERT` | `api-version, connectorName, subscriptionId` | Create a cloud account connector or update an existing one. Connect to your cloud account. For AWS, use either account credentials or role-based authentication. For GCP, use account organization credentials. |
| `Connectors_Delete` | `DELETE` | `api-version, connectorName, subscriptionId` | Delete a cloud account connector from a subscription |

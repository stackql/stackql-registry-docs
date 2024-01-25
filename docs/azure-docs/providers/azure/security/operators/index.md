---
title: operators
hide_title: false
hide_table_of_contents: false
keywords:
  - operators
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
<tr><td><b>Name</b></td><td><code>operators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.operators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `identity` | `object` | Identity for the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, pricingName, securityOperatorName, subscriptionId` | Get a specific security operator for the requested scope. |
| `list` | `SELECT` | `api-version, pricingName, subscriptionId` | Lists Microsoft Defender for Cloud securityOperators in the subscription. |
| `create_or_update` | `INSERT` | `api-version, pricingName, securityOperatorName, subscriptionId` | Creates Microsoft Defender for Cloud security operator on the given scope. |
| `delete` | `DELETE` | `api-version, pricingName, securityOperatorName, subscriptionId` | Delete Microsoft Defender for Cloud securityOperator in the subscription. |
| `_list` | `EXEC` | `api-version, pricingName, subscriptionId` | Lists Microsoft Defender for Cloud securityOperators in the subscription. |

---
title: discovered_security_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - discovered_security_solutions
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
<tr><td><b>Name</b></td><td><code>discovered_security_solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.discovered_security_solutions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `location` | `string` | Location where the resource is stored |
| `properties` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiscoveredSecuritySolutions_Get` | `SELECT` | `api-version, ascLocation, discoveredSecuritySolutionName, resourceGroupName, subscriptionId` | Gets a specific discovered Security Solution. |
| `DiscoveredSecuritySolutions_List` | `SELECT` | `api-version, subscriptionId` | Gets a list of discovered Security Solutions for the subscription. |
| `DiscoveredSecuritySolutions_ListByHomeRegion` | `SELECT` | `api-version, ascLocation, subscriptionId` | Gets a list of discovered Security Solutions for the subscription and location. |

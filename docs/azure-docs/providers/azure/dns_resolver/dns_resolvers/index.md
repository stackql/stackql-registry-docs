---
title: dns_resolvers
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_resolvers
  - dns_resolver
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
<tr><td><b>Name</b></td><td><code>dns_resolvers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns_resolver.dns_resolvers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | ETag of the DNS resolver. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Represents the properties of a DNS resolver. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dnsResolverName, resourceGroupName, subscriptionId` | Gets properties of a DNS resolver. |
| `list` | `SELECT` | `subscriptionId` | Lists DNS resolvers in all resource groups of a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists DNS resolvers within a resource group. |
| `list_by_virtual_network` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Lists DNS resolver resource IDs linked to a virtual network. |
| `create_or_update` | `INSERT` | `dnsResolverName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a DNS resolver. |
| `delete` | `DELETE` | `dnsResolverName, resourceGroupName, subscriptionId` | Deletes a DNS resolver. WARNING: This operation cannot be undone. |
| `_list` | `EXEC` | `subscriptionId` | Lists DNS resolvers in all resource groups of a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists DNS resolvers within a resource group. |
| `update` | `EXEC` | `dnsResolverName, resourceGroupName, subscriptionId` | Updates a DNS resolver. |

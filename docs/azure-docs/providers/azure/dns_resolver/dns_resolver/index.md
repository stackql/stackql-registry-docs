---
title: dns_resolver
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_resolver
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
<tr><td><b>Name</b></td><td><code>dns_resolver</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns_resolver.dns_resolver</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | ETag of the DNS resolver. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Represents the properties of a DNS resolver. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DnsResolvers_Get` | `SELECT` | `dnsResolverName, resourceGroupName, subscriptionId` | Gets properties of a DNS resolver. |
| `DnsResolvers_List` | `SELECT` | `subscriptionId` | Lists DNS resolvers in all resource groups of a subscription. |
| `DnsResolvers_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists DNS resolvers within a resource group. |
| `DnsResolvers_ListByVirtualNetwork` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Lists DNS resolver resource IDs linked to a virtual network. |
| `DnsResolvers_CreateOrUpdate` | `INSERT` | `dnsResolverName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a DNS resolver. |
| `DnsResolvers_Delete` | `DELETE` | `dnsResolverName, resourceGroupName, subscriptionId` | Deletes a DNS resolver. WARNING: This operation cannot be undone. |
| `DnsResolvers_Update` | `EXEC` | `dnsResolverName, resourceGroupName, subscriptionId` | Updates a DNS resolver. |

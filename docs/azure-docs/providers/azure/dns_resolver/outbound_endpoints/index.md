---
title: outbound_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_endpoints
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
<tr><td><b>Name</b></td><td><code>outbound_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns_resolver.outbound_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | ETag of the outbound endpoint. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Represents the properties of an outbound endpoint for a DNS resolver. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId` | Gets properties of an outbound endpoint for a DNS resolver. |
| `list` | `SELECT` | `dnsResolverName, resourceGroupName, subscriptionId` | Lists outbound endpoints for a DNS resolver. |
| `create_or_update` | `INSERT` | `dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an outbound endpoint for a DNS resolver. |
| `delete` | `DELETE` | `dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId` | Deletes an outbound endpoint for a DNS resolver. WARNING: This operation cannot be undone. |
| `_list` | `EXEC` | `dnsResolverName, resourceGroupName, subscriptionId` | Lists outbound endpoints for a DNS resolver. |
| `update` | `EXEC` | `dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId` | Updates an outbound endpoint for a DNS resolver. |

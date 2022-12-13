---
title: inbound_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_endpoints
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
<tr><td><b>Name</b></td><td><code>inbound_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns_resolver.inbound_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | ETag of the inbound endpoint. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Represents the properties of an inbound endpoint for a DNS resolver. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `InboundEndpoints_Get` | `SELECT` | `dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId` | Gets properties of an inbound endpoint for a DNS resolver. |
| `InboundEndpoints_List` | `SELECT` | `dnsResolverName, resourceGroupName, subscriptionId` | Lists inbound endpoints for a DNS resolver. |
| `InboundEndpoints_CreateOrUpdate` | `INSERT` | `dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an inbound endpoint for a DNS resolver. |
| `InboundEndpoints_Delete` | `DELETE` | `dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId` | Deletes an inbound endpoint for a DNS resolver. WARNING: This operation cannot be undone. |
| `InboundEndpoints_Update` | `EXEC` | `dnsResolverName, inboundEndpointName, resourceGroupName, subscriptionId` | Updates an inbound endpoint for a DNS resolver. |

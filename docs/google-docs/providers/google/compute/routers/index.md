---
title: routers
hide_title: false
hide_table_of_contents: false
keywords:
  - routers
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.routers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `bgp` | `object` |  |
| `bgpPeers` | `array` | BGP information that must be configured into the routing stack to establish BGP peering. This information must specify the peer ASN and either the interface name, IP address, or peer IP address. Please refer to RFC4273. |
| `encryptedInterconnectRouter` | `boolean` | Indicates if a router is dedicated for use with encrypted VLAN attachments (interconnectAttachments). Not currently available publicly.  |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `region` | `string` | [Output Only] URI of the region where the router resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#router for routers. |
| `nats` | `array` | A list of NAT services created in this router. |
| `network` | `string` | URI of the network to which this router belongs. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `interfaces` | `array` | Router interfaces. Each interface requires either one linked resource, (for example, linkedVpnTunnel), or IP address and IP address range (for example, ipRange), or both. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of routers. |
| `get` | `SELECT` | `project, region, router` | Returns the specified Router resource. Gets a list of available routers by making a list() request. |
| `list` | `SELECT` | `project, region` | Retrieves a list of Router resources available to the specified project. |
| `insert` | `INSERT` | `project, region` | Creates a Router resource in the specified project and region using the data included in the request. |
| `delete` | `DELETE` | `project, region, router` | Deletes the specified Router resource. |
| `patch` | `EXEC` | `project, region, router` | Patches the specified Router resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules. |
| `preview` | `EXEC` | `project, region, router` | Preview fields auto-generated during router create and update operations. Calling this method does NOT create or update the router. |
| `update` | `EXEC` | `project, region, router` | Updates the specified Router resource with the data included in the request. This method conforms to PUT semantics, which requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message payload. |

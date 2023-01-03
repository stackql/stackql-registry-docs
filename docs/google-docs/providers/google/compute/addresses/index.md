---
title: addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - addresses
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
<tr><td><b>Name</b></td><td><code>addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.addresses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit. |
| `description` | `string` | An optional description of this resource. Provide this field when you create the resource. |
| `ipVersion` | `string` | The IP version that will be used by this address. Valid options are IPV4 or IPV6. This can only be specified for a global address. |
| `subnetwork` | `string` | The URL of the subnetwork in which to reserve the address. If an IP address is specified, it must be within the subnetwork's IP range. This field can only be used with INTERNAL type with a GCE_ENDPOINT or DNS_RESOLVER purpose. |
| `purpose` | `string` | The purpose of this resource, which can be one of the following values: - GCE_ENDPOINT for addresses that are used by VM instances, alias IP ranges, load balancers, and similar resources. - DNS_RESOLVER for a DNS resolver address in a subnetwork for a Cloud DNS inbound forwarder IP addresses (regional internal IP address in a subnet of a VPC network) - VPC_PEERING for global internal IP addresses used for private services access allocated ranges. - NAT_AUTO for the regional external IP addresses used by Cloud NAT when allocating addresses using automatic NAT IP address allocation. - IPSEC_INTERCONNECT for addresses created from a private IP range that are reserved for a VLAN attachment in an *IPsec-encrypted Cloud Interconnect* configuration. These addresses are regional resources. Not currently available publicly. - `SHARED_LOADBALANCER_VIP` for an internal IP address that is assigned to multiple internal forwarding rules. - `PRIVATE_SERVICE_CONNECT` for a private network address that is used to configure Private Service Connect. Only global internal addresses can use this purpose.  |
| `network` | `string` | The URL of the network in which to reserve the address. This field can only be used with INTERNAL type with the VPC_PEERING purpose. |
| `prefixLength` | `integer` | The prefix length if the resource represents an IP range. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `region` | `string` | [Output Only] The URL of the region where a regional address resides. For regional addresses, you must specify the region as a path parameter in the HTTP request URL. *This field is not applicable to global addresses.* |
| `networkTier` | `string` | This signifies the networking tier used for configuring this address and can only take the following values: PREMIUM or STANDARD. Internal IP addresses are always Premium Tier; global external IP addresses are always Premium Tier; regional external IP addresses can be either Standard or Premium Tier. If this field is not specified, it is assumed to be PREMIUM. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `status` | `string` | [Output Only] The status of the address, which can be one of RESERVING, RESERVED, or IN_USE. An address that is RESERVING is currently in the process of being reserved. A RESERVED address is currently reserved and available to use. An IN_USE address is currently being used by another resource and is not available. |
| `users` | `array` | [Output Only] The URLs of the resources that are using this address. |
| `address` | `string` | The static IP address represented by this resource. |
| `addressType` | `string` | The type of address to reserve, either INTERNAL or EXTERNAL. If unspecified, defaults to EXTERNAL. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#address for addresses. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of addresses. |
| `get` | `SELECT` | `address, project, region` | Returns the specified address resource. |
| `list` | `SELECT` | `project, region` | Retrieves a list of addresses contained within the specified region. |
| `insert` | `INSERT` | `project, region` | Creates an address resource in the specified project by using the data included in the request. |
| `delete` | `DELETE` | `address, project, region` | Deletes the specified address resource. |

---
title: target_vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - target_vpn_gateways
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
<tr><td><b>Name</b></td><td><code>target_vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.target_vpn_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `region` | `string` | [Output Only] URL of the region where the target VPN gateway resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `status` | `string` | [Output Only] The status of the VPN gateway, which can be one of the following: CREATING, READY, FAILED, or DELETING. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#targetVpnGateway for target VPN gateways. |
| `tunnels` | `array` | [Output Only] A list of URLs to VpnTunnel resources. VpnTunnels are created using the compute.vpntunnels.insert method and associated with a VPN gateway. |
| `network` | `string` | URL of the network to which this VPN gateway is attached. Provided by the client when the VPN gateway is created. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `forwardingRules` | `array` | [Output Only] A list of URLs to the ForwardingRule resources. ForwardingRules are created using compute.forwardingRules.insert and associated with a VPN gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `targetVpnGateways_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of target VPN gateways. |
| `targetVpnGateways_get` | `SELECT` | `project, region, targetVpnGateway` | Returns the specified target VPN gateway. Gets a list of available target VPN gateways by making a list() request. |
| `targetVpnGateways_list` | `SELECT` | `project, region` | Retrieves a list of target VPN gateways available to the specified project and region. |
| `targetVpnGateways_insert` | `INSERT` | `project, region` | Creates a target VPN gateway in the specified project and region using the data included in the request. |
| `targetVpnGateways_delete` | `DELETE` | `project, region, targetVpnGateway` | Deletes the specified target VPN gateway. |

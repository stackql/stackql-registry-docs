---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this field when you create the resource. |
| <CopyableCode code="asPaths" /> | `array` | [Output Only] AS path. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="destRange" /> | `string` | The destination range of outgoing packets that this route applies to. Both IPv4 and IPv6 are supported. Must specify an IPv4 range (e.g. 192.0.2.0/24) or an IPv6 range in RFC 4291 format (e.g. 2001:db8::/32). IPv6 range will be displayed using RFC 5952 compressed format. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of this resource. Always compute#routes for Route resources. |
| <CopyableCode code="network" /> | `string` | Fully-qualified URL of the network that this route applies to. |
| <CopyableCode code="nextHopGateway" /> | `string` | The URL to a gateway that should handle matching packets. You can only specify the internet gateway using a full or partial valid URL: projects/ project/global/gateways/default-internet-gateway |
| <CopyableCode code="nextHopHub" /> | `string` | [Output Only] The full resource name of the Network Connectivity Center hub that will handle matching packets. |
| <CopyableCode code="nextHopIlb" /> | `string` | The URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets or the IP address of the forwarding Rule. For example, the following are all valid URLs: - 10.128.0.56 - https://www.googleapis.com/compute/v1/projects/project/regions/region /forwardingRules/forwardingRule - regions/region/forwardingRules/forwardingRule  |
| <CopyableCode code="nextHopInstance" /> | `string` | The URL to an instance that should handle matching packets. You can specify this as a full or partial URL. For example: https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/ |
| <CopyableCode code="nextHopIp" /> | `string` | The network IP address of an instance that should handle matching packets. Both IPv6 address and IPv4 addresses are supported. Must specify an IPv4 address in dot-decimal notation (e.g. 192.0.2.99) or an IPv6 address in RFC 4291 format (e.g. 2001:db8::2d9:51:0:0 or 2001:db8:0:0:2d9:51:0:0). IPv6 addresses will be displayed using RFC 5952 compressed format (e.g. 2001:db8::2d9:51:0:0). Should never be an IPv4-mapped IPv6 address. |
| <CopyableCode code="nextHopNetwork" /> | `string` | The URL of the local network if it should handle matching packets. |
| <CopyableCode code="nextHopPeering" /> | `string` | [Output Only] The network peering name that should handle matching packets, which should conform to RFC1035. |
| <CopyableCode code="nextHopVpnTunnel" /> | `string` | The URL to a VpnTunnel that should handle matching packets. |
| <CopyableCode code="priority" /> | `integer` | The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length. In cases where multiple routes have equal prefix length, the one with the lowest-numbered priority value wins. The default value is `1000`. The priority value must be from `0` to `65535`, inclusive. |
| <CopyableCode code="routeStatus" /> | `string` | [Output only] The status of the route. |
| <CopyableCode code="routeType" /> | `string` | [Output Only] The type of this route, which can be one of the following values: - 'TRANSIT' for a transit route that this router learned from another Cloud Router and will readvertise to one of its BGP peers - 'SUBNET' for a route from a subnet of the VPC - 'BGP' for a route learned from a BGP peer of this router - 'STATIC' for a static route |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined fully-qualified URL for this resource. |
| <CopyableCode code="tags" /> | `array` | A list of instance tags to which this route applies. |
| <CopyableCode code="warnings" /> | `array` | [Output Only] If potential misconfigurations are detected for this route, this field will be populated with warning messages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, route" /> | Returns the specified Route resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves the list of Route resources available to the specified project. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project" /> | Creates a Route resource in the specified project using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, route" /> | Deletes the specified Route resource. |

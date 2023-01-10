---
title: client_vpn_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_connections
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_vpn_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.client_vpn_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ingressBytes` | `string` | The number of bytes sent by the client. |
| `egressPackets` | `string` | The number of packets received by the client. |
| `clientVpnEndpointId` | `string` | The ID of the Client VPN endpoint to which the client is connected. |
| `connectionId` | `string` | The ID of the client connection. |
| `connectionEstablishedTime` | `string` | The date and time the client connection was established. |
| `commonName` | `string` | The common name associated with the client. This is either the name of the client certificate, or the Active Directory user name. |
| `ingressPackets` | `string` | The number of packets sent by the client. |
| `status` | `object` | Describes the status of a client connection. |
| `postureComplianceStatusSet` | `array` | The statuses returned by the client connect handler for posture compliance, if applicable. |
| `egressBytes` | `string` | The number of bytes received by the client. |
| `clientIp` | `string` | The IP address of the client. |
| `timestamp` | `string` | The current date and time. |
| `connectionEndTime` | `string` | The date and time the client connection was terminated. |
| `username` | `string` | The username of the client who established the client connection. This information is only provided if Active Directory client authentication is used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `client_vpn_connections_Describe` | `SELECT` | `ClientVpnEndpointId` | Describes active client connections and connections that have been terminated within the last 60 minutes for the specified Client VPN endpoint. |
| `client_vpn_connections_Terminate` | `EXEC` | `ClientVpnEndpointId` | Terminates active Client VPN endpoint connections. This action can be used to terminate a specific client connection, or up to five connections established by a specific user. |

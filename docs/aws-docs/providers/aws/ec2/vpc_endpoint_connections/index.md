---
title: vpc_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_connections
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
<tr><td><b>Name</b></td><td><code>vpc_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `gatewayLoadBalancerArnSet` | `array` | The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service. |
| `networkLoadBalancerArnSet` | `array` | The Amazon Resource Names (ARNs) of the network load balancers for the service. |
| `vpcEndpointOwner` | `string` | The ID of the Amazon Web Services account that owns the VPC endpoint. |
| `vpcEndpointId` | `string` | The ID of the VPC endpoint. |
| `creationTimestamp` | `string` | The date and time that the VPC endpoint was created. |
| `serviceId` | `string` | The ID of the service to which the endpoint is connected. |
| `ipAddressType` | `string` | The IP address type for the endpoint. |
| `vpcEndpointState` | `string` | The state of the VPC endpoint. |
| `dnsEntrySet` | `array` | The DNS entries for the VPC endpoint. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpc_endpoint_connections_Describe` | `SELECT` | `region` | Describes the VPC endpoint connections to your VPC endpoint services, including any endpoints that are pending your acceptance. |
| `vpc_endpoint_connections_Accept` | `EXEC` | `ServiceId, VpcEndpointId, region` | Accepts one or more interface VPC endpoint connection requests to your VPC endpoint service. |
| `vpc_endpoint_connections_Reject` | `EXEC` | `ServiceId, VpcEndpointId, region` | Rejects one or more VPC endpoint connection requests to your VPC endpoint service. |

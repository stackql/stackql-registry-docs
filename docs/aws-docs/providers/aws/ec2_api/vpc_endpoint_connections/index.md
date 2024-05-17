---
title: vpc_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_connections
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.vpc_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTimestamp" /> | `string` | The date and time that the VPC endpoint was created. |
| <CopyableCode code="dnsEntrySet" /> | `array` | The DNS entries for the VPC endpoint. |
| <CopyableCode code="gatewayLoadBalancerArnSet" /> | `array` | The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service. |
| <CopyableCode code="ipAddressType" /> | `string` | The IP address type for the endpoint. |
| <CopyableCode code="networkLoadBalancerArnSet" /> | `array` | The Amazon Resource Names (ARNs) of the network load balancers for the service. |
| <CopyableCode code="serviceId" /> | `string` | The ID of the service to which the endpoint is connected. |
| <CopyableCode code="vpcEndpointId" /> | `string` | The ID of the VPC endpoint. |
| <CopyableCode code="vpcEndpointOwner" /> | `string` | The ID of the Amazon Web Services account that owns the VPC endpoint. |
| <CopyableCode code="vpcEndpointState" /> | `string` | The state of the VPC endpoint. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="vpc_endpoint_connections_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the VPC endpoint connections to your VPC endpoint services, including any endpoints that are pending your acceptance. |
| <CopyableCode code="vpc_endpoint_connections_Accept" /> | `EXEC` | <CopyableCode code="ServiceId, VpcEndpointId, region" /> | Accepts one or more interface VPC endpoint connection requests to your VPC endpoint service. |
| <CopyableCode code="vpc_endpoint_connections_Reject" /> | `EXEC` | <CopyableCode code="ServiceId, VpcEndpointId, region" /> | Rejects one or more VPC endpoint connection requests to your VPC endpoint service. |

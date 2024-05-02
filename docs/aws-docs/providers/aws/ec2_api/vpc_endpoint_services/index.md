---
title: vpc_endpoint_services
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_services
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.vpc_endpoint_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `acceptanceRequired` | `boolean` | Indicates whether VPC endpoint connection requests to the service must be accepted by the service owner. |
| `availabilityZoneSet` | `array` | The Availability Zones in which the service is available. |
| `baseEndpointDnsNameSet` | `array` | The DNS names for the service. |
| `managesVpcEndpoints` | `boolean` | Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted. |
| `owner` | `string` | The Amazon Web Services account ID of the service owner. |
| `payerResponsibility` | `string` | The payer responsibility. |
| `privateDnsName` | `string` | The private DNS name for the service. |
| `privateDnsNameSet` | `array` | The private DNS names assigned to the VPC endpoint service.  |
| `privateDnsNameVerificationState` | `string` | &lt;p&gt;The verification state of the VPC endpoint service.&lt;/p&gt; &lt;p&gt;Consumers of the endpoint service cannot use the private name when the state is not &lt;code&gt;verified&lt;/code&gt;.&lt;/p&gt; |
| `serviceId` | `string` | The ID of the endpoint service. |
| `serviceName` | `string` | The Amazon Resource Name (ARN) of the service. |
| `serviceType` | `array` | The type of service. |
| `supportedIpAddressTypeSet` | `array` | The supported IP address types. |
| `tagSet` | `array` | Any tags assigned to the service. |
| `vpcEndpointPolicySupported` | `boolean` | Indicates whether the service supports endpoint policies. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `vpc_endpoint_services_Describe` | `SELECT` | `region` |

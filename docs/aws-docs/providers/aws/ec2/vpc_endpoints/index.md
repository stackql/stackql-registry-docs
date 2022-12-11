---
title: vpc_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoints
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `routeTableIdSet` | `array` | (Gateway endpoint) One or more route tables associated with the endpoint. |
| `serviceName` | `string` | The name of the service to which the endpoint is associated. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the endpoint. |
| `groupSet` | `array` | (Interface endpoint) Information about the security groups that are associated with the network interface. |
| `dnsOptions` | `object` | Describes the DNS options for an endpoint. |
| `policyDocument` | `string` | The policy document associated with the endpoint, if applicable. |
| `state` | `string` | The state of the endpoint. |
| `networkInterfaceIdSet` | `array` | (Interface endpoint) One or more network interfaces for the endpoint. |
| `dnsEntrySet` | `array` | (Interface endpoint) The DNS entries for the endpoint. |
| `tagSet` | `array` | Any tags assigned to the endpoint. |
| `creationTimestamp` | `string` | The date and time that the endpoint was created. |
| `vpcId` | `string` | The ID of the VPC to which the endpoint is associated. |
| `ipAddressType` | `string` | The IP address type for the endpoint. |
| `vpcEndpointType` | `string` | The type of endpoint. |
| `requesterManaged` | `boolean` | Indicates whether the endpoint is being managed by its service. |
| `lastError` | `object` | The last error that occurred for a VPC endpoint. |
| `vpcEndpointId` | `string` | The ID of the endpoint. |
| `subnetIdSet` | `array` | (Interface endpoint) The subnets for the endpoint. |
| `privateDnsEnabled` | `boolean` | (Interface endpoint) Indicates whether the VPC is associated with a private hosted zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpc_endpoints_Describe` | `SELECT` |  | Describes one or more of your VPC endpoints. |
| `vpc_endpoint_Create` | `INSERT` | `ServiceName, VpcId` | Creates a VPC endpoint for a specified service. An endpoint enables you to create a private connection between your VPC and the service. The service may be provided by Amazon Web Services, an Amazon Web Services Marketplace Partner, or another Amazon Web Services account. For more information, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/privatelink/"&gt;Amazon Web Services PrivateLink Guide&lt;/a&gt;. |
| `vpc_endpoints_Delete` | `DELETE` | `VpcEndpointId` | &lt;p&gt;Deletes one or more specified VPC endpoints. You can delete any of the following types of VPC endpoints. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Gateway endpoint,&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Gateway Load Balancer endpoint,&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Interface endpoint&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following rules apply when you delete a VPC endpoint:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When you delete a gateway endpoint, we delete the endpoint routes in the route tables that are associated with the endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you delete a Gateway Load Balancer endpoint, we delete the endpoint network interfaces. &lt;/p&gt; &lt;p&gt;You can only delete Gateway Load Balancer endpoints when the routes that are associated with the endpoint are deleted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you delete an interface endpoint, we delete the endpoint network interfaces.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `vpc_endpoint_Modify` | `EXEC` | `VpcEndpointId` | Modifies attributes of a specified VPC endpoint. The attributes that you can modify depend on the type of VPC endpoint (interface, gateway, or Gateway Load Balancer). For more information, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/privatelink/"&gt;Amazon Web Services PrivateLink Guide&lt;/a&gt;. |

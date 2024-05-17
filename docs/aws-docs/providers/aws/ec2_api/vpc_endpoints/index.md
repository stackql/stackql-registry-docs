---
title: vpc_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoints
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
<tr><td><b>Name</b></td><td><code>vpc_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.vpc_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTimestamp" /> | `string` | The date and time that the endpoint was created. |
| <CopyableCode code="dnsEntrySet" /> | `array` | (Interface endpoint) The DNS entries for the endpoint. |
| <CopyableCode code="dnsOptions" /> | `object` | Describes the DNS options for an endpoint. |
| <CopyableCode code="groupSet" /> | `array` | (Interface endpoint) Information about the security groups that are associated with the network interface. |
| <CopyableCode code="ipAddressType" /> | `string` | The IP address type for the endpoint. |
| <CopyableCode code="lastError" /> | `object` | The last error that occurred for a VPC endpoint. |
| <CopyableCode code="networkInterfaceIdSet" /> | `array` | (Interface endpoint) One or more network interfaces for the endpoint. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the Amazon Web Services account that owns the endpoint. |
| <CopyableCode code="policyDocument" /> | `string` | The policy document associated with the endpoint, if applicable. |
| <CopyableCode code="privateDnsEnabled" /> | `boolean` | (Interface endpoint) Indicates whether the VPC is associated with a private hosted zone. |
| <CopyableCode code="requesterManaged" /> | `boolean` | Indicates whether the endpoint is being managed by its service. |
| <CopyableCode code="routeTableIdSet" /> | `array` | (Gateway endpoint) One or more route tables associated with the endpoint. |
| <CopyableCode code="serviceName" /> | `string` | The name of the service to which the endpoint is associated. |
| <CopyableCode code="state" /> | `string` | The state of the endpoint. |
| <CopyableCode code="subnetIdSet" /> | `array` | (Interface endpoint) The subnets for the endpoint. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the endpoint. |
| <CopyableCode code="vpcEndpointId" /> | `string` | The ID of the endpoint. |
| <CopyableCode code="vpcEndpointType" /> | `string` | The type of endpoint. |
| <CopyableCode code="vpcId" /> | `string` | The ID of the VPC to which the endpoint is associated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="vpc_endpoints_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more of your VPC endpoints. |
| <CopyableCode code="vpc_endpoint_Create" /> | `INSERT` | <CopyableCode code="ServiceName, VpcId, region" /> | Creates a VPC endpoint for a specified service. An endpoint enables you to create a private connection between your VPC and the service. The service may be provided by Amazon Web Services, an Amazon Web Services Marketplace Partner, or another Amazon Web Services account. For more information, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/privatelink/"&gt;Amazon Web Services PrivateLink Guide&lt;/a&gt;. |
| <CopyableCode code="vpc_endpoints_Delete" /> | `DELETE` | <CopyableCode code="VpcEndpointId, region" /> | &lt;p&gt;Deletes one or more specified VPC endpoints. You can delete any of the following types of VPC endpoints. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Gateway endpoint,&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Gateway Load Balancer endpoint,&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Interface endpoint&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following rules apply when you delete a VPC endpoint:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When you delete a gateway endpoint, we delete the endpoint routes in the route tables that are associated with the endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you delete a Gateway Load Balancer endpoint, we delete the endpoint network interfaces. &lt;/p&gt; &lt;p&gt;You can only delete Gateway Load Balancer endpoints when the routes that are associated with the endpoint are deleted.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you delete an interface endpoint, we delete the endpoint network interfaces.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| <CopyableCode code="vpc_endpoint_Modify" /> | `EXEC` | <CopyableCode code="VpcEndpointId, region" /> | Modifies attributes of a specified VPC endpoint. The attributes that you can modify depend on the type of VPC endpoint (interface, gateway, or Gateway Load Balancer). For more information, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/privatelink/"&gt;Amazon Web Services PrivateLink Guide&lt;/a&gt;. |

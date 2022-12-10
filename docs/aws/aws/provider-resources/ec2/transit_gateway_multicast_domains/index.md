---
title: transit_gateway_multicast_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_domains
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
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_multicast_domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `creationTime` | `string` | The time the transit gateway multicast domain was created. |
| `options` | `object` | Describes the options for a transit gateway multicast domain. |
| `ownerId` | `string` |  The ID of the Amazon Web Services account that owns the transit gateway multicast domain. |
| `state` | `string` | The state of the transit gateway multicast domain. |
| `tagSet` | `array` | The tags for the transit gateway multicast domain. |
| `transitGatewayId` | `string` | The ID of the transit gateway. |
| `transitGatewayMulticastDomainArn` | `string` | The Amazon Resource Name (ARN) of the transit gateway multicast domain. |
| `transitGatewayMulticastDomainId` | `string` | The ID of the transit gateway multicast domain. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_multicast_domains_Describe` | `SELECT` |  | Describes one or more transit gateway multicast domains. |
| `transit_gateway_multicast_domain_Create` | `INSERT` | `TransitGatewayId` | &lt;p&gt;Creates a multicast domain using the specified transit gateway.&lt;/p&gt; &lt;p&gt;The transit gateway must be in the available state before you create a domain. Use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html"&gt;DescribeTransitGateways&lt;/a&gt; to see the state of transit gateway.&lt;/p&gt; |
| `transit_gateway_multicast_domain_Delete` | `DELETE` | `TransitGatewayMulticastDomainId` | Deletes the specified transit gateway multicast domain. |
| `transit_gateway_multicast_domain_Associate` | `EXEC` |  | &lt;p&gt;Associates the specified subnets and transit gateway attachments with the specified transit gateway multicast domain.&lt;/p&gt; &lt;p&gt;The transit gateway attachment must be in the available state before you can add a resource. Use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html"&gt;DescribeTransitGatewayAttachments&lt;/a&gt; to see the state of the attachment.&lt;/p&gt; |
| `transit_gateway_multicast_domain_Disassociate` | `EXEC` |  | Disassociates the specified subnets from the transit gateway multicast domain.  |

---
title: transit_gateway_multicast_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_domains
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
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_multicast_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTime" /> | `string` | The time the transit gateway multicast domain was created. |
| <CopyableCode code="options" /> | `object` | Describes the options for a transit gateway multicast domain. |
| <CopyableCode code="ownerId" /> | `string` |  The ID of the Amazon Web Services account that owns the transit gateway multicast domain. |
| <CopyableCode code="state" /> | `string` | The state of the transit gateway multicast domain. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the transit gateway multicast domain. |
| <CopyableCode code="transitGatewayId" /> | `string` | The ID of the transit gateway. |
| <CopyableCode code="transitGatewayMulticastDomainArn" /> | `string` | The Amazon Resource Name (ARN) of the transit gateway multicast domain. |
| <CopyableCode code="transitGatewayMulticastDomainId" /> | `string` | The ID of the transit gateway multicast domain. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_multicast_domains_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more transit gateway multicast domains. |
| <CopyableCode code="transit_gateway_multicast_domain_Create" /> | `INSERT` | <CopyableCode code="TransitGatewayId, region" /> | &lt;p&gt;Creates a multicast domain using the specified transit gateway.&lt;/p&gt; &lt;p&gt;The transit gateway must be in the available state before you create a domain. Use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html"&gt;DescribeTransitGateways&lt;/a&gt; to see the state of transit gateway.&lt;/p&gt; |
| <CopyableCode code="transit_gateway_multicast_domain_Delete" /> | `DELETE` | <CopyableCode code="TransitGatewayMulticastDomainId, region" /> | Deletes the specified transit gateway multicast domain. |
| <CopyableCode code="transit_gateway_multicast_domain_Associate" /> | `EXEC` | <CopyableCode code="region" /> | &lt;p&gt;Associates the specified subnets and transit gateway attachments with the specified transit gateway multicast domain.&lt;/p&gt; &lt;p&gt;The transit gateway attachment must be in the available state before you can add a resource. Use &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html"&gt;DescribeTransitGatewayAttachments&lt;/a&gt; to see the state of the attachment.&lt;/p&gt; |
| <CopyableCode code="transit_gateway_multicast_domain_Disassociate" /> | `EXEC` | <CopyableCode code="region" /> | Disassociates the specified subnets from the transit gateway multicast domain.  |

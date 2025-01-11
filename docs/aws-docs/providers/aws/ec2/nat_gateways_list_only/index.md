---
title: nat_gateways_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateways_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>nat_gateways</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/nat_gateways/"><code>nat_gateways</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nat_gateways_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a network address translation (NAT) gateway in the specified subnet. You can create either a public NAT gateway or a private NAT gateway. The default is a public NAT gateway. If you create a public NAT gateway, you must specify an elastic IP address.<br />With a NAT gateway, instances in a private subnet can connect to the internet, other AWS services, or an on-premises network using the IP address of the NAT gateway. For more information, see &#91;NAT gateways&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*.<br />If you add a default route (<code>AWS::EC2::Route</code> resource) that points to a NAT gateway, specify the NAT gateway ID for the route's <code>NatGatewayId</code> property.<br />When you associate an Elastic IP address or secondary Elastic IP address with a public NAT gateway, the network border group of the Elastic IP address must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. Otherwise, the NAT gateway fails to launch. You can see the network border group for the AZ by viewing the details of the subnet. Similarly, you can view the network border group for the Elastic IP address by viewing its details. For more information, see &#91;Allocate an Elastic IP address&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#allocate-eip) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.nat_gateways_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="nat_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>nat_gateways</code> in a region.
```sql
SELECT
region,
nat_gateway_id
FROM aws.ec2.nat_gateways_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>nat_gateways_list_only</code> resource, see <a href="/providers/aws/ec2/nat_gateways/#permissions"><code>nat_gateways</code></a>


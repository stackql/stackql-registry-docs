---
title: vpc_endpoints_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoints_list_only
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

Lists <code>vpc_endpoints</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/vpc_endpoints/"><code>vpc_endpoints</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoints_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a VPC endpoint. A VPC endpoint provides a private connection between your VPC and an endpoint service. You can use an endpoint service provided by AWS, an MKT Partner, or another AWS accounts in your organization. For more information, see the &#91;User Guide&#93;(https://docs.aws.amazon.com/vpc/latest/privatelink/).<br />An endpoint of type <code>Interface</code> establishes connections between the subnets in your VPC and an AWS-service, your own service, or a service hosted by another AWS-account. With an interface VPC endpoint, you specify the subnets in which to create the endpoint and the security groups to associate with the endpoint network interfaces.<br />An endpoint of type <code>gateway</code> serves as a target for a route in your route table for traffic destined for S3 or DDB. You can specify an endpoint policy for the endpoint, which controls access to the service from your VPC. You can also specify the VPC route tables that use the endpoint. For more information about connectivity to S3, see &#91;Why can't I connect to an S3 bucket using a gateway VPC endpoint?&#93;(https://docs.aws.amazon.com/premiumsupport/knowledge-center/connect-s3-vpc-endpoint) <br />An endpoint of type <code>GatewayLoadBalancer</code> provides private connectivity between your VPC and virtual appliances from a service provider.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_endpoints_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>vpc_endpoints</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.vpc_endpoints_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_endpoints_list_only</code> resource, see <a href="/providers/aws/ec2/vpc_endpoints/#permissions"><code>vpc_endpoints</code></a>


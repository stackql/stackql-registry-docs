---
title: vpc_gateway_attachments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_gateway_attachments_list_only
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

Lists <code>vpc_gateway_attachments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/vpc_gateway_attachments/"><code>vpc_gateway_attachments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_gateway_attachments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCGatewayAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_gateway_attachments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="attachment_type" /></td><td><code>string</code></td><td>Used to identify if this resource is an Internet Gateway or Vpn Gateway Attachment</td></tr>
<tr><td><CopyableCode code="internet_gateway_id" /></td><td><code>string</code></td><td>The ID of the internet gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><CopyableCode code="vpn_gateway_id" /></td><td><code>string</code></td><td>The ID of the virtual private gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.</td></tr>
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
Lists all <code>vpc_gateway_attachments</code> in a region.
```sql
SELECT
region,
attachment_type,
vpc_id
FROM aws.ec2.vpc_gateway_attachments_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_gateway_attachments_list_only</code> resource, see <a href="/providers/aws/ec2/vpc_gateway_attachments/#permissions"><code>vpc_gateway_attachments</code></a>



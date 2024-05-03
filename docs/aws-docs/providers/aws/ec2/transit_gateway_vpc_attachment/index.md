---
title: transit_gateway_vpc_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_vpc_attachment
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

Gets or operates on an individual <code>transit_gateway_vpc_attachment</code> resource, use <code>transit_gateway_vpc_attachments</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_vpc_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGatewayVpcAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_vpc_attachment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="options" /></td><td><code>object</code></td><td>The options for the transit gateway vpc attachment.</td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="remove_subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="add_subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
options,
transit_gateway_id,
vpc_id,
remove_subnet_ids,
id,
subnet_ids,
add_subnet_ids,
tags
FROM aws.ec2.transit_gateway_vpc_attachment
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>transit_gateway_vpc_attachment</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeTransitGatewayAttachments,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:CreateTransitGatewayVpcAttachment,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeTags,
ec2:DescribeTransitGatewayAttachments,
ec2:ModifyTransitGatewayVpcAttachment
```

### Update
```json
ec2:DescribeTransitGatewayAttachments,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:DescribeTags,
ec2:CreateTransitGatewayVpcAttachment,
ec2:CreateTags,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:DeleteTags,
ec2:ModifyTransitGatewayVpcAttachment
```

### Delete
```json
ec2:DescribeTransitGatewayAttachments,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:CreateTransitGatewayVpcAttachment,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeTags,
ec2:DescribeTransitGatewayAttachments,
ec2:ModifyTransitGatewayVpcAttachment
```


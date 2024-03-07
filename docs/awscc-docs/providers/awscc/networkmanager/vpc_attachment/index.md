---
title: vpc_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_attachment
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vpc_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_attachment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkmanager.vpc_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>core_network_id</code></td><td><code>string</code></td><td>The ID of a core network for the VPC attachment.</td></tr>
<tr><td><code>core_network_arn</code></td><td><code>string</code></td><td>The ARN of a core network for the VPC attachment.</td></tr>
<tr><td><code>attachment_id</code></td><td><code>string</code></td><td>Id of the attachment.</td></tr>
<tr><td><code>owner_account_id</code></td><td><code>string</code></td><td>Owner account of the attachment.</td></tr>
<tr><td><code>attachment_type</code></td><td><code>string</code></td><td>Attachment type.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>State of the attachment.</td></tr>
<tr><td><code>edge_location</code></td><td><code>string</code></td><td>The Region where the edge is located.</td></tr>
<tr><td><code>vpc_arn</code></td><td><code>string</code></td><td>The ARN of the VPC.</td></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td>The ARN of the Resource.</td></tr>
<tr><td><code>attachment_policy_rule_number</code></td><td><code>integer</code></td><td>The policy rule number associated with the attachment.</td></tr>
<tr><td><code>segment_name</code></td><td><code>string</code></td><td>The name of the segment attachment..</td></tr>
<tr><td><code>proposed_segment_change</code></td><td><code>object</code></td><td>The attachment to move from one segment to another.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags for the attachment.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>Creation time of the attachment.</td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td>Last update time of the attachment.</td></tr>
<tr><td><code>subnet_arns</code></td><td><code>array</code></td><td>Subnet Arn list</td></tr>
<tr><td><code>options</code></td><td><code>object</code></td><td>Vpc options of the attachment.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
core_network_id,
core_network_arn,
attachment_id,
owner_account_id,
attachment_type,
state,
edge_location,
vpc_arn,
resource_arn,
attachment_policy_rule_number,
segment_name,
proposed_segment_change,
tags,
created_at,
updated_at,
subnet_arns,
options
FROM awscc.networkmanager.vpc_attachment
WHERE region = 'us-east-1'
AND data__Identifier = '{AttachmentId}';
```

## Permissions

To operate on the <code>vpc_attachment</code> resource, the following permissions are required:

### Read
```json
networkmanager:GetVpcAttachment
```

### Update
```json
networkmanager:UpdateVpcAttachment,
networkmanager:GetVpcAttachment,
networkmanager:ListTagsForResource,
networkmanager:TagResource,
networkmanager:UntagResource,
ec2:DescribeRegions
```

### Delete
```json
networkmanager:DeleteAttachment,
networkmanager:GetVpcAttachment,
networkmanager:UntagResource,
ec2:DescribeRegions
```


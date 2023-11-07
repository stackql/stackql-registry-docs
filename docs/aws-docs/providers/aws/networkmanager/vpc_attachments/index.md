---
title: vpc_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_attachments
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
Retrieves a list of <code>vpc_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_attachments</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.vpc_attachments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CoreNetworkId</code></td><td><code>string</code></td><td>The ID of a core network for the VPC attachment.</td></tr>
<tr><td><code>CoreNetworkArn</code></td><td><code>string</code></td><td>The ARN of a core network for the VPC attachment.</td></tr>
<tr><td><code>AttachmentId</code></td><td><code>string</code></td><td>Id of the attachment.</td></tr>
<tr><td><code>OwnerAccountId</code></td><td><code>string</code></td><td>Owner account of the attachment.</td></tr>
<tr><td><code>AttachmentType</code></td><td><code>string</code></td><td>Attachment type.</td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td>State of the attachment.</td></tr>
<tr><td><code>EdgeLocation</code></td><td><code>string</code></td><td>The Region where the edge is located.</td></tr>
<tr><td><code>VpcArn</code></td><td><code>string</code></td><td>The ARN of the VPC.</td></tr>
<tr><td><code>ResourceArn</code></td><td><code>string</code></td><td>The ARN of the Resource.</td></tr>
<tr><td><code>AttachmentPolicyRuleNumber</code></td><td><code>integer</code></td><td>The policy rule number associated with the attachment.</td></tr>
<tr><td><code>SegmentName</code></td><td><code>string</code></td><td>The name of the segment attachment..</td></tr>
<tr><td><code>ProposedSegmentChange</code></td><td><code>undefined</code></td><td>The attachment to move from one segment to another.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Tags for the attachment.</td></tr>
<tr><td><code>CreatedAt</code></td><td><code>string</code></td><td>Creation time of the attachment.</td></tr>
<tr><td><code>UpdatedAt</code></td><td><code>string</code></td><td>Last update time of the attachment.</td></tr>
<tr><td><code>SubnetArns</code></td><td><code>array</code></td><td>Subnet Arn list</td></tr>
<tr><td><code>Options</code></td><td><code>undefined</code></td><td>Vpc options of the attachment.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.networkmanager.vpc_attachments<br/>WHERE region = 'us-east-1'
</pre>

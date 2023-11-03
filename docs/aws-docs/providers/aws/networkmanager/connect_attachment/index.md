---
title: connect_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - connect_attachment
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
Gets an individual <code>connect_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connect_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.connect_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CoreNetworkId</code></td><td><code>string</code></td><td>ID of the CoreNetwork that the attachment will be attached to.</td></tr><tr><td><code>CoreNetworkArn</code></td><td><code>string</code></td><td>The ARN of a core network for the VPC attachment.</td></tr><tr><td><code>AttachmentId</code></td><td><code>string</code></td><td>The ID of the attachment.</td></tr><tr><td><code>OwnerAccountId</code></td><td><code>string</code></td><td>The ID of the attachment account owner.</td></tr><tr><td><code>AttachmentType</code></td><td><code>string</code></td><td>The type of attachment.</td></tr><tr><td><code>State</code></td><td><code>string</code></td><td>State of the attachment.</td></tr><tr><td><code>EdgeLocation</code></td><td><code>string</code></td><td>Edge location of the attachment.</td></tr><tr><td><code>ResourceArn</code></td><td><code>string</code></td><td>The attachment resource ARN.</td></tr><tr><td><code>AttachmentPolicyRuleNumber</code></td><td><code>integer</code></td><td>The policy rule number associated with the attachment.</td></tr><tr><td><code>SegmentName</code></td><td><code>string</code></td><td>The name of the segment attachment.</td></tr><tr><td><code>ProposedSegmentChange</code></td><td><code>undefined</code></td><td>The attachment to move from one segment to another.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Tags for the attachment.</td></tr><tr><td><code>CreatedAt</code></td><td><code>string</code></td><td>Creation time of the attachment.</td></tr><tr><td><code>UpdatedAt</code></td><td><code>string</code></td><td>Last update time of the attachment.</td></tr><tr><td><code>TransportAttachmentId</code></td><td><code>string</code></td><td>Id of transport attachment</td></tr><tr><td><code>Options</code></td><td><code>undefined</code></td><td>Protocol options for connect attachment</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.networkmanager.connect_attachment
WHERE region = 'us-east-1' AND data__Identifier = '{AttachmentId}'
</pre>

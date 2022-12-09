---
title: transit_gateway_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_attachments
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
<tr><td><b>Name</b></td><td><code>transit_gateway_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_attachments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceOwnerId` | `string` | The ID of the Amazon Web Services account that owns the resource. |
| `resourceId` | `string` | The ID of the resource. |
| `transitGatewayAttachmentId` | `string` | The ID of the attachment. |
| `tagSet` | `array` | The tags for the attachment. |
| `transitGatewayOwnerId` | `string` | The ID of the Amazon Web Services account that owns the transit gateway. |
| `association` | `object` | Describes an association. |
| `transitGatewayId` | `string` | The ID of the transit gateway. |
| `resourceType` | `string` | The resource type. Note that the &lt;code&gt;tgw-peering&lt;/code&gt; resource type has been deprecated. |
| `creationTime` | `string` | The creation time. |
| `state` | `string` | The attachment state. Note that the &lt;code&gt;initiating&lt;/code&gt; state has been deprecated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `transit_gateway_attachments_Describe` | `SELECT` |  |

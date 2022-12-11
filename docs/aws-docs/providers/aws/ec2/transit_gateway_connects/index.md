---
title: transit_gateway_connects
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_connects
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
<tr><td><b>Name</b></td><td><code>transit_gateway_connects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_connects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `transitGatewayId` | `string` | The ID of the transit gateway. |
| `transportTransitGatewayAttachmentId` | `string` | The ID of the attachment from which the Connect attachment was created. |
| `creationTime` | `string` | The creation time. |
| `options` | `object` | Describes the Connect attachment options. |
| `state` | `string` | The state of the attachment. |
| `tagSet` | `array` | The tags for the attachment. |
| `transitGatewayAttachmentId` | `string` | The ID of the Connect attachment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_connects_Describe` | `SELECT` |  | Describes one or more Connect attachments. |
| `transit_gateway_connect_Create` | `INSERT` | `Options, TransportTransitGatewayAttachmentId` | &lt;p&gt;Creates a Connect attachment from a specified transit gateway attachment. A Connect attachment is a GRE-based tunnel attachment that you can use to establish a connection between a transit gateway and an appliance.&lt;/p&gt; &lt;p&gt;A Connect attachment uses an existing VPC or Amazon Web Services Direct Connect attachment as the underlying transport mechanism.&lt;/p&gt; |
| `transit_gateway_connect_Delete` | `DELETE` | `TransitGatewayAttachmentId` | Deletes the specified Connect attachment. You must first delete any Connect peers for the attachment. |

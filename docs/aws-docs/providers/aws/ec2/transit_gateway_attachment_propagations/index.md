---
title: transit_gateway_attachment_propagations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_attachment_propagations
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_attachment_propagations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_attachment_propagations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `state` | `string` | The state of the propagation route table. |
| `transitGatewayRouteTableId` | `string` | The ID of the propagation route table. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `transit_gateway_attachment_propagations_Get` | `SELECT` | `TransitGatewayAttachmentId, region` |

---
title: egress_only_internet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - egress_only_internet_gateways
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
<tr><td><b>Name</b></td><td><code>egress_only_internet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.egress_only_internet_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tagSet` | `array` | The tags assigned to the egress-only internet gateway. |
| `attachmentSet` | `array` | Information about the attachment of the egress-only internet gateway. |
| `egressOnlyInternetGatewayId` | `string` | The ID of the egress-only internet gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `egress_only_internet_gateways_Describe` | `SELECT` |  | Describes one or more of your egress-only internet gateways. |
| `egress_only_internet_gateway_Create` | `INSERT` | `VpcId` | [IPv6 only] Creates an egress-only internet gateway for your VPC. An egress-only internet gateway is used to enable outbound communication over IPv6 from instances in your VPC to the internet, and prevents hosts outside of your VPC from initiating an IPv6 connection with your instance. |
| `egress_only_internet_gateway_Delete` | `DELETE` | `EgressOnlyInternetGatewayId` | Deletes an egress-only internet gateway. |

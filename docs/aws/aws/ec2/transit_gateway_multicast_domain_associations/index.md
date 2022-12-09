---
title: transit_gateway_multicast_domain_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_domain_associations
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
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_domain_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_multicast_domain_associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceId` | `string` | The ID of the resource. |
| `resourceOwnerId` | `string` |  The ID of the Amazon Web Services account that owns the transit gateway multicast domain association resource. |
| `resourceType` | `string` | The type of resource, for example a VPC attachment. |
| `subnet` | `object` | Describes the subnet association with the transit gateway multicast domain. |
| `transitGatewayAttachmentId` | `string` | The ID of the transit gateway attachment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `transit_gateway_multicast_domain_associations_Get` | `SELECT` |  | Gets information about the associations for the transit gateway multicast domain. |
| `transit_gateway_multicast_domain_associations_Accept` | `EXEC` |  | Accepts a request to associate subnets with a transit gateway multicast domain. |
| `transit_gateway_multicast_domain_associations_Reject` | `EXEC` |  | Rejects a request to associate cross-account subnets with a transit gateway multicast domain. |

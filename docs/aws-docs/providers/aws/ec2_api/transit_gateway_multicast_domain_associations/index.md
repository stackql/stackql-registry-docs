---
title: transit_gateway_multicast_domain_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_domain_associations
  - ec2_api
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_domain_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_multicast_domain_associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resourceId" /> | `string` | The ID of the resource. |
| <CopyableCode code="resourceOwnerId" /> | `string` |  The ID of the Amazon Web Services account that owns the transit gateway multicast domain association resource. |
| <CopyableCode code="resourceType" /> | `string` | The type of resource, for example a VPC attachment. |
| <CopyableCode code="subnet" /> | `object` | Describes the subnet association with the transit gateway multicast domain. |
| <CopyableCode code="transitGatewayAttachmentId" /> | `string` | The ID of the transit gateway attachment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_multicast_domain_associations_Get" /> | `SELECT` | <CopyableCode code="region" /> | Gets information about the associations for the transit gateway multicast domain. |
| <CopyableCode code="transit_gateway_multicast_domain_associations_Accept" /> | `EXEC` | <CopyableCode code="region" /> | Accepts a request to associate subnets with a transit gateway multicast domain. |
| <CopyableCode code="transit_gateway_multicast_domain_associations_Reject" /> | `EXEC` | <CopyableCode code="region" /> | Rejects a request to associate cross-account subnets with a transit gateway multicast domain. |

---
title: transit_gateway_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_attachments
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
<tr><td><b>Name</b></td><td><code>transit_gateway_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="association" /> | `object` | Describes an association. |
| <CopyableCode code="creationTime" /> | `string` | The creation time. |
| <CopyableCode code="resourceId" /> | `string` | The ID of the resource. |
| <CopyableCode code="resourceOwnerId" /> | `string` | The ID of the Amazon Web Services account that owns the resource. |
| <CopyableCode code="resourceType" /> | `string` | The resource type. Note that the &lt;code&gt;tgw-peering&lt;/code&gt; resource type has been deprecated. |
| <CopyableCode code="state" /> | `string` | The attachment state. Note that the &lt;code&gt;initiating&lt;/code&gt; state has been deprecated. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the attachment. |
| <CopyableCode code="transitGatewayAttachmentId" /> | `string` | The ID of the attachment. |
| <CopyableCode code="transitGatewayId" /> | `string` | The ID of the transit gateway. |
| <CopyableCode code="transitGatewayOwnerId" /> | `string` | The ID of the Amazon Web Services account that owns the transit gateway. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="transit_gateway_attachments_Describe" /> | `SELECT` | <CopyableCode code="region" /> |

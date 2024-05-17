---
title: transit_gateway_connects
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_connects
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
<tr><td><b>Name</b></td><td><code>transit_gateway_connects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.transit_gateway_connects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTime" /> | `string` | The creation time. |
| <CopyableCode code="options" /> | `object` | Describes the Connect attachment options. |
| <CopyableCode code="state" /> | `string` | The state of the attachment. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the attachment. |
| <CopyableCode code="transitGatewayAttachmentId" /> | `string` | The ID of the Connect attachment. |
| <CopyableCode code="transitGatewayId" /> | `string` | The ID of the transit gateway. |
| <CopyableCode code="transportTransitGatewayAttachmentId" /> | `string` | The ID of the attachment from which the Connect attachment was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="transit_gateway_connects_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more Connect attachments. |
| <CopyableCode code="transit_gateway_connect_Create" /> | `INSERT` | <CopyableCode code="Options, TransportTransitGatewayAttachmentId, region" /> | &lt;p&gt;Creates a Connect attachment from a specified transit gateway attachment. A Connect attachment is a GRE-based tunnel attachment that you can use to establish a connection between a transit gateway and an appliance.&lt;/p&gt; &lt;p&gt;A Connect attachment uses an existing VPC or Amazon Web Services Direct Connect attachment as the underlying transport mechanism.&lt;/p&gt; |
| <CopyableCode code="transit_gateway_connect_Delete" /> | `DELETE` | <CopyableCode code="TransitGatewayAttachmentId, region" /> | Deletes the specified Connect attachment. You must first delete any Connect peers for the attachment. |

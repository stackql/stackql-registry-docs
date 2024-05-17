---
title: internet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateways
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
<tr><td><b>Name</b></td><td><code>internet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.internet_gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attachmentSet" /> | `array` | Any VPCs attached to the internet gateway. |
| <CopyableCode code="internetGatewayId" /> | `string` | The ID of the internet gateway. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the Amazon Web Services account that owns the internet gateway. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the internet gateway. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="internet_gateways_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more of your internet gateways. |
| <CopyableCode code="internet_gateway_Create" /> | `INSERT` | <CopyableCode code="region" /> | &lt;p&gt;Creates an internet gateway for use with a VPC. After creating the internet gateway, you attach it to a VPC using &lt;a&gt;AttachInternetGateway&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about your VPC and internet gateway, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/"&gt;Amazon Virtual Private Cloud User Guide&lt;/a&gt;.&lt;/p&gt; |
| <CopyableCode code="internet_gateway_Delete" /> | `DELETE` | <CopyableCode code="InternetGatewayId, region" /> | Deletes the specified internet gateway. You must detach the internet gateway from the VPC before you can delete it. |
| <CopyableCode code="internet_gateway_Attach" /> | `EXEC` | <CopyableCode code="InternetGatewayId, VpcId, region" /> | Attaches an internet gateway or a virtual private gateway to a VPC, enabling connectivity between the internet and the VPC. For more information about your VPC and internet gateway, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/userguide/"&gt;Amazon Virtual Private Cloud User Guide&lt;/a&gt;. |
| <CopyableCode code="internet_gateway_Detach" /> | `EXEC` | <CopyableCode code="InternetGatewayId, VpcId, region" /> | Detaches an internet gateway from a VPC, disabling connectivity between the internet and the VPC. The VPC must not contain any running instances with Elastic IP addresses or public IPv4 addresses. |

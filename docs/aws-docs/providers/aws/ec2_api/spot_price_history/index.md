---
title: spot_price_history
hide_title: false
hide_table_of_contents: false
keywords:
  - spot_price_history
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
<tr><td><b>Name</b></td><td><code>spot_price_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.spot_price_history" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availabilityZone" /> | `string` | The Availability Zone. |
| <CopyableCode code="instanceType" /> | `string` | The instance type. |
| <CopyableCode code="productDescription" /> | `string` | A general description of the AMI. |
| <CopyableCode code="spotPrice" /> | `string` | The maximum price per hour that you are willing to pay for a Spot Instance. |
| <CopyableCode code="timestamp" /> | `string` | The date and time the request was created, in UTC format (for example, &lt;i&gt;YYYY&lt;/i&gt;-&lt;i&gt;MM&lt;/i&gt;-&lt;i&gt;DD&lt;/i&gt;T&lt;i&gt;HH&lt;/i&gt;:&lt;i&gt;MM&lt;/i&gt;:&lt;i&gt;SS&lt;/i&gt;Z). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="spot_price_history_Describe" /> | `SELECT` | <CopyableCode code="region" /> |

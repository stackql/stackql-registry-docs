---
title: coip_pool_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - coip_pool_usage
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
<tr><td><b>Name</b></td><td><code>coip_pool_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.coip_pool_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allocationId" /> | `string` | The allocation ID of the address. |
| <CopyableCode code="awsAccountId" /> | `string` | The Amazon Web Services account ID. |
| <CopyableCode code="awsService" /> | `string` | The Amazon Web Services service. |
| <CopyableCode code="coIp" /> | `string` | The customer-owned IP address. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="coip_pool_usage_Get" /> | `SELECT` | <CopyableCode code="PoolId, region" /> |

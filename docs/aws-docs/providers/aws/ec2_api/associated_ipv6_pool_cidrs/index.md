---
title: associated_ipv6_pool_cidrs
hide_title: false
hide_table_of_contents: false
keywords:
  - associated_ipv6_pool_cidrs
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
<tr><td><b>Name</b></td><td><code>associated_ipv6_pool_cidrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.associated_ipv6_pool_cidrs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associatedResource" /> | `string` | The resource that's associated with the IPv6 CIDR block. |
| <CopyableCode code="ipv6Cidr" /> | `string` | The IPv6 CIDR block. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="associated_ipv6_pool_cidrs_Get" /> | `SELECT` | <CopyableCode code="PoolId, region" /> |

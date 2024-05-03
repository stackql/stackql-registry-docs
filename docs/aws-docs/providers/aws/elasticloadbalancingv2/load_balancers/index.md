---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - elasticloadbalancingv2
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

Used to retrieve a list of <code>load_balancers</code> in a region or create a <code>load_balancers</code> resource, use <code>load_balancer</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Application Load Balancer, a Network Load Balancer, or a Gateway Load Balancer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.load_balancers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="load_balancer_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
load_balancer_arn
FROM aws.elasticloadbalancingv2.load_balancers
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>load_balancers</code> resource, the following permissions are required:

### Create
```json
elasticloadbalancing:CreateLoadBalancer,
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:ModifyLoadBalancerAttributes,
elasticloadbalancing:AddTags
```

### List
```json
elasticloadbalancing:DescribeLoadBalancers
```


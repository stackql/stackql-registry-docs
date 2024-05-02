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
Retrieves a list of <code>load_balancers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Application Load Balancer, a Network Load Balancer, or a Gateway Load Balancer.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.load_balancers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>load_balancer_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
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


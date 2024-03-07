---
title: protections
hide_title: false
hide_table_of_contents: false
keywords:
  - protections
  - shield
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>protections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>protections</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.shield.protections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>protection_arn</code></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
protection_arn
FROM awscc.shield.protections

```

## Permissions

To operate on the <code>protections</code> resource, the following permissions are required:

### Create
```json
shield:CreateProtection,
shield:DeleteProtection,
shield:DescribeProtection,
shield:ListProtections,
shield:EnableApplicationLayerAutomaticResponse,
shield:AssociateHealthCheck,
shield:TagResource,
ec2:DescribeAddresses,
elasticloadbalancing:DescribeLoadBalancers,
route53:GetHealthCheck,
iam:GetRole,
iam:CreateServiceLinkedRole,
wafv2:GetWebACLForResource,
wafv2:GetWebACL
```

### List
```json
shield:ListProtections
```


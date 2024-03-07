---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - m2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environments</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.m2.environments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>environment_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the runtime environment.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkInterface,
ec2:CreateNetworkInterfacePermission,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
ec2:ModifyNetworkInterfaceAttribute,
elasticfilesystem:DescribeMountTargets,
elasticloadbalancing:CreateLoadBalancer,
elasticloadbalancing:AddTags,
fsx:DescribeFileSystems,
iam:CreateServiceLinkedRole,
kms:DescribeKey,
kms:CreateGrant,
m2:CreateEnvironment,
m2:GetEnvironment,
m2:ListTagsForResource,
m2:TagResource
```

### List
```json
m2:ListEnvironments
```


## Example
```sql
SELECT
region,
environment_arn
FROM awscc.m2.environments
WHERE region = 'us-east-1'
```

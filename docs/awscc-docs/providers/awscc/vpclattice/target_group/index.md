---
title: target_group
hide_title: false
hide_table_of_contents: false
keywords:
  - target_group
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>target_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>target_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.vpclattice.target_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_updated_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>targets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>target_group</code> resource, the following permissions are required:

### Read
<pre>
vpc-lattice:GetTargetGroup,
vpc-lattice:ListTargets,
vpc-lattice:ListTagsForResource</pre>

### Update
<pre>
vpc-lattice:UpdateTargetGroup,
vpc-lattice:GetTargetGroup,
vpc-lattice:ListTargets,
vpc-lattice:RegisterTargets,
vpc-lattice:DeregisterTargets,
ec2:DescribeVpcs,
ec2:DescribeInstances,
ec2:DescribeSubnets,
ec2:DescribeAvailabilityZoneMappings,
elasticloadbalancing:DescribeLoadBalancers,
lambda:Invoke,
lambda:RemovePermission,
lambda:AddPermission,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:ListTagsForResource</pre>

### Delete
<pre>
vpc-lattice:DeleteTargetGroup,
vpc-lattice:GetTargetGroup,
vpc-lattice:DeregisterTargets,
vpc-lattice:ListTargets,
lambda:RemovePermission</pre>


## Example
```sql
SELECT
region,
arn,
config,
created_at,
id,
last_updated_at,
name,
status,
type,
targets,
tags
FROM awscc.vpclattice.target_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```

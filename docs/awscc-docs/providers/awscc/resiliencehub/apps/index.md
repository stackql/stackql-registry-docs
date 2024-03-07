---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - resiliencehub
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>apps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>apps</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.resiliencehub.apps</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>app_arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the App.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>apps</code> resource, the following permissions are required:

### Create
```json
cloudformation:DescribeStacks,
cloudformation:ListStackResources,
s3:GetBucketLocation,
s3:GetObject,
s3:ListAllMyBuckets,
autoscaling:DescribeAutoScalingGroups,
apigateway:GET,
ec2:Describe*,
ecs:DescribeServices,
eks:DescribeCluster,
elasticfilesystem:DescribeFileSystems,
elasticloadbalancing:DescribeLoadBalancers,
lambda:GetFunction*,
rds:Describe*,
dynamodb:Describe*,
sqs:GetQueueAttributes,
sns:GetTopicAttributes,
route53:List*,
iam:PassRole,
resiliencehub:*
```

### List
```json
resiliencehub:ListApps
```


## Example
```sql
SELECT
region,
app_arn
FROM awscc.resiliencehub.apps
WHERE region = 'us-east-1'
```

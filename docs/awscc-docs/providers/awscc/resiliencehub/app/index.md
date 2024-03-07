---
title: app
hide_title: false
hide_table_of_contents: false
keywords:
  - app
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
Gets an individual <code>app</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.resiliencehub.app</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the app.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>App description.</td></tr>
<tr><td><code>app_arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the App.</td></tr>
<tr><td><code>resiliency_policy_arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Resiliency Policy.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>app_template_body</code></td><td><code>string</code></td><td>A string containing full ResilienceHub app template body.</td></tr>
<tr><td><code>resource_mappings</code></td><td><code>array</code></td><td>An array of ResourceMapping objects.</td></tr>
<tr><td><code>app_assessment_schedule</code></td><td><code>string</code></td><td>Assessment execution schedule.</td></tr>
<tr><td><code>permission_model</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>event_subscriptions</code></td><td><code>array</code></td><td>The list of events you would like to subscribe and get notification for.</td></tr>
<tr><td><code>drift_status</code></td><td><code>string</code></td><td>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>app</code> resource, the following permissions are required:

### Read
<pre>
resiliencehub:DescribeApp,
resiliencehub:DescribeAppVersionTemplate,
resiliencehub:ListAppVersionResourceMappings,
resiliencehub:ListTagsForResource</pre>

### Update
<pre>
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
resiliencehub:*</pre>

### Delete
<pre>
resiliencehub:DeleteApp,
resiliencehub:UntagResource,
resiliencehub:ListApps</pre>


## Example
```sql
SELECT
region,
name,
description,
app_arn,
resiliency_policy_arn,
tags,
app_template_body,
resource_mappings,
app_assessment_schedule,
permission_model,
event_subscriptions,
drift_status
FROM awscc.resiliencehub.app
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AppArn&gt;'
```

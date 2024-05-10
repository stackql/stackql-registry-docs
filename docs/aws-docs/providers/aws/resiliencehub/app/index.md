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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>app</code> resource, use <code>apps</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::ResilienceHub::App.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resiliencehub.app" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the app.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>App description.</td></tr>
<tr><td><CopyableCode code="app_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the App.</td></tr>
<tr><td><CopyableCode code="resiliency_policy_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Resiliency Policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="app_template_body" /></td><td><code>string</code></td><td>A string containing full ResilienceHub app template body.</td></tr>
<tr><td><CopyableCode code="resource_mappings" /></td><td><code>array</code></td><td>An array of ResourceMapping objects.</td></tr>
<tr><td><CopyableCode code="app_assessment_schedule" /></td><td><code>string</code></td><td>Assessment execution schedule.</td></tr>
<tr><td><CopyableCode code="permission_model" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="event_subscriptions" /></td><td><code>array</code></td><td>The list of events you would like to subscribe and get notification for.</td></tr>
<tr><td><CopyableCode code="drift_status" /></td><td><code>string</code></td><td>Indicates if compliance drifts (deviations) were detected while running an assessment for your application.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.resiliencehub.app
WHERE region = 'us-east-1' AND data__Identifier = '<AppArn>';
```


## Permissions

To operate on the <code>app</code> resource, the following permissions are required:

### Read
```json
resiliencehub:DescribeApp,
resiliencehub:DescribeAppVersionTemplate,
resiliencehub:ListAppVersionResourceMappings,
resiliencehub:ListTagsForResource
```

### Update
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


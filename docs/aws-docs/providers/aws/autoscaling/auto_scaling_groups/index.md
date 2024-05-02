---
title: auto_scaling_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scaling_groups
  - autoscaling
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>auto_scaling_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::AutoScaling::AutoScalingGroup`` resource defines an Amazon EC2 Auto Scaling group, which is a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. &lt;br&#x2F;&gt; For more information about Amazon EC2 Auto Scaling, see the &#91;Amazon EC2 Auto Scaling User Guide&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;what-is-amazon-ec2-auto-scaling.html). &lt;br&#x2F;&gt;  Amazon EC2 Auto Scaling configures instances launched as part of an Auto Scaling group using either a &#91;launch template&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-ec2-launchtemplate.html) or a launch configuration. We strongly recommend that you do not use launch configurations. They do not provide full functionality for Amazon EC2 Auto Scaling or Amazon EC2. For more information, see &#91;Launch configurations&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;launch-configurations.html) and &#91;Migrate CloudFormation stacks from launch configurations to launch templates&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;autoscaling&#x2F;ec2&#x2F;userguide&#x2F;migrate-launch-configurations-with-cloudformation.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.autoscaling.auto_scaling_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>auto_scaling_group_name</code></td><td><code>string</code></td><td>The name of the Auto Scaling group. This name must be unique per Region per account.&lt;br&#x2F;&gt; The name can contain any ASCII character 33 to 126 including most punctuation characters, digits, and upper and lowercased letters.&lt;br&#x2F;&gt;  You cannot use a colon (:) in the name.</td></tr>
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
auto_scaling_group_name
FROM aws.autoscaling.auto_scaling_groups
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>auto_scaling_groups</code> resource, the following permissions are required:

### Create
```json
autoscaling:CreateAutoScalingGroup,
autoscaling:UpdateAutoScalingGroup,
autoscaling:CreateOrUpdateTags,
autoscaling:Describe*,
autoscaling:EnableMetricsCollection,
autoscaling:PutNotificationConfiguration,
cloudwatch:PutMetricAlarm,
ec2:Describe*,
ec2:Get*,
ec2:RunInstances,
elasticloadbalancing:Describe*,
iam:CreateServiceLinkedRole,
iam:PassRole,
managed-fleets:Get*,
managed-fleets:CreateAutoScalingGroup,
managed-fleets:UpdateAutoScalingGroup,
ssm:Get*
```

### List
```json
autoscaling:Describe*
```


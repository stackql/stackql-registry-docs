---
title: scaling_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_policy
  - applicationautoscaling
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


Gets or updates an individual <code>scaling_policy</code> resource, use <code>scaling_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApplicationAutoScaling::ScalingPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationautoscaling.scaling_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name of the scaling policy.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Updates to the name of a target tracking scaling policy are not supported, unless you also update the metric used for scaling. To change only a target tracking scaling policy's name, first delete the policy by removing the existing AWS::ApplicationAutoScaling::ScalingPolicy resource from the template and updating the stack. Then, recreate the resource with the same settings and a different name.</td></tr>
<tr><td><CopyableCode code="policy_type" /></td><td><code>string</code></td><td>The scaling policy type.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The following policy types are supported:&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;TargetTrackingScaling Not supported for Amazon EMR&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;StepScaling Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.</td></tr>
<tr><td><CopyableCode code="scalable_dimension" /></td><td><code>string</code></td><td>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</td></tr>
<tr><td><CopyableCode code="scaling_target_id" /></td><td><code>string</code></td><td>The CloudFormation-generated ID of an Application Auto Scaling scalable target. For more information about the ID, see the Return Value section of the AWS::ApplicationAutoScaling::ScalableTarget resource.</td></tr>
<tr><td><CopyableCode code="service_namespace" /></td><td><code>string</code></td><td>The namespace of the AWS service that provides the resource, or a custom-resource.</td></tr>
<tr><td><CopyableCode code="step_scaling_policy_configuration" /></td><td><code>object</code></td><td>A step scaling policy.</td></tr>
<tr><td><CopyableCode code="target_tracking_scaling_policy_configuration" /></td><td><code>object</code></td><td>A target tracking scaling policy.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN is a read only property for the resource.</td></tr>
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
policy_name,
policy_type,
resource_id,
scalable_dimension,
scaling_target_id,
service_namespace,
step_scaling_policy_configuration,
target_tracking_scaling_policy_configuration,
arn
FROM aws.applicationautoscaling.scaling_policy
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>|<ScalableDimension>';
```


## Permissions

To operate on the <code>scaling_policy</code> resource, the following permissions are required:

### Read
```json
application-autoscaling:DescribeScalingPolicies
```

### Update
```json
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:PutScalingPolicy
```


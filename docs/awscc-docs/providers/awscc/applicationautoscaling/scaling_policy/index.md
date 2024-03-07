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
Gets an individual <code>scaling_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scaling_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.applicationautoscaling.scaling_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy_name</code></td><td><code>string</code></td><td>The name of the scaling policy.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Updates to the name of a target tracking scaling policy are not supported, unless you also update the metric used for scaling. To change only a target tracking scaling policy's name, first delete the policy by removing the existing AWS::ApplicationAutoScaling::ScalingPolicy resource from the template and updating the stack. Then, recreate the resource with the same settings and a different name.</td></tr>
<tr><td><code>policy_type</code></td><td><code>string</code></td><td>The scaling policy type.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The following policy types are supported:&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;TargetTrackingScaling Not supported for Amazon EMR&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;StepScaling Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.</td></tr>
<tr><td><code>scalable_dimension</code></td><td><code>string</code></td><td>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</td></tr>
<tr><td><code>scaling_target_id</code></td><td><code>string</code></td><td>The CloudFormation-generated ID of an Application Auto Scaling scalable target. For more information about the ID, see the Return Value section of the AWS::ApplicationAutoScaling::ScalableTarget resource.</td></tr>
<tr><td><code>service_namespace</code></td><td><code>string</code></td><td>The namespace of the AWS service that provides the resource, or a custom-resource.</td></tr>
<tr><td><code>step_scaling_policy_configuration</code></td><td><code>object</code></td><td>A step scaling policy.</td></tr>
<tr><td><code>target_tracking_scaling_policy_configuration</code></td><td><code>object</code></td><td>A target tracking scaling policy.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>ARN is a read only property for the resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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

### Delete
```json
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeleteScalingPolicy
```


## Example
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
FROM awscc.applicationautoscaling.scaling_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
AND data__Identifier = '&lt;ScalableDimension&gt;'
```

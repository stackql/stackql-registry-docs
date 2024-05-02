---
title: scalable_target
hide_title: false
hide_table_of_contents: false
keywords:
  - scalable_target
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
Gets or operates on an individual <code>scalable_target</code> resource, use <code>scalable_targets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scalable_target</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApplicationAutoScaling::ScalableTarget</td></tr>
<tr><td><b>Id</b></td><td><code>aws.applicationautoscaling.scalable_target</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>This value can be returned by using the Ref function. Ref returns the Cloudformation generated ID of the resource in format - ResourceId|ScalableDimension|ServiceNamespace</td></tr>
<tr><td><code>max_capacity</code></td><td><code>integer</code></td><td>The maximum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand</td></tr>
<tr><td><code>min_capacity</code></td><td><code>integer</code></td><td>The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>The identifier of the resource associated with the scalable target</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf. </td></tr>
<tr><td><code>scalable_dimension</code></td><td><code>string</code></td><td>The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property</td></tr>
<tr><td><code>scheduled_actions</code></td><td><code>array</code></td><td>The scheduled actions for the scalable target. Duplicates aren't allowed.</td></tr>
<tr><td><code>service_namespace</code></td><td><code>string</code></td><td>The namespace of the AWS service that provides the resource, or a custom-resource</td></tr>
<tr><td><code>suspended_state</code></td><td><code>object</code></td><td>An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to true suspends the specified scaling activities. Setting it to false (default) resumes the specified scaling activities.</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
max_capacity,
min_capacity,
resource_id,
role_arn,
scalable_dimension,
scheduled_actions,
service_namespace,
suspended_state
FROM aws.applicationautoscaling.scalable_target
WHERE data__Identifier = '<ResourceId>|<ScalableDimension>|<ServiceNamespace>';
```

## Permissions

To operate on the <code>scalable_target</code> resource, the following permissions are required:

### Read
```json
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScheduledActions
```

### Update
```json
application-autoscaling:RegisterScalableTarget,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScheduledActions,
application-autoscaling:DeleteScheduledAction,
application-autoscaling:PutScheduledAction,
cloudwatch:PutMetricAlarm,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
lambda:GetProvisionedConcurrencyConfig,
lambda:PutProvisionedConcurrencyConfig,
lambda:DeleteProvisionedConcurrencyConfig
```

### Delete
```json
application-autoscaling:DeregisterScalableTarget
```


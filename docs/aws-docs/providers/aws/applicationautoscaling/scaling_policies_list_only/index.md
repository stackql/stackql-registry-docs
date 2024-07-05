---
title: scaling_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_policies_list_only
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

Lists <code>scaling_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/scaling_policies/"><code>scaling_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ApplicationAutoScaling::ScalingPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationautoscaling.scaling_policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name of the scaling policy.<br />Updates to the name of a target tracking scaling policy are not supported, unless you also update the metric used for scaling. To change only a target tracking scaling policy's name, first delete the policy by removing the existing AWS::ApplicationAutoScaling::ScalingPolicy resource from the template and updating the stack. Then, recreate the resource with the same settings and a different name.</td></tr>
<tr><td><CopyableCode code="policy_type" /></td><td><code>string</code></td><td>The scaling policy type.<br />The following policy types are supported:<br />TargetTrackingScaling Not supported for Amazon EMR<br />StepScaling Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>scaling_policies</code> in a region.
```sql
SELECT
region,
arn,
scalable_dimension
FROM aws.applicationautoscaling.scaling_policies_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>scaling_policies_list_only</code> resource, see <a href="/providers/aws/applicationautoscaling/scaling_policies/#permissions"><code>scaling_policies</code></a>



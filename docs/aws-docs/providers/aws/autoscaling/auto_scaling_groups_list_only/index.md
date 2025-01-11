---
title: auto_scaling_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scaling_groups_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>auto_scaling_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/auto_scaling_groups/"><code>auto_scaling_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>auto_scaling_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::AutoScaling::AutoScalingGroup</code> resource defines an Amazon EC2 Auto Scaling group, which is a collection of Amazon EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. <br />For more information about Amazon EC2 Auto Scaling, see the &#91;Amazon EC2 Auto Scaling User Guide&#93;(https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html). <br />Amazon EC2 Auto Scaling configures instances launched as part of an Auto Scaling group using either a &#91;launch template&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html) or a launch configuration. We strongly recommend that you do not use launch configurations. For more information, see &#91;Launch configurations&#93;(https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-configurations.html) in the *Amazon EC2 Auto Scaling User Guide*.<br />For help migrating from launch configurations to launch templates, see &#91;Migrate CloudFormation stacks from launch configurations to launch templates&#93;(https://docs.aws.amazon.com/autoscaling/ec2/userguide/migrate-launch-configurations-with-cloudformation.html) in the *Amazon EC2 Auto Scaling User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.auto_scaling_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="auto_scaling_group_name" /></td><td><code>string</code></td><td>The name of the Auto Scaling group. This name must be unique per Region per account.<br />The name can contain any ASCII character 33 to 126 including most punctuation characters, digits, and upper and lowercased letters.<br />You cannot use a colon (:) in the name.</td></tr>
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
Lists all <code>auto_scaling_groups</code> in a region.
```sql
SELECT
region,
auto_scaling_group_name
FROM aws.autoscaling.auto_scaling_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>auto_scaling_groups_list_only</code> resource, see <a href="/providers/aws/autoscaling/auto_scaling_groups/#permissions"><code>auto_scaling_groups</code></a>


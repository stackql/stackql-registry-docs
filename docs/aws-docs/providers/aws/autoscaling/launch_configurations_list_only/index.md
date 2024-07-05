---
title: launch_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_configurations_list_only
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

Lists <code>launch_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/launch_configurations/"><code>launch_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AutoScaling::LaunchConfiguration resource specifies the launch configuration that can be used by an Auto Scaling group to configure Amazon EC2 instances.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.autoscaling.launch_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="placement_tenancy" /></td><td><code>string</code></td><td>The tenancy of the instance, either default or dedicated.</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td>A list that contains the security groups to assign to the instances in the Auto Scaling group.</td></tr>
<tr><td><CopyableCode code="launch_configuration_name" /></td><td><code>string</code></td><td>The name of the launch configuration. This name must be unique per Region per account.</td></tr>
<tr><td><CopyableCode code="metadata_options" /></td><td><code>object</code></td><td>The metadata options for the instances.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the Amazon EC2 instance you want to use to create the launch configuration.</td></tr>
<tr><td><CopyableCode code="user_data" /></td><td><code>string</code></td><td>The Base64-encoded user data to make available to the launched EC2 instances.</td></tr>
<tr><td><CopyableCode code="classic_link_vpc_security_groups" /></td><td><code>array</code></td><td>The IDs of one or more security groups for the VPC that you specified in the ClassicLinkVPCId property.</td></tr>
<tr><td><CopyableCode code="block_device_mappings" /></td><td><code>array</code></td><td>Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes.</td></tr>
<tr><td><CopyableCode code="iam_instance_profile" /></td><td><code>string</code></td><td>Provides the name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.</td></tr>
<tr><td><CopyableCode code="kernel_id" /></td><td><code>string</code></td><td>Provides the ID of the kernel associated with the EC2 AMI.</td></tr>
<tr><td><CopyableCode code="associate_public_ip_address" /></td><td><code>boolean</code></td><td>For Auto Scaling groups that are running in a virtual private cloud (VPC), specifies whether to assign a public IP address to the group's instances.</td></tr>
<tr><td><CopyableCode code="classic_link_vpc_id" /></td><td><code>string</code></td><td>The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.</td></tr>
<tr><td><CopyableCode code="ebs_optimized" /></td><td><code>boolean</code></td><td>Specifies whether the launch configuration is optimized for EBS I/O (true) or not (false).</td></tr>
<tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td>Provides the name of the EC2 key pair.</td></tr>
<tr><td><CopyableCode code="spot_price" /></td><td><code>string</code></td><td>The maximum hourly price you are willing to pay for any Spot Instances launched to fulfill the request.</td></tr>
<tr><td><CopyableCode code="image_id" /></td><td><code>string</code></td><td>Provides the unique ID of the Amazon Machine Image (AMI) that was assigned during registration.</td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td>Specifies the instance type of the EC2 instance.</td></tr>
<tr><td><CopyableCode code="ram_disk_id" /></td><td><code>string</code></td><td>The ID of the RAM disk to select.</td></tr>
<tr><td><CopyableCode code="instance_monitoring" /></td><td><code>boolean</code></td><td>Controls whether instances in this group are launched with detailed (true) or basic (false) monitoring.</td></tr>
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
Lists all <code>launch_configurations</code> in a region.
```sql
SELECT
region,
launch_configuration_name
FROM aws.autoscaling.launch_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>launch_configurations_list_only</code> resource, see <a href="/providers/aws/autoscaling/launch_configurations/#permissions"><code>launch_configurations</code></a>



---
title: launch_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_configuration
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
Gets an individual <code>launch_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>launch_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.autoscaling.launch_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>associate_public_ip_address</code></td><td><code>boolean</code></td><td>For Auto Scaling groups that are running in a virtual private cloud (VPC), specifies whether to assign a public IP address to the group's instances.</td></tr>
<tr><td><code>block_device_mappings</code></td><td><code>array</code></td><td>Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes.</td></tr>
<tr><td><code>classic_link_vpc_id</code></td><td><code>string</code></td><td>The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.</td></tr>
<tr><td><code>classic_link_vpc_security_groups</code></td><td><code>array</code></td><td>The IDs of one or more security groups for the VPC that you specified in the ClassicLinkVPCId property.</td></tr>
<tr><td><code>ebs_optimized</code></td><td><code>boolean</code></td><td>Specifies whether the launch configuration is optimized for EBS I&#x2F;O (true) or not (false).</td></tr>
<tr><td><code>iam_instance_profile</code></td><td><code>string</code></td><td>Provides the name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.</td></tr>
<tr><td><code>image_id</code></td><td><code>string</code></td><td>Provides the unique ID of the Amazon Machine Image (AMI) that was assigned during registration.</td></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td>The ID of the Amazon EC2 instance you want to use to create the launch configuration.</td></tr>
<tr><td><code>instance_monitoring</code></td><td><code>boolean</code></td><td>Controls whether instances in this group are launched with detailed (true) or basic (false) monitoring.</td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td>Specifies the instance type of the EC2 instance.</td></tr>
<tr><td><code>kernel_id</code></td><td><code>string</code></td><td>Provides the ID of the kernel associated with the EC2 AMI.</td></tr>
<tr><td><code>key_name</code></td><td><code>string</code></td><td>Provides the name of the EC2 key pair.</td></tr>
<tr><td><code>launch_configuration_name</code></td><td><code>string</code></td><td>The name of the launch configuration. This name must be unique per Region per account.</td></tr>
<tr><td><code>metadata_options</code></td><td><code>object</code></td><td>The metadata options for the instances.</td></tr>
<tr><td><code>placement_tenancy</code></td><td><code>string</code></td><td>The tenancy of the instance, either default or dedicated.</td></tr>
<tr><td><code>ram_disk_id</code></td><td><code>string</code></td><td>The ID of the RAM disk to select.</td></tr>
<tr><td><code>security_groups</code></td><td><code>array</code></td><td>A list that contains the security groups to assign to the instances in the Auto Scaling group.</td></tr>
<tr><td><code>spot_price</code></td><td><code>string</code></td><td>The maximum hourly price you are willing to pay for any Spot Instances launched to fulfill the request.</td></tr>
<tr><td><code>user_data</code></td><td><code>string</code></td><td>The Base64-encoded user data to make available to the launched EC2 instances.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
associate_public_ip_address,
block_device_mappings,
classic_link_vp_cid,
classic_link_vp_csecurity_groups,
ebs_optimized,
iam_instance_profile,
image_id,
instance_id,
instance_monitoring,
instance_type,
kernel_id,
key_name,
launch_configuration_name,
metadata_options,
placement_tenancy,
ram_disk_id,
security_groups,
spot_price,
user_data
FROM awscc.autoscaling.launch_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '{LaunchConfigurationName}';
```

## Permissions

To operate on the <code>launch_configuration</code> resource, the following permissions are required:

### Read
```json
autoscaling:DescribeLaunchConfigurations
```

### Delete
```json
autoscaling:DeleteLaunchConfiguration,
autoscaling:DescribeLaunchConfigurations
```


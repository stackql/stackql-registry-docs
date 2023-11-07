---
title: launch_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_configurations
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
Retrieves a list of <code>launch_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.autoscaling.launch_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AssociatePublicIpAddress</code></td><td><code>boolean</code></td><td>For Auto Scaling groups that are running in a virtual private cloud (VPC), specifies whether to assign a public IP address to the group's instances.</td></tr>
<tr><td><code>BlockDeviceMappings</code></td><td><code>array</code></td><td>Specifies how block devices are exposed to the instance. You can specify virtual devices and EBS volumes.</td></tr>
<tr><td><code>ClassicLinkVPCId</code></td><td><code>string</code></td><td>The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.</td></tr>
<tr><td><code>ClassicLinkVPCSecurityGroups</code></td><td><code>array</code></td><td>The IDs of one or more security groups for the VPC that you specified in the ClassicLinkVPCId property.</td></tr>
<tr><td><code>EbsOptimized</code></td><td><code>boolean</code></td><td>Specifies whether the launch configuration is optimized for EBS I&#x2F;O (true) or not (false).</td></tr>
<tr><td><code>IamInstanceProfile</code></td><td><code>string</code></td><td>Provides the name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance. The instance profile contains the IAM role.</td></tr>
<tr><td><code>ImageId</code></td><td><code>string</code></td><td>Provides the unique ID of the Amazon Machine Image (AMI) that was assigned during registration.</td></tr>
<tr><td><code>InstanceId</code></td><td><code>string</code></td><td>The ID of the Amazon EC2 instance you want to use to create the launch configuration.</td></tr>
<tr><td><code>InstanceMonitoring</code></td><td><code>boolean</code></td><td>Controls whether instances in this group are launched with detailed (true) or basic (false) monitoring.</td></tr>
<tr><td><code>InstanceType</code></td><td><code>string</code></td><td>Specifies the instance type of the EC2 instance.</td></tr>
<tr><td><code>KernelId</code></td><td><code>string</code></td><td>Provides the ID of the kernel associated with the EC2 AMI.</td></tr>
<tr><td><code>KeyName</code></td><td><code>string</code></td><td>Provides the name of the EC2 key pair.</td></tr>
<tr><td><code>LaunchConfigurationName</code></td><td><code>string</code></td><td>The name of the launch configuration. This name must be unique per Region per account.</td></tr>
<tr><td><code>MetadataOptions</code></td><td><code>undefined</code></td><td>The metadata options for the instances.</td></tr>
<tr><td><code>PlacementTenancy</code></td><td><code>string</code></td><td>The tenancy of the instance, either default or dedicated.</td></tr>
<tr><td><code>RamDiskId</code></td><td><code>string</code></td><td>The ID of the RAM disk to select.</td></tr>
<tr><td><code>SecurityGroups</code></td><td><code>array</code></td><td>A list that contains the security groups to assign to the instances in the Auto Scaling group.</td></tr>
<tr><td><code>SpotPrice</code></td><td><code>string</code></td><td>The maximum hourly price you are willing to pay for any Spot Instances launched to fulfill the request.</td></tr>
<tr><td><code>UserData</code></td><td><code>string</code></td><td>The Base64-encoded user data to make available to the launched EC2 instances.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.autoscaling.launch_configurations
WHERE region = 'us-east-1'
</pre>

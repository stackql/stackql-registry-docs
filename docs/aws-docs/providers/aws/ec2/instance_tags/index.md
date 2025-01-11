---
title: instance_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_tags
  - ec2
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

Expands all tag keys and values for <code>instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.instance_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="tenancy" /></td><td><code>string</code></td><td>The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware.</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td>the names of the security groups. For a nondefault VPC, you must use security group IDs instead.</td></tr>
<tr><td><CopyableCode code="private_dns_name" /></td><td><code>string</code></td><td>The private DNS name of the specified instance. For example: ip-10-24-34-0.ec2.internal.</td></tr>
<tr><td><CopyableCode code="private_ip_address" /></td><td><code>string</code></td><td>&#91;EC2-VPC&#93; The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.</td></tr>
<tr><td><CopyableCode code="user_data" /></td><td><code>string</code></td><td>The user data to make available to the instance.</td></tr>
<tr><td><CopyableCode code="block_device_mappings" /></td><td><code>array</code></td><td>The block device mapping entries that defines the block devices to attach to the instance at launch.</td></tr>
<tr><td><CopyableCode code="iam_instance_profile" /></td><td><code>string</code></td><td>The IAM instance profile.</td></tr>
<tr><td><CopyableCode code="ipv6_addresses" /></td><td><code>array</code></td><td>&#91;EC2-VPC&#93; The IPv6 addresses from the range of the subnet to associate with the primary network interface.</td></tr>
<tr><td><CopyableCode code="kernel_id" /></td><td><code>string</code></td><td>The ID of the kernel.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>&#91;EC2-VPC&#93; The ID of the subnet to launch the instance into.<br /></td></tr>
<tr><td><CopyableCode code="ebs_optimized" /></td><td><code>boolean</code></td><td>Indicates whether the instance is optimized for Amazon EBS I/O.</td></tr>
<tr><td><CopyableCode code="propagate_tags_to_volume_on_creation" /></td><td><code>boolean</code></td><td>Indicates whether to assign the tags from the instance to all of the volumes attached to the instance at launch. If you specify true and you assign tags to the instance, those tags are automatically assigned to all of the volumes that you attach to the instance at launch. If you specify false, those tags are not assigned to the attached volumes.</td></tr>
<tr><td><CopyableCode code="elastic_gpu_specifications" /></td><td><code>array</code></td><td>An elastic GPU to associate with the instance.</td></tr>
<tr><td><CopyableCode code="elastic_inference_accelerators" /></td><td><code>array</code></td><td>An elastic inference accelerator to associate with the instance.</td></tr>
<tr><td><CopyableCode code="volumes" /></td><td><code>array</code></td><td>The volumes to attach to the instance.</td></tr>
<tr><td><CopyableCode code="private_ip" /></td><td><code>string</code></td><td>The private IP address of the specified instance. For example: 10.24.34.0.</td></tr>
<tr><td><CopyableCode code="ipv6_address_count" /></td><td><code>integer</code></td><td>&#91;EC2-VPC&#93; The number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.</td></tr>
<tr><td><CopyableCode code="launch_template" /></td><td><code>object</code></td><td>The launch template to use to launch the instances.</td></tr>
<tr><td><CopyableCode code="enclave_options" /></td><td><code>object</code></td><td>Indicates whether the instance is enabled for AWS Nitro Enclaves.</td></tr>
<tr><td><CopyableCode code="network_interfaces" /></td><td><code>array</code></td><td>The network interfaces to associate with the instance.</td></tr>
<tr><td><CopyableCode code="image_id" /></td><td><code>string</code></td><td>The ID of the AMI. An AMI ID is required to launch an instance and must be specified here or in a launch template.</td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td>The instance type.</td></tr>
<tr><td><CopyableCode code="monitoring" /></td><td><code>boolean</code></td><td>Specifies whether detailed monitoring is enabled for the instance.</td></tr>
<tr><td><CopyableCode code="additional_info" /></td><td><code>string</code></td><td>This property is reserved for internal use. If you use it, the stack fails with this error: Bad property set: &#91;Testing this property&#93; (Service: AmazonEC2; Status Code: 400; Error Code: InvalidParameterCombination; Request ID: 0XXXXXX-49c7-4b40-8bcc-76885dcXXXXX).</td></tr>
<tr><td><CopyableCode code="hibernation_options" /></td><td><code>object</code></td><td>Indicates whether an instance is enabled for hibernation.</td></tr>
<tr><td><CopyableCode code="license_specifications" /></td><td><code>array</code></td><td>The license configurations.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The EC2 Instance ID.</td></tr>
<tr><td><CopyableCode code="public_ip" /></td><td><code>string</code></td><td>The public IP address of the specified instance. For example: 192.0.2.0.</td></tr>
<tr><td><CopyableCode code="instance_initiated_shutdown_behavior" /></td><td><code>string</code></td><td>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</td></tr>
<tr><td><CopyableCode code="cpu_options" /></td><td><code>object</code></td><td>The CPU options for the instance.</td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone of the instance.</td></tr>
<tr><td><CopyableCode code="private_dns_name_options" /></td><td><code>object</code></td><td>The options for the instance hostname.</td></tr>
<tr><td><CopyableCode code="host_id" /></td><td><code>string</code></td><td>If you specify host for the Affinity property, the ID of a dedicated host that the instance is associated with. If you don't specify an ID, Amazon EC2 launches the instance onto any available, compatible dedicated host in your account.</td></tr>
<tr><td><CopyableCode code="host_resource_group_arn" /></td><td><code>string</code></td><td>The ARN of the host resource group in which to launch the instances. If you specify a host resource group ARN, omit the Tenancy parameter or set it to host.</td></tr>
<tr><td><CopyableCode code="public_dns_name" /></td><td><code>string</code></td><td>The public DNS name of the specified instance. For example: ec2-107-20-50-45.compute-1.amazonaws.com.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>The IDs of the security groups.</td></tr>
<tr><td><CopyableCode code="disable_api_termination" /></td><td><code>boolean</code></td><td>If you set this parameter to true, you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can.</td></tr>
<tr><td><CopyableCode code="key_name" /></td><td><code>string</code></td><td>The name of the key pair.</td></tr>
<tr><td><CopyableCode code="ramdisk_id" /></td><td><code>string</code></td><td>The ID of the RAM disk to select.</td></tr>
<tr><td><CopyableCode code="source_dest_check" /></td><td><code>boolean</code></td><td>Specifies whether to enable an instance launched in a VPC to perform NAT.</td></tr>
<tr><td><CopyableCode code="placement_group_name" /></td><td><code>string</code></td><td>The name of an existing placement group that you want to launch the instance into (cluster | partition | spread).</td></tr>
<tr><td><CopyableCode code="ssm_associations" /></td><td><code>array</code></td><td>The SSM document and parameter values in AWS Systems Manager to associate with this instance.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC that the instance is running in.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>object</code></td><td>The current state of the instance.</td></tr>
<tr><td><CopyableCode code="affinity" /></td><td><code>string</code></td><td>Indicates whether the instance is associated with a dedicated host. If you want the instance to always restart on the same host on which it was launched, specify host. If you want the instance to restart on any available host, but try to launch onto the last host it ran on (on a best-effort basis), specify default.</td></tr>
<tr><td><CopyableCode code="credit_specification" /></td><td><code>object</code></td><td>The credit option for CPU usage of the burstable performance instance. Valid values are standard and unlimited.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>instances</code> in a region.
```sql
SELECT
region,
tenancy,
security_groups,
private_dns_name,
private_ip_address,
user_data,
block_device_mappings,
iam_instance_profile,
ipv6_addresses,
kernel_id,
subnet_id,
ebs_optimized,
propagate_tags_to_volume_on_creation,
elastic_gpu_specifications,
elastic_inference_accelerators,
volumes,
private_ip,
ipv6_address_count,
launch_template,
enclave_options,
network_interfaces,
image_id,
instance_type,
monitoring,
additional_info,
hibernation_options,
license_specifications,
instance_id,
public_ip,
instance_initiated_shutdown_behavior,
cpu_options,
availability_zone,
private_dns_name_options,
host_id,
host_resource_group_arn,
public_dns_name,
security_group_ids,
disable_api_termination,
key_name,
ramdisk_id,
source_dest_check,
placement_group_name,
ssm_associations,
vpc_id,
state,
affinity,
credit_specification,
tag_key,
tag_value
FROM aws.ec2.instance_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>instance_tags</code> resource, see <a href="/providers/aws/ec2/instances/#permissions"><code>instances</code></a>


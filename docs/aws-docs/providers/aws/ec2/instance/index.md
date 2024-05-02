---
title: instance
hide_title: false
hide_table_of_contents: false
keywords:
  - instance
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
Gets or operates on an individual <code>instance</code> resource, use <code>instances</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::Instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>tenancy</code></td><td><code>string</code></td><td>The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware.</td></tr>
<tr><td><code>security_groups</code></td><td><code>array</code></td><td>the names of the security groups. For a nondefault VPC, you must use security group IDs instead.</td></tr>
<tr><td><code>private_dns_name</code></td><td><code>string</code></td><td>The private DNS name of the specified instance. For example: ip-10-24-34-0.ec2.internal.</td></tr>
<tr><td><code>private_ip_address</code></td><td><code>string</code></td><td>&#91;EC2-VPC&#93; The primary IPv4 address. You must specify a value from the IPv4 address range of the subnet.</td></tr>
<tr><td><code>user_data</code></td><td><code>string</code></td><td>The user data to make available to the instance.</td></tr>
<tr><td><code>block_device_mappings</code></td><td><code>array</code></td><td>The block device mapping entries that defines the block devices to attach to the instance at launch.</td></tr>
<tr><td><code>iam_instance_profile</code></td><td><code>string</code></td><td>The IAM instance profile.</td></tr>
<tr><td><code>ipv6_addresses</code></td><td><code>array</code></td><td>&#91;EC2-VPC&#93; The IPv6 addresses from the range of the subnet to associate with the primary network interface.</td></tr>
<tr><td><code>kernel_id</code></td><td><code>string</code></td><td>The ID of the kernel.</td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>&#91;EC2-VPC&#93; The ID of the subnet to launch the instance into.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;</td></tr>
<tr><td><code>ebs_optimized</code></td><td><code>boolean</code></td><td>Indicates whether the instance is optimized for Amazon EBS I&#x2F;O.</td></tr>
<tr><td><code>propagate_tags_to_volume_on_creation</code></td><td><code>boolean</code></td><td>Indicates whether to assign the tags from the instance to all of the volumes attached to the instance at launch. If you specify true and you assign tags to the instance, those tags are automatically assigned to all of the volumes that you attach to the instance at launch. If you specify false, those tags are not assigned to the attached volumes.</td></tr>
<tr><td><code>elastic_gpu_specifications</code></td><td><code>array</code></td><td>An elastic GPU to associate with the instance.</td></tr>
<tr><td><code>elastic_inference_accelerators</code></td><td><code>array</code></td><td>An elastic inference accelerator to associate with the instance.</td></tr>
<tr><td><code>volumes</code></td><td><code>array</code></td><td>The volumes to attach to the instance.</td></tr>
<tr><td><code>private_ip</code></td><td><code>string</code></td><td>The private IP address of the specified instance. For example: 10.24.34.0.</td></tr>
<tr><td><code>ipv6_address_count</code></td><td><code>integer</code></td><td>&#91;EC2-VPC&#93; The number of IPv6 addresses to associate with the primary network interface. Amazon EC2 chooses the IPv6 addresses from the range of your subnet.</td></tr>
<tr><td><code>launch_template</code></td><td><code>object</code></td><td>The launch template to use to launch the instances.</td></tr>
<tr><td><code>enclave_options</code></td><td><code>object</code></td><td>Indicates whether the instance is enabled for AWS Nitro Enclaves.</td></tr>
<tr><td><code>network_interfaces</code></td><td><code>array</code></td><td>The network interfaces to associate with the instance.</td></tr>
<tr><td><code>image_id</code></td><td><code>string</code></td><td>The ID of the AMI. An AMI ID is required to launch an instance and must be specified here or in a launch template.</td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td>The instance type.</td></tr>
<tr><td><code>monitoring</code></td><td><code>boolean</code></td><td>Specifies whether detailed monitoring is enabled for the instance.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to add to the instance.</td></tr>
<tr><td><code>additional_info</code></td><td><code>string</code></td><td>This property is reserved for internal use. If you use it, the stack fails with this error: Bad property set: &#91;Testing this property&#93; (Service: AmazonEC2; Status Code: 400; Error Code: InvalidParameterCombination; Request ID: 0XXXXXX-49c7-4b40-8bcc-76885dcXXXXX).</td></tr>
<tr><td><code>hibernation_options</code></td><td><code>object</code></td><td>Indicates whether an instance is enabled for hibernation.</td></tr>
<tr><td><code>license_specifications</code></td><td><code>array</code></td><td>The license configurations.</td></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td>The EC2 Instance ID.</td></tr>
<tr><td><code>public_ip</code></td><td><code>string</code></td><td>The public IP address of the specified instance. For example: 192.0.2.0.</td></tr>
<tr><td><code>instance_initiated_shutdown_behavior</code></td><td><code>string</code></td><td>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</td></tr>
<tr><td><code>cpu_options</code></td><td><code>object</code></td><td>The CPU options for the instance.</td></tr>
<tr><td><code>availability_zone</code></td><td><code>string</code></td><td>The Availability Zone of the instance.</td></tr>
<tr><td><code>private_dns_name_options</code></td><td><code>object</code></td><td>The options for the instance hostname.</td></tr>
<tr><td><code>host_id</code></td><td><code>string</code></td><td>If you specify host for the Affinity property, the ID of a dedicated host that the instance is associated with. If you don't specify an ID, Amazon EC2 launches the instance onto any available, compatible dedicated host in your account.</td></tr>
<tr><td><code>host_resource_group_arn</code></td><td><code>string</code></td><td>The ARN of the host resource group in which to launch the instances. If you specify a host resource group ARN, omit the Tenancy parameter or set it to host.</td></tr>
<tr><td><code>public_dns_name</code></td><td><code>string</code></td><td>The public DNS name of the specified instance. For example: ec2-107-20-50-45.compute-1.amazonaws.com.</td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td>The IDs of the security groups.</td></tr>
<tr><td><code>disable_api_termination</code></td><td><code>boolean</code></td><td>If you set this parameter to true, you can't terminate the instance using the Amazon EC2 console, CLI, or API; otherwise, you can.</td></tr>
<tr><td><code>key_name</code></td><td><code>string</code></td><td>The name of the key pair.</td></tr>
<tr><td><code>ramdisk_id</code></td><td><code>string</code></td><td>The ID of the RAM disk to select.</td></tr>
<tr><td><code>source_dest_check</code></td><td><code>boolean</code></td><td>Specifies whether to enable an instance launched in a VPC to perform NAT.</td></tr>
<tr><td><code>placement_group_name</code></td><td><code>string</code></td><td>The name of an existing placement group that you want to launch the instance into (cluster | partition | spread).</td></tr>
<tr><td><code>ssm_associations</code></td><td><code>array</code></td><td>The SSM document and parameter values in AWS Systems Manager to associate with this instance.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC that the instance is running in.</td></tr>
<tr><td><code>affinity</code></td><td><code>string</code></td><td>Indicates whether the instance is associated with a dedicated host. If you want the instance to always restart on the same host on which it was launched, specify host. If you want the instance to restart on any available host, but try to launch onto the last host it ran on (on a best-effort basis), specify default.</td></tr>
<tr><td><code>credit_specification</code></td><td><code>object</code></td><td>The credit option for CPU usage of the burstable performance instance. Valid values are standard and unlimited.</td></tr>
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
tags,
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
affinity,
credit_specification
FROM aws.ec2.instance
WHERE data__Identifier = '<InstanceId>';
```

## Permissions

To operate on the <code>instance</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeElasticGpus,
ec2:DescribeNetworkInterfaces,
ec2:DescribeVolumes,
ec2:DescribeInstances,
ec2:DescribeInstanceAttribute,
ec2:DescribeInstanceCreditSpecifications,
ec2:DescribeLaunchTemplates,
elastic-inference:DescribeAccelerators,
ssm:DescribeAssociation,
ssm:ListAssociations
```

### Update
```json
ec2:DescribeElasticGpus,
ec2:ModifyPrivateDnsNameOptions,
ec2:DescribeNetworkInterfaces,
ec2:AssociateIamInstanceProfile,
ec2:DescribeIamInstanceProfileAssociations,
ec2:DescribeInstances,
ec2:DescribeSubnets,
ec2:DescribeKeyPairs,
ec2:DescribeSecurityGroups,
ec2:DescribeVpcs,
ec2:DescribeInstanceAttribute,
ec2:DescribeInstanceCreditSpecifications,
ec2:DescribeLaunchTemplates,
ec2:DetachVolume,
ec2:DisassociateIamInstanceProfile,
ec2:ModifyInstanceAttribute,
ec2:ModifyInstanceCreditSpecification,
ec2:ModifyInstanceMaintenanceOptions,
ec2:ModifyInstancePlacement,
ec2:MonitorInstances,
ec2:AttachVolume,
ec2:CreateTags,
ec2:DeleteTags,
ec2:ReplaceIamInstanceProfileAssociation,
ec2:StartInstances,
ec2:StopInstances,
ec2:UnmonitorInstances,
elastic-inference:DescribeAccelerators,
ssm:CreateAssociation,
ssm:DeleteAssociation,
ssm:DescribeAssociation,
ssm:ListAssociations
```

### Delete
```json
ec2:DescribeInstances,
ec2:TerminateInstances,
ec2:DescribeElasticGpus,
ec2:DescribeNetworkInterfaces,
ec2:DescribeVolumes,
ec2:DescribeInstances,
ec2:DescribeInstanceAttribute,
ec2:DescribeInstanceCreditSpecifications,
ec2:DescribeLaunchTemplates,
elastic-inference:DescribeAccelerators,
ssm:DescribeAssociation,
ssm:ListAssociations
```


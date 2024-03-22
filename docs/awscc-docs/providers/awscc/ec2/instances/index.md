---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
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
List of ec2 instances by region (requires `aws` provider to be installed)

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>List of ec2 instances by region (requires `aws` provider to be installed)</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.instances</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td>The ID of the instance.</td></tr>
<tr><td><code>instance_state</code></td><td><code>object</code></td><td>Describes the current state of an instance.</td></tr>
<tr><td><code>instance_type</code></td><td><code>string</code></td><td>The instance type.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ami_launch_index</code></td><td><code>integer</code></td><td>The AMI launch index, which can be used to find this instance in the launch group.</td></tr>
<tr><td><code>architecture</code></td><td><code>string</code></td><td>The architecture of the image.</td></tr>
<tr><td><code>block_device_mapping</code></td><td><code>array</code></td><td>Any block device mapping entries for the instance.</td></tr>
<tr><td><code>boot_mode</code></td><td><code>string</code></td><td>The boot mode of the instance.</td></tr>
<tr><td><code>capacity_reservation_id</code></td><td><code>string</code></td><td>The ID of the Capacity Reservation.</td></tr>
<tr><td><code>capacity_reservation_specification</code></td><td><code>object</code></td><td>Describes the instances Capacity Reservation targeting preferences</td></tr>
<tr><td><code>client_token</code></td><td><code>string</code></td><td>The idempotency token you provided when you launched the instance, if applicable.</td></tr>
<tr><td><code>cpu_options</code></td><td><code>object</code></td><td>The CPU options for the instance.</td></tr>
<tr><td><code>dns_name</code></td><td><code>string</code></td><td>(IPv4 only) The public DNS name assigned to the instance.</td></tr>
<tr><td><code>ebs_optimized</code></td><td><code>boolean</code></td><td>Indicates whether the instance is optimized for Amazon EBS I&#x2F;O.</td></tr>
<tr><td><code>elastic_gpu_association_set</code></td><td><code>array</code></td><td>The Elastic GPU associated with the instance.</td></tr>
<tr><td><code>elastic_inference_accelerator_association_set</code></td><td><code>array</code></td><td>The elastic inference accelerator associated with the instance.</td></tr>
<tr><td><code>ena_support</code></td><td><code>boolean</code></td><td>Specifies whether enhanced networking with ENA is enabled.</td></tr>
<tr><td><code>enclave_options</code></td><td><code>object</code></td><td>Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves.</td></tr>
<tr><td><code>group_set</code></td><td><code>array</code></td><td>The security groups for the instance.</td></tr>
<tr><td><code>hibernation_options</code></td><td><code>object</code></td><td>Indicates whether your instance is configured for hibernation.</td></tr>
<tr><td><code>hypervisor</code></td><td><code>string</code></td><td>The hypervisor type of the instance.</td></tr>
<tr><td><code>iam_instance_profile</code></td><td><code>object</code></td><td>Describes an IAM instance profile.</td></tr>
<tr><td><code>image_id</code></td><td><code>string</code></td><td>The ID of the AMI used to launch the instance.</td></tr>
<tr><td><code>instance_lifecycle</code></td><td><code>string</code></td><td>Indicates whether this is a Spot Instance or a Scheduled Instance.</td></tr>
<tr><td><code>ip_address</code></td><td><code>string</code></td><td>The public IPv4 address, or the Carrier IP address assigned to the instance, if applicable.</td></tr>
<tr><td><code>ipv6_address</code></td><td><code>string</code></td><td>The IPv6 address assigned to the instance.</td></tr>
<tr><td><code>kernel_id</code></td><td><code>string</code></td><td>The kernel associated with this instance, if applicable.</td></tr>
<tr><td><code>key_name</code></td><td><code>string</code></td><td>The name of the key pair, if this instance was launched with an associated key pair.</td></tr>
<tr><td><code>launch_time</code></td><td><code>string</code></td><td>The time the instance was launched.</td></tr>
<tr><td><code>license_set</code></td><td><code>array</code></td><td>The license configurations for the instance.</td></tr>
<tr><td><code>maintenance_options</code></td><td><code>object</code></td><td>The maintenance options for the instance.</td></tr>
<tr><td><code>metadata_options</code></td><td><code>object</code></td><td>The metadata options for the instance.</td></tr>
<tr><td><code>monitoring</code></td><td><code>object</code></td><td>Describes the monitoring of an instance.</td></tr>
<tr><td><code>network_interface_set</code></td><td><code>array</code></td><td>&#91;EC2-VPC&#93; The network interfaces for the instance.</td></tr>
<tr><td><code>outpost_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>placement</code></td><td><code>object</code></td><td>Describes the placement of an instance.</td></tr>
<tr><td><code>platform</code></td><td><code>string</code></td><td>The value is Windows instances; otherwise blank.</td></tr>
<tr><td><code>platform_details</code></td><td><code>string</code></td><td>The platform details value for the instance.</td></tr>
<tr><td><code>private_dns_name</code></td><td><code>string</code></td><td>(IPv4 only) The private DNS hostname name assigned to the instance.</td></tr>
<tr><td><code>private_dns_name_options</code></td><td><code>object</code></td><td>Describes the options for instance hostnames.</td></tr>
<tr><td><code>private_ip_address</code></td><td><code>string</code></td><td>The private IPv4 address assigned to the instance.</td></tr>
<tr><td><code>product_codes</code></td><td><code>array</code></td><td>The product codes attached to this instance, if applicable.</td></tr>
<tr><td><code>ramdisk_id</code></td><td><code>string</code></td><td>The RAM disk associated with this instance, if applicable.</td></tr>
<tr><td><code>reason</code></td><td><code>string</code></td><td>The reason for the most recent state transition. This might be an empty string.</td></tr>
<tr><td><code>root_device_name</code></td><td><code>string</code></td><td>The device name of the root device volume.</td></tr>
<tr><td><code>root_device_type</code></td><td><code>string</code></td><td>The root device type used by the AMI. The AMI can use an EBS volume or an instance store volume.</td></tr>
<tr><td><code>source_dest_check</code></td><td><code>boolean</code></td><td>Indicates whether source&#x2F;destination checking is enabled.</td></tr>
<tr><td><code>spot_instance_request_id</code></td><td><code>string</code></td><td>If the request is a Spot Instance request, the ID of the request.</td></tr>
<tr><td><code>sriov_net_support</code></td><td><code>string</code></td><td>Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled.</td></tr>
<tr><td><code>state_reason</code></td><td><code>object</code></td><td>Describes a state change.</td></tr>
<tr><td><code>tag_set</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tpm_support</code></td><td><code>string</code></td><td>If the instance is configured for NitroTPM support</td></tr>
<tr><td><code>usage_operation</code></td><td><code>string</code></td><td>The usage operation value for the instance.</td></tr>
<tr><td><code>usage_operation_update_time</code></td><td><code>string</code></td><td>The time that the usage operation was last updated.</td></tr>
<tr><td><code>virtualization_type</code></td><td><code>string</code></td><td>The virtualization type of the instance.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_id,
instance_state,
instance_type,
vpc_id,
subnet_id,
ami_launch_index,
architecture,
block_device_mapping,
boot_mode,
capacity_reservation_id,
capacity_reservation_specification,
client_token,
cpu_options,
dns_name,
ebs_optimized,
elastic_gpu_association_set,
elastic_inference_accelerator_association_set,
ena_support,
enclave_options,
group_set,
hibernation_options,
hypervisor,
iam_instance_profile,
image_id,
instance_lifecycle,
ip_address,
ipv6_address,
kernel_id,
key_name,
launch_time,
license_set,
maintenance_options,
metadata_options,
monitoring,
network_interface_set,
outpost_arn,
placement,
platform,
platform_details,
private_dns_name,
private_dns_name_options,
private_ip_address,
product_codes,
ramdisk_id,
reason,
root_device_name,
root_device_type,
source_dest_check,
spot_instance_request_id,
sriov_net_support,
state_reason,
tag_set,
tpm_support,
usage_operation,
usage_operation_update_time,
virtualization_type,
region
FROM awscc.ec2.instances
WHERE region = '<region>';
```





---
title: eip
hide_title: false
hide_table_of_contents: false
keywords:
  - eip
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


Gets or updates an individual <code>eip</code> resource, use <code>eips</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eip</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Elastic IP (EIP) address and can, optionally, associate it with an Amazon EC2 instance.&lt;br&#x2F;&gt; You can allocate an Elastic IP address from an address pool owned by AWS or from an address pool created from a public IPv4 address range that you have brought to AWS for use with your AWS resources using bring your own IP addresses (BYOIP). For more information, see &#91;Bring Your Own IP Addresses (BYOIP)&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;ec2-byoip.html) in the *Amazon EC2 User Guide*.&lt;br&#x2F;&gt; For more information, see &#91;Elastic IP Addresses&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;elastic-ip-addresses-eip.html) in the *Amazon EC2 User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.eip" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="public_ip" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="allocation_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The network (<code>vpc</code>).&lt;br&#x2F;&gt; If you define an Elastic IP address and associate it with a VPC that is defined in the same template, you must declare a dependency on the VPC-gateway attachment by using the &#91;DependsOn Attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-dependson.html) on this resource.</td></tr>
<tr><td><CopyableCode code="network_border_group" /></td><td><code>string</code></td><td>A unique set of Availability Zones, Local Zones, or Wavelength Zones from which AWS advertises IP addresses. Use this parameter to limit the IP address to this location. IP addresses cannot move between network border groups.&lt;br&#x2F;&gt; Use &#91;DescribeAvailabilityZones&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;APIReference&#x2F;API_DescribeAvailabilityZones.html) to view the network border groups.</td></tr>
<tr><td><CopyableCode code="transfer_address" /></td><td><code>string</code></td><td>The Elastic IP address you are accepting for transfer. You can only accept one transferred address. For more information on Elastic IP address transfers, see &#91;Transfer Elastic IP addresses&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;vpc-eips.html#transfer-EIPs-intro) in the *Amazon Virtual Private Cloud User Guide*.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance.&lt;br&#x2F;&gt;  Updates to the <code>InstanceId</code> property may require *some interruptions*. Updates on an EIP reassociates the address on its associated resource.</td></tr>
<tr><td><CopyableCode code="public_ipv4_pool" /></td><td><code>string</code></td><td>The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool.&lt;br&#x2F;&gt;  Updates to the <code>PublicIpv4Pool</code> property may require *some interruptions*. Updates on an EIP reassociates the address on its associated resource.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the Elastic IP address.&lt;br&#x2F;&gt;  Updates to the <code>Tags</code> property may require *some interruptions*. Updates on an EIP reassociates the address on its associated resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
public_ip,
allocation_id,
domain,
network_border_group,
transfer_address,
instance_id,
public_ipv4_pool,
tags
FROM aws.ec2.eip
WHERE region = 'us-east-1' AND data__Identifier = '<PublicIp>|<AllocationId>';
```


## Permissions

To operate on the <code>eip</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeAddresses
```

### Update
```json
ec2:DescribeAddresses,
ec2:DisassociateAddress,
ec2:DeleteTags,
ec2:CreateTags,
ec2:AssociateAddress
```


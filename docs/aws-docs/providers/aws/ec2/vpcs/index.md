---
title: vpcs
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcs
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


Used to retrieve a list of <code>vpcs</code> in a region or to create or delete a <code>vpcs</code> resource, use <code>vpc</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpcs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a virtual private cloud (VPC).&lt;br&#x2F;&gt; You can optionally request an IPv6 CIDR block for the VPC. You can request an Amazon-provided IPv6 CIDR block from Amazon's pool of IPv6 addresses, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses (BYOIP).&lt;br&#x2F;&gt; For more information, see &#91;Virtual private clouds (VPC)&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;configure-your-vpc.html) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpcs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
vpc_id
FROM aws.ec2.vpcs
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "InstanceTenancy": "{{ InstanceTenancy }}",
 "Ipv4NetmaskLength": "{{ Ipv4NetmaskLength }}",
 "CidrBlock": "{{ CidrBlock }}",
 "Ipv4IpamPoolId": "{{ Ipv4IpamPoolId }}",
 "EnableDnsSupport": "{{ EnableDnsSupport }}",
 "EnableDnsHostnames": "{{ EnableDnsHostnames }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.ec2.vpcs (
 InstanceTenancy,
 Ipv4NetmaskLength,
 CidrBlock,
 Ipv4IpamPoolId,
 EnableDnsSupport,
 EnableDnsHostnames,
 Tags,
 region
)
SELECT 
{{ InstanceTenancy }},
 {{ Ipv4NetmaskLength }},
 {{ CidrBlock }},
 {{ Ipv4IpamPoolId }},
 {{ EnableDnsSupport }},
 {{ EnableDnsHostnames }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "InstanceTenancy": "{{ InstanceTenancy }}",
 "Ipv4NetmaskLength": "{{ Ipv4NetmaskLength }}",
 "CidrBlock": "{{ CidrBlock }}",
 "Ipv4IpamPoolId": "{{ Ipv4IpamPoolId }}",
 "EnableDnsSupport": "{{ EnableDnsSupport }}",
 "EnableDnsHostnames": "{{ EnableDnsHostnames }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.vpcs (
 InstanceTenancy,
 Ipv4NetmaskLength,
 CidrBlock,
 Ipv4IpamPoolId,
 EnableDnsSupport,
 EnableDnsHostnames,
 Tags,
 region
)
SELECT 
 {{ InstanceTenancy }},
 {{ Ipv4NetmaskLength }},
 {{ CidrBlock }},
 {{ Ipv4IpamPoolId }},
 {{ EnableDnsSupport }},
 {{ EnableDnsHostnames }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.vpcs
WHERE data__Identifier = '<VpcId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpcs</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVpc,
ec2:DescribeVpcs,
ec2:ModifyVpcAttribute,
ec2:CreateTags
```

### List
```json
ec2:DescribeVpcs
```

### Delete
```json
ec2:DeleteVpc,
ec2:DescribeVpcs
```


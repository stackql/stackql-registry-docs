---
title: vpc_cidr_blocks
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_cidr_blocks
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


Used to retrieve a list of <code>vpc_cidr_blocks</code> in a region or to create or delete a <code>vpc_cidr_blocks</code> resource, use <code>vpc_cidr_block</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_cidr_blocks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCCidrBlock</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_cidr_blocks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Id of the VPC associated CIDR Block.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
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
    <td><CopyableCode code="VpcId, region" /></td>
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
id,
vpc_id
FROM aws.ec2.vpc_cidr_blocks
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>vpc_cidr_block</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ec2.vpc_cidr_blocks (
 VpcId,
 region
)
SELECT 
'{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpc_cidr_blocks (
 CidrBlock,
 Ipv6Pool,
 VpcId,
 Ipv6CidrBlock,
 Ipv4IpamPoolId,
 Ipv4NetmaskLength,
 Ipv6IpamPoolId,
 Ipv6NetmaskLength,
 AmazonProvidedIpv6CidrBlock,
 region
)
SELECT 
 '{{ CidrBlock }}',
 '{{ Ipv6Pool }}',
 '{{ VpcId }}',
 '{{ Ipv6CidrBlock }}',
 '{{ Ipv4IpamPoolId }}',
 '{{ Ipv4NetmaskLength }}',
 '{{ Ipv6IpamPoolId }}',
 '{{ Ipv6NetmaskLength }}',
 '{{ AmazonProvidedIpv6CidrBlock }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: vpc_cidr_block
    props:
      - name: CidrBlock
        value: '{{ CidrBlock }}'
      - name: Ipv6Pool
        value: '{{ Ipv6Pool }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: Ipv6CidrBlock
        value: '{{ Ipv6CidrBlock }}'
      - name: Ipv4IpamPoolId
        value: '{{ Ipv4IpamPoolId }}'
      - name: Ipv4NetmaskLength
        value: '{{ Ipv4NetmaskLength }}'
      - name: Ipv6IpamPoolId
        value: '{{ Ipv6IpamPoolId }}'
      - name: Ipv6NetmaskLength
        value: '{{ Ipv6NetmaskLength }}'
      - name: AmazonProvidedIpv6CidrBlock
        value: '{{ AmazonProvidedIpv6CidrBlock }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.ec2.vpc_cidr_blocks
WHERE data__Identifier = '<Id|VpcId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_cidr_blocks</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateVpcCidrBlock,
ec2:DescribeVpcs,
ec2:AllocateIpamPoolCidr
```

### Delete
```json
ec2:DescribeVpcs,
ec2:DisassociateVpcCidrBlock
```

### List
```json
ec2:DescribeVpcs
```


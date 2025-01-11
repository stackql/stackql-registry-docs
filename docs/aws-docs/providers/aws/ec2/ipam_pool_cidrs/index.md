---
title: ipam_pool_cidrs
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_pool_cidrs
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

Creates, updates, deletes or gets an <code>ipam_pool_cidr</code> resource or lists <code>ipam_pool_cidrs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_pool_cidrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMPoolCidr Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_pool_cidrs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ipam_pool_cidr_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool Cidr.</td></tr>
<tr><td><CopyableCode code="ipam_pool_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="cidr" /></td><td><code>string</code></td><td>Represents a single IPv4 or IPv6 CIDR</td></tr>
<tr><td><CopyableCode code="netmask_length" /></td><td><code>integer</code></td><td>The desired netmask length of the provision. If set, IPAM will choose a block of free space with this size and return the CIDR representing it.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>Provisioned state of the cidr.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ipampoolcidr.html"><code>AWS::EC2::IPAMPoolCidr</code></a>.

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
    <td><CopyableCode code="IpamPoolId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>ipam_pool_cidrs</code> in a region.
```sql
SELECT
region,
ipam_pool_cidr_id,
ipam_pool_id,
cidr,
netmask_length,
state
FROM aws.ec2.ipam_pool_cidrs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ipam_pool_cidr</code>.
```sql
SELECT
region,
ipam_pool_cidr_id,
ipam_pool_id,
cidr,
netmask_length,
state
FROM aws.ec2.ipam_pool_cidrs
WHERE region = 'us-east-1' AND data__Identifier = '<IpamPoolId>|<IpamPoolCidrId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ipam_pool_cidr</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.ipam_pool_cidrs (
 IpamPoolId,
 region
)
SELECT 
'{{ IpamPoolId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.ipam_pool_cidrs (
 IpamPoolId,
 Cidr,
 NetmaskLength,
 region
)
SELECT 
 '{{ IpamPoolId }}',
 '{{ Cidr }}',
 '{{ NetmaskLength }}',
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
  - name: ipam_pool_cidr
    props:
      - name: IpamPoolId
        value: '{{ IpamPoolId }}'
      - name: Cidr
        value: '{{ Cidr }}'
      - name: NetmaskLength
        value: '{{ NetmaskLength }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.ipam_pool_cidrs
WHERE data__Identifier = '<IpamPoolId|IpamPoolCidrId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ipam_pool_cidrs</code> resource, the following permissions are required:

### Create
```json
ec2:ProvisionIpamPoolCidr,
ec2:GetIpamPoolCidrs
```

### Read
```json
ec2:GetIpamPoolCidrs
```

### Delete
```json
ec2:DeprovisionIpamPoolCidr,
ec2:GetIpamPoolCidrs
```

### List
```json
ec2:GetIpamPoolCidrs
```

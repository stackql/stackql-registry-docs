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


Used to retrieve a list of <code>ipam_pool_cidrs</code> in a region or to create or delete a <code>ipam_pool_cidrs</code> resource, use <code>ipam_pool_cidr</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_pool_cidrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMPoolCidr Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_pool_cidrs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ipam_pool_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="ipam_pool_cidr_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool Cidr.</td></tr>
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
ipam_pool_id,
ipam_pool_cidr_id
FROM aws.ec2.ipam_pool_cidrs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>ipam_pool_cidr</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- ipam_pool_cidr.iql (required properties only)
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
-- ipam_pool_cidr.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
ec2:DeprovisionIpamPoolCidr,
ec2:GetIpamPoolCidrs
```

### List
```json
ec2:GetIpamPoolCidrs
```


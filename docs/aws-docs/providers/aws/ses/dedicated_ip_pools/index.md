---
title: dedicated_ip_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_ip_pools
  - ses
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

Creates, updates, deletes or gets a <code>dedicated_ip_pool</code> resource or lists <code>dedicated_ip_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_ip_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SES::DedicatedIpPool</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.dedicated_ip_pools" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="pool_name" /></td><td><code>string</code></td><td>The name of the dedicated IP pool.</td></tr>
<tr><td><CopyableCode code="scaling_mode" /></td><td><code>string</code></td><td>Specifies whether the dedicated IP pool is managed or not. The default value is STANDARD.</td></tr>
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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
Gets all <code>dedicated_ip_pools</code> in a region.
```sql
SELECT
region,
pool_name,
scaling_mode
FROM aws.ses.dedicated_ip_pools
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>dedicated_ip_pool</code>.
```sql
SELECT
region,
pool_name,
scaling_mode
FROM aws.ses.dedicated_ip_pools
WHERE region = 'us-east-1' AND data__Identifier = '<PoolName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dedicated_ip_pool</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ses.dedicated_ip_pools (
 PoolName,
 ScalingMode,
 region
)
SELECT 
'{{ PoolName }}',
 '{{ ScalingMode }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ses.dedicated_ip_pools (
 PoolName,
 ScalingMode,
 region
)
SELECT 
 '{{ PoolName }}',
 '{{ ScalingMode }}',
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
  - name: dedicated_ip_pool
    props:
      - name: PoolName
        value: '{{ PoolName }}'
      - name: ScalingMode
        value: '{{ ScalingMode }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ses.dedicated_ip_pools
WHERE data__Identifier = '<PoolName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dedicated_ip_pools</code> resource, the following permissions are required:

### Create
```json
ses:CreateDedicatedIpPool,
ses:GetDedicatedIpPool,
ses:GetDedicatedIps
```

### Read
```json
ses:GetDedicatedIpPool,
ses:GetDedicatedIps
```

### Update
```json
ses:PutDedicatedIpPoolScalingAttributes,
ses:GetDedicatedIpPool
```

### Delete
```json
ses:DeleteDedicatedIpPool
```

### List
```json
ses:ListDedicatedIpPools
```


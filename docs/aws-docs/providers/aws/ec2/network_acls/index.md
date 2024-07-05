---
title: network_acls
hide_title: false
hide_table_of_contents: false
keywords:
  - network_acls
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

Creates, updates, deletes or gets a <code>network_acl</code> resource or lists <code>network_acls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a network ACL for your VPC.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_acls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the network ACL.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC for the network ACL.</td></tr>
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
Gets all <code>network_acls</code> in a region.
```sql
SELECT
region,
id,
tags,
vpc_id
FROM aws.ec2.network_acls
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>network_acl</code>.
```sql
SELECT
region,
id,
tags,
vpc_id
FROM aws.ec2.network_acls
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_acl</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.network_acls (
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
INSERT INTO aws.ec2.network_acls (
 Tags,
 VpcId,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ VpcId }}',
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
  - name: network_acl
    props:
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VpcId
        value: '{{ VpcId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.network_acls
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_acls</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkAcl,
ec2:DescribeNetworkAcls,
ec2:CreateTags
```

### Read
```json
ec2:DescribeNetworkAcls,
ec2:DescribeTags
```

### Update
```json
ec2:DescribeNetworkAcls,
ec2:DeleteTags,
ec2:CreateTags
```

### Delete
```json
ec2:DeleteTags,
ec2:DeleteNetworkAcl,
ec2:DescribeNetworkAcls
```

### List
```json
ec2:DescribeNetworkAcls
```


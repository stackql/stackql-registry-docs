---
title: subnet_network_acl_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_network_acl_associations
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


Used to retrieve a list of <code>subnet_network_acl_associations</code> in a region or to create or delete a <code>subnet_network_acl_associations</code> resource, use <code>subnet_network_acl_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_network_acl_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SubnetNetworkAclAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnet_network_acl_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="NetworkAclId, SubnetId, region" /></td>
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
association_id
FROM aws.ec2.subnet_network_acl_associations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>subnet_network_acl_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.subnet_network_acl_associations (
 SubnetId,
 NetworkAclId,
 region
)
SELECT 
'{{ SubnetId }}',
 '{{ NetworkAclId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.subnet_network_acl_associations (
 SubnetId,
 NetworkAclId,
 region
)
SELECT 
 '{{ SubnetId }}',
 '{{ NetworkAclId }}',
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
  - name: subnet_network_acl_association
    props:
      - name: SubnetId
        value: '{{ SubnetId }}'
      - name: NetworkAclId
        value: '{{ NetworkAclId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.ec2.subnet_network_acl_associations
WHERE data__Identifier = '<AssociationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subnet_network_acl_associations</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeNetworkAcls,
ec2:ReplaceNetworkAclAssociation
```

### Delete
```json
ec2:DescribeNetworkAcls,
ec2:ReplaceNetworkAclAssociation
```

### List
```json
ec2:DescribeNetworkAcls
```


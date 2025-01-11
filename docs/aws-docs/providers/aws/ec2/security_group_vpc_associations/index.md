---
title: security_group_vpc_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_vpc_associations
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

Creates, updates, deletes or gets a <code>security_group_vpc_association</code> resource or lists <code>security_group_vpc_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_vpc_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for the AWS::EC2::SecurityGroupVpcAssociation resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_group_vpc_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>The group ID of the specified security group.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC in the security group vpc association.</td></tr>
<tr><td><CopyableCode code="vpc_owner_id" /></td><td><code>string</code></td><td>The owner of the VPC in the security group vpc association.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the security group vpc association.</td></tr>
<tr><td><CopyableCode code="state_reason" /></td><td><code>string</code></td><td>The reason for the state of the security group vpc association.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-securitygroupvpcassociation.html"><code>AWS::EC2::SecurityGroupVpcAssociation</code></a>.

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
    <td><CopyableCode code="GroupId, VpcId, region" /></td>
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
Gets all <code>security_group_vpc_associations</code> in a region.
```sql
SELECT
region,
group_id,
vpc_id,
vpc_owner_id,
state,
state_reason
FROM aws.ec2.security_group_vpc_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>security_group_vpc_association</code>.
```sql
SELECT
region,
group_id,
vpc_id,
vpc_owner_id,
state,
state_reason
FROM aws.ec2.security_group_vpc_associations
WHERE region = 'us-east-1' AND data__Identifier = '<GroupId>|<VpcId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_group_vpc_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.security_group_vpc_associations (
 GroupId,
 VpcId,
 region
)
SELECT 
'{{ GroupId }}',
 '{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.security_group_vpc_associations (
 GroupId,
 VpcId,
 region
)
SELECT 
 '{{ GroupId }}',
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
  - name: security_group_vpc_association
    props:
      - name: GroupId
        value: '{{ GroupId }}'
      - name: VpcId
        value: '{{ VpcId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.security_group_vpc_associations
WHERE data__Identifier = '<GroupId|VpcId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>security_group_vpc_associations</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateSecurityGroupVpc,
ec2:DescribeSecurityGroupVpcAssociations
```

### Read
```json
ec2:DescribeSecurityGroupVpcAssociations
```

### Delete
```json
ec2:DisassociateSecurityGroupVpc,
ec2:DescribeSecurityGroupVpcAssociations
```

### List
```json
ec2:DescribeSecurityGroupVpcAssociations
```

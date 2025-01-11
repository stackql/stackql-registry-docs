---
title: flow_vpc_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_vpc_interfaces
  - mediaconnect
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

Creates, updates, deletes or gets a <code>flow_vpc_interface</code> resource or lists <code>flow_vpc_interfaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_vpc_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowVpcInterface</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_vpc_interfaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Immutable and has to be a unique against other VpcInterfaces in this Flow.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role Arn MediaConnect can assume to create ENIs in customer's account.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>Security Group IDs to be used on ENI.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>Subnet must be in the AZ of the Flow</td></tr>
<tr><td><CopyableCode code="network_interface_ids" /></td><td><code>array</code></td><td>IDs of the network interfaces created in customer's account by MediaConnect.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html"><code>AWS::MediaConnect::FlowVpcInterface</code></a>.

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
    <td><CopyableCode code="FlowArn, Name, RoleArn, SubnetId, SecurityGroupIds, region" /></td>
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
Gets all <code>flow_vpc_interfaces</code> in a region.
```sql
SELECT
region,
flow_arn,
name,
role_arn,
security_group_ids,
subnet_id,
network_interface_ids
FROM aws.mediaconnect.flow_vpc_interfaces
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>flow_vpc_interface</code>.
```sql
SELECT
region,
flow_arn,
name,
role_arn,
security_group_ids,
subnet_id,
network_interface_ids
FROM aws.mediaconnect.flow_vpc_interfaces
WHERE region = 'us-east-1' AND data__Identifier = '<FlowArn>|<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow_vpc_interface</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediaconnect.flow_vpc_interfaces (
 FlowArn,
 Name,
 RoleArn,
 SecurityGroupIds,
 SubnetId,
 region
)
SELECT 
'{{ FlowArn }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ SecurityGroupIds }}',
 '{{ SubnetId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediaconnect.flow_vpc_interfaces (
 FlowArn,
 Name,
 RoleArn,
 SecurityGroupIds,
 SubnetId,
 region
)
SELECT 
 '{{ FlowArn }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ SecurityGroupIds }}',
 '{{ SubnetId }}',
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
  - name: flow_vpc_interface
    props:
      - name: FlowArn
        value: '{{ FlowArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: SubnetId
        value: '{{ SubnetId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediaconnect.flow_vpc_interfaces
WHERE data__Identifier = '<FlowArn|Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flow_vpc_interfaces</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
mediaconnect:DescribeFlow,
mediaconnect:AddFlowVpcInterfaces
```

### Read
```json
mediaconnect:DescribeFlow
```

### Update
```json
mediaconnect:DescribeFlow,
mediaconnect:AddFlowVpcInterfaces,
mediaconnect:RemoveFlowVpcInterface
```

### Delete
```json
mediaconnect:DescribeFlow,
mediaconnect:RemoveFlowVpcInterface
```

### List
```json
mediaconnect:DescribeFlow
```

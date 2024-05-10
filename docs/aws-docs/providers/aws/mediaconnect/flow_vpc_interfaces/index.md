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


Used to retrieve a list of <code>flow_vpc_interfaces</code> in a region or to create or delete a <code>flow_vpc_interfaces</code> resource, use <code>flow_vpc_interface</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_vpc_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowVpcInterface</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_vpc_interfaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Immutable and has to be a unique against other VpcInterfaces in this Flow.</td></tr>
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
flow_arn,
name
FROM aws.mediaconnect.flow_vpc_interfaces
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
 "FlowArn": "{{ FlowArn }}",
 "Name": "{{ Name }}",
 "RoleArn": "{{ RoleArn }}",
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "SubnetId": "{{ SubnetId }}"
}
>>>
--required properties only
INSERT INTO aws.mediaconnect.flow_vpc_interfaces (
 FlowArn,
 Name,
 RoleArn,
 SecurityGroupIds,
 SubnetId,
 region
)
SELECT 
{{ .FlowArn }},
 {{ .Name }},
 {{ .RoleArn }},
 {{ .SecurityGroupIds }},
 {{ .SubnetId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "FlowArn": "{{ FlowArn }}",
 "Name": "{{ Name }}",
 "RoleArn": "{{ RoleArn }}",
 "SecurityGroupIds": [
  "{{ SecurityGroupIds[0] }}"
 ],
 "SubnetId": "{{ SubnetId }}"
}
>>>
--all properties
INSERT INTO aws.mediaconnect.flow_vpc_interfaces (
 FlowArn,
 Name,
 RoleArn,
 SecurityGroupIds,
 SubnetId,
 region
)
SELECT 
 {{ .FlowArn }},
 {{ .Name }},
 {{ .RoleArn }},
 {{ .SecurityGroupIds }},
 {{ .SubnetId }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
mediaconnect:DescribeFlow,
mediaconnect:RemoveFlowVpcInterface
```

### List
```json
mediaconnect:DescribeFlow
```


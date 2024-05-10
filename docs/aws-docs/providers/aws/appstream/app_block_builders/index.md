---
title: app_block_builders
hide_title: false
hide_table_of_contents: false
keywords:
  - app_block_builders
  - appstream
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


Used to retrieve a list of <code>app_block_builders</code> in a region or to create or delete a <code>app_block_builders</code> resource, use <code>app_block_builder</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_block_builders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::AppBlockBuilder.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.app_block_builders" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
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
name
FROM aws.appstream.app_block_builders
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
 "Name": "{{ Name }}",
 "Platform": "{{ Platform }}",
 "VpcConfig": {
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ]
 },
 "InstanceType": "{{ InstanceType }}"
}
>>>
--required properties only
INSERT INTO aws.appstream.app_block_builders (
 Name,
 Platform,
 VpcConfig,
 InstanceType,
 region
)
SELECT 
{{ Name }},
 {{ Platform }},
 {{ VpcConfig }},
 {{ InstanceType }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "DisplayName": "{{ DisplayName }}",
 "Platform": "{{ Platform }}",
 "AccessEndpoints": [
  {
   "EndpointType": "{{ EndpointType }}",
   "VpceId": "{{ VpceId }}"
  }
 ],
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "VpcConfig": {
  "SecurityGroupIds": [
   "{{ SecurityGroupIds[0] }}"
  ],
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ]
 },
 "EnableDefaultInternetAccess": "{{ EnableDefaultInternetAccess }}",
 "IamRoleArn": "{{ IamRoleArn }}",
 "InstanceType": "{{ InstanceType }}",
 "AppBlockArns": [
  "{{ AppBlockArns[0] }}"
 ]
}
>>>
--all properties
INSERT INTO aws.appstream.app_block_builders (
 Name,
 Description,
 DisplayName,
 Platform,
 AccessEndpoints,
 Tags,
 VpcConfig,
 EnableDefaultInternetAccess,
 IamRoleArn,
 InstanceType,
 AppBlockArns,
 region
)
SELECT 
 {{ Name }},
 {{ Description }},
 {{ DisplayName }},
 {{ Platform }},
 {{ AccessEndpoints }},
 {{ Tags }},
 {{ VpcConfig }},
 {{ EnableDefaultInternetAccess }},
 {{ IamRoleArn }},
 {{ InstanceType }},
 {{ AppBlockArns }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.appstream.app_block_builders
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>app_block_builders</code> resource, the following permissions are required:

### Create
```json
appstream:CreateAppBlockBuilder,
appstream:DescribeAppBlockBuilders,
appstream:StartAppBlockBuilder,
appstream:AssociateAppBlockBuilderAppBlock,
appstream:DescribeAppBlockBuilderAppBlockAssociations,
appstream:TagResource,
iam:PassRole
```

### Delete
```json
appstream:DescribeAppBlockBuilders,
appstream:DeleteAppBlockBuilder,
appstream:DisassociateAppBlockBuilderAppBlock,
appstream:DescribeAppBlockBuilderAppBlockAssociations
```

### List
```json
appstream:DescribeAppBlockBuilders
```


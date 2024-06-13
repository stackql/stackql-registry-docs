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

Creates, updates, deletes or gets an <code>app_block_builder</code> resource or lists <code>app_block_builders</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_block_builders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::AppBlockBuilder.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.app_block_builders" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="platform" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="access_endpoints" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_default_internet_access" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="iam_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="app_block_arns" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, Platform, InstanceType, VpcConfig, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>app_block_builders</code> in a region.
```sql
SELECT
region,
name
FROM aws.appstream.app_block_builders
WHERE region = 'us-east-1';
```
Gets all properties from an <code>app_block_builder</code>.
```sql
SELECT
region,
name,
arn,
description,
display_name,
platform,
access_endpoints,
tags,
vpc_config,
enable_default_internet_access,
iam_role_arn,
created_time,
instance_type,
app_block_arns
FROM aws.appstream.app_block_builders
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app_block_builder</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appstream.app_block_builders (
 Name,
 Platform,
 VpcConfig,
 InstanceType,
 region
)
SELECT 
'{{ Name }}',
 '{{ Platform }}',
 '{{ VpcConfig }}',
 '{{ InstanceType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ Name }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ Platform }}',
 '{{ AccessEndpoints }}',
 '{{ Tags }}',
 '{{ VpcConfig }}',
 '{{ EnableDefaultInternetAccess }}',
 '{{ IamRoleArn }}',
 '{{ InstanceType }}',
 '{{ AppBlockArns }}',
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
  - name: app_block_builder
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: Platform
        value: '{{ Platform }}'
      - name: AccessEndpoints
        value:
          - EndpointType: '{{ EndpointType }}'
            VpceId: '{{ VpceId }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: VpcConfig
        value:
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
      - name: EnableDefaultInternetAccess
        value: '{{ EnableDefaultInternetAccess }}'
      - name: IamRoleArn
        value: '{{ IamRoleArn }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: AppBlockArns
        value:
          - '{{ AppBlockArns[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
appstream:DescribeAppBlockBuilders
```

### Update
```json
appstream:UpdateAppBlockBuilder,
appstream:DescribeAppBlockBuilders,
appstream:StartAppBlockBuilder,
appstream:StopAppBlockBuilder,
appstream:AssociateAppBlockBuilderAppBlock,
appstream:DisassociateAppBlockBuilderAppBlock,
appstream:DescribeAppBlockBuilderAppBlockAssociations,
appstream:ListTagsForResource,
appstream:TagResource,
appstream:UntagResource,
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


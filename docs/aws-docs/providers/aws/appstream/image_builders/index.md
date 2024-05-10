---
title: image_builders
hide_title: false
hide_table_of_contents: false
keywords:
  - image_builders
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


Used to retrieve a list of <code>image_builders</code> in a region or to create or delete a <code>image_builders</code> resource, use <code>image_builder</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_builders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::ImageBuilder</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.image_builders" /></td></tr>
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
FROM aws.appstream.image_builders
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>image_builder</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- image_builder.iql (required properties only)
INSERT INTO aws.appstream.image_builders (
 Name,
 InstanceType,
 region
)
SELECT 
'{{ Name }}',
 '{{ InstanceType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- image_builder.iql (all properties)
INSERT INTO aws.appstream.image_builders (
 Description,
 VpcConfig,
 EnableDefaultInternetAccess,
 DomainJoinInfo,
 AppstreamAgentVersion,
 Name,
 ImageName,
 DisplayName,
 IamRoleArn,
 InstanceType,
 Tags,
 ImageArn,
 AccessEndpoints,
 region
)
SELECT 
 '{{ Description }}',
 '{{ VpcConfig }}',
 '{{ EnableDefaultInternetAccess }}',
 '{{ DomainJoinInfo }}',
 '{{ AppstreamAgentVersion }}',
 '{{ Name }}',
 '{{ ImageName }}',
 '{{ DisplayName }}',
 '{{ IamRoleArn }}',
 '{{ InstanceType }}',
 '{{ Tags }}',
 '{{ ImageArn }}',
 '{{ AccessEndpoints }}',
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
  - name: image_builder
    props:
      - name: Description
        value: '{{ Description }}'
      - name: VpcConfig
        value:
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
      - name: EnableDefaultInternetAccess
        value: '{{ EnableDefaultInternetAccess }}'
      - name: DomainJoinInfo
        value:
          OrganizationalUnitDistinguishedName: '{{ OrganizationalUnitDistinguishedName }}'
          DirectoryName: '{{ DirectoryName }}'
      - name: AppstreamAgentVersion
        value: '{{ AppstreamAgentVersion }}'
      - name: Name
        value: '{{ Name }}'
      - name: ImageName
        value: '{{ ImageName }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: IamRoleArn
        value: '{{ IamRoleArn }}'
      - name: InstanceType
        value: '{{ InstanceType }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: ImageArn
        value: '{{ ImageArn }}'
      - name: AccessEndpoints
        value:
          - EndpointType: '{{ EndpointType }}'
            VpceId: '{{ VpceId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.appstream.image_builders
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>image_builders</code> resource, the following permissions are required:

### Create
```json
appstream:CreateImageBuilder,
appstream:CreateImageBuilderStreamingURL,
appstream:CreateStreamingURL,
appstream:DeleteImageBuilder,
appstream:DescribeImageBuilders,
appstream:StartImageBuilder,
appstream:StopImageBuilder,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Delete
```json
appstream:CreateImageBuilder,
appstream:CreateImageBuilderStreamingURL,
appstream:CreateStreamingURL,
appstream:DeleteImageBuilder,
appstream:DescribeImageBuilders,
appstream:StartImageBuilder,
appstream:StopImageBuilder,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### List
```json
appstream:CreateImageBuilder,
appstream:CreateImageBuilderStreamingURL,
appstream:CreateStreamingURL,
appstream:DeleteImageBuilder,
appstream:DescribeImageBuilders,
appstream:StartImageBuilder,
appstream:StopImageBuilder,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```


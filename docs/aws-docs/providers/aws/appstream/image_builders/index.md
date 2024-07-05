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

Creates, updates, deletes or gets an <code>image_builder</code> resource or lists <code>image_builders</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_builders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::ImageBuilder</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.image_builders" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_default_internet_access" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_join_info" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="appstream_agent_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="iam_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instance_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="streaming_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="access_endpoints" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="InstanceType, Name, region" /></td>
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
Gets all <code>image_builders</code> in a region.
```sql
SELECT
region,
description,
vpc_config,
enable_default_internet_access,
domain_join_info,
appstream_agent_version,
name,
image_name,
display_name,
iam_role_arn,
instance_type,
tags,
streaming_url,
image_arn,
access_endpoints
FROM aws.appstream.image_builders
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>image_builder</code>.
```sql
SELECT
region,
description,
vpc_config,
enable_default_internet_access,
domain_join_info,
appstream_agent_version,
name,
image_name,
display_name,
iam_role_arn,
instance_type,
tags,
streaming_url,
image_arn,
access_endpoints
FROM aws.appstream.image_builders
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
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


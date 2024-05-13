---
title: infrastructure_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - infrastructure_configurations
  - imagebuilder
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


Used to retrieve a list of <code>infrastructure_configurations</code> in a region or to create or delete a <code>infrastructure_configurations</code> resource, use <code>infrastructure_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>infrastructure_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::InfrastructureConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.infrastructure_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr>
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
    <td><CopyableCode code="Name, InstanceProfileName, region" /></td>
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
arn
FROM aws.imagebuilder.infrastructure_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>infrastructure_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.imagebuilder.infrastructure_configurations (
 Name,
 InstanceProfileName,
 region
)
SELECT 
'{{ Name }}',
 '{{ InstanceProfileName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.imagebuilder.infrastructure_configurations (
 Name,
 Description,
 InstanceTypes,
 SecurityGroupIds,
 Logging,
 SubnetId,
 KeyPair,
 TerminateInstanceOnFailure,
 InstanceProfileName,
 InstanceMetadataOptions,
 SnsTopicArn,
 ResourceTags,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ InstanceTypes }}',
 '{{ SecurityGroupIds }}',
 '{{ Logging }}',
 '{{ SubnetId }}',
 '{{ KeyPair }}',
 '{{ TerminateInstanceOnFailure }}',
 '{{ InstanceProfileName }}',
 '{{ InstanceMetadataOptions }}',
 '{{ SnsTopicArn }}',
 '{{ ResourceTags }}',
 '{{ Tags }}',
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
  - name: infrastructure_configuration
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: InstanceTypes
        value:
          - '{{ InstanceTypes[0] }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: Logging
        value:
          S3Logs:
            S3BucketName: '{{ S3BucketName }}'
            S3KeyPrefix: '{{ S3KeyPrefix }}'
      - name: SubnetId
        value: '{{ SubnetId }}'
      - name: KeyPair
        value: '{{ KeyPair }}'
      - name: TerminateInstanceOnFailure
        value: '{{ TerminateInstanceOnFailure }}'
      - name: InstanceProfileName
        value: '{{ InstanceProfileName }}'
      - name: InstanceMetadataOptions
        value:
          HttpPutResponseHopLimit: '{{ HttpPutResponseHopLimit }}'
          HttpTokens: '{{ HttpTokens }}'
      - name: SnsTopicArn
        value: '{{ SnsTopicArn }}'
      - name: ResourceTags
        value: {}
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.imagebuilder.infrastructure_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>infrastructure_configurations</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
iam:GetRole,
iam:GetInstanceProfile,
iam:CreateServiceLinkedRole,
sns:Publish,
imagebuilder:TagResource,
imagebuilder:GetInfrastructureConfiguration,
imagebuilder:CreateInfrastructureConfiguration
```

### Delete
```json
imagebuilder:UnTagResource,
imagebuilder:GetInfrastructureConfiguration,
imagebuilder:DeleteInfrastructureConfiguration
```

### List
```json
imagebuilder:ListInfrastructureConfigurations
```


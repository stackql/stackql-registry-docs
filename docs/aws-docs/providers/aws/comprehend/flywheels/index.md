---
title: flywheels
hide_title: false
hide_table_of_contents: false
keywords:
  - flywheels
  - comprehend
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


Used to retrieve a list of <code>flywheels</code> in a region or to create or delete a <code>flywheels</code> resource, use <code>flywheel</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flywheels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Comprehend::Flywheel resource creates an Amazon Comprehend Flywheel that enables customer to train their model.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.comprehend.flywheels" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.comprehend.flywheels
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>flywheel</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- flywheel.iql (required properties only)
INSERT INTO aws.comprehend.flywheels (
 DataAccessRoleArn,
 DataLakeS3Uri,
 FlywheelName,
 region
)
SELECT 
'{{ DataAccessRoleArn }}',
 '{{ DataLakeS3Uri }}',
 '{{ FlywheelName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- flywheel.iql (all properties)
INSERT INTO aws.comprehend.flywheels (
 ActiveModelArn,
 DataAccessRoleArn,
 DataLakeS3Uri,
 DataSecurityConfig,
 FlywheelName,
 ModelType,
 Tags,
 TaskConfig,
 region
)
SELECT 
 '{{ ActiveModelArn }}',
 '{{ DataAccessRoleArn }}',
 '{{ DataLakeS3Uri }}',
 '{{ DataSecurityConfig }}',
 '{{ FlywheelName }}',
 '{{ ModelType }}',
 '{{ Tags }}',
 '{{ TaskConfig }}',
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
  - name: flywheel
    props:
      - name: ActiveModelArn
        value: '{{ ActiveModelArn }}'
      - name: DataAccessRoleArn
        value: '{{ DataAccessRoleArn }}'
      - name: DataLakeS3Uri
        value: '{{ DataLakeS3Uri }}'
      - name: DataSecurityConfig
        value:
          ModelKmsKeyId: '{{ ModelKmsKeyId }}'
          VolumeKmsKeyId: null
          DataLakeKmsKeyId: null
          VpcConfig:
            SecurityGroupIds:
              - '{{ SecurityGroupIds[0] }}'
            Subnets:
              - '{{ Subnets[0] }}'
      - name: FlywheelName
        value: '{{ FlywheelName }}'
      - name: ModelType
        value: '{{ ModelType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TaskConfig
        value:
          LanguageCode: '{{ LanguageCode }}'
          DocumentClassificationConfig:
            Mode: '{{ Mode }}'
            Labels:
              - '{{ Labels[0] }}'
          EntityRecognitionConfig:
            EntityTypes:
              - Type: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.comprehend.flywheels
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flywheels</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
comprehend:CreateFlywheel,
comprehend:DescribeFlywheel,
comprehend:ListTagsForResource
```

### Delete
```json
comprehend:DeleteFlywheel,
comprehend:DescribeFlywheel
```

### List
```json
comprehend:ListFlywheels
```


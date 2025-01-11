---
title: rotation_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - rotation_schedules
  - secretsmanager
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

Creates, updates, deletes or gets a <code>rotation_schedule</code> resource or lists <code>rotation_schedules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rotation_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecretsManager::RotationSchedule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.secretsmanager.rotation_schedules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="hosted_rotation_lambda" /></td><td><code>object</code></td><td>Creates a new Lambda rotation function based on one of the Secrets Manager rotation function templates. To use a rotation function that already exists, specify RotationLambdaARN instead.</td></tr>
<tr><td><CopyableCode code="secret_id" /></td><td><code>string</code></td><td>The ARN or name of the secret to rotate.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ARN of the secret.</td></tr>
<tr><td><CopyableCode code="rotate_immediately_on_update" /></td><td><code>boolean</code></td><td>Specifies whether to rotate the secret immediately or wait until the next scheduled rotation window.</td></tr>
<tr><td><CopyableCode code="rotation_lambda_arn" /></td><td><code>string</code></td><td>The ARN of an existing Lambda rotation function. To specify a rotation function that is also defined in this template, use the Ref function.</td></tr>
<tr><td><CopyableCode code="rotation_rules" /></td><td><code>object</code></td><td>A structure that defines the rotation configuration for this secret.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html"><code>AWS::SecretsManager::RotationSchedule</code></a>.

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
    <td><CopyableCode code="SecretId, region" /></td>
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
Gets all <code>rotation_schedules</code> in a region.
```sql
SELECT
region,
hosted_rotation_lambda,
secret_id,
id,
rotate_immediately_on_update,
rotation_lambda_arn,
rotation_rules
FROM aws.secretsmanager.rotation_schedules
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>rotation_schedule</code>.
```sql
SELECT
region,
hosted_rotation_lambda,
secret_id,
id,
rotate_immediately_on_update,
rotation_lambda_arn,
rotation_rules
FROM aws.secretsmanager.rotation_schedules
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rotation_schedule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.secretsmanager.rotation_schedules (
 SecretId,
 region
)
SELECT 
'{{ SecretId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.secretsmanager.rotation_schedules (
 HostedRotationLambda,
 SecretId,
 RotateImmediatelyOnUpdate,
 RotationLambdaARN,
 RotationRules,
 region
)
SELECT 
 '{{ HostedRotationLambda }}',
 '{{ SecretId }}',
 '{{ RotateImmediatelyOnUpdate }}',
 '{{ RotationLambdaARN }}',
 '{{ RotationRules }}',
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
  - name: rotation_schedule
    props:
      - name: HostedRotationLambda
        value:
          Runtime: '{{ Runtime }}'
          KmsKeyArn: '{{ KmsKeyArn }}'
          MasterSecretArn: '{{ MasterSecretArn }}'
          RotationLambdaName: '{{ RotationLambdaName }}'
          RotationType: '{{ RotationType }}'
          ExcludeCharacters: '{{ ExcludeCharacters }}'
          VpcSecurityGroupIds: '{{ VpcSecurityGroupIds }}'
          MasterSecretKmsKeyArn: '{{ MasterSecretKmsKeyArn }}'
          SuperuserSecretArn: '{{ SuperuserSecretArn }}'
          SuperuserSecretKmsKeyArn: '{{ SuperuserSecretKmsKeyArn }}'
          VpcSubnetIds: '{{ VpcSubnetIds }}'
      - name: SecretId
        value: '{{ SecretId }}'
      - name: RotateImmediatelyOnUpdate
        value: '{{ RotateImmediatelyOnUpdate }}'
      - name: RotationLambdaARN
        value: '{{ RotationLambdaARN }}'
      - name: RotationRules
        value:
          ScheduleExpression: '{{ ScheduleExpression }}'
          Duration: '{{ Duration }}'
          AutomaticallyAfterDays: '{{ AutomaticallyAfterDays }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.secretsmanager.rotation_schedules
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rotation_schedules</code> resource, the following permissions are required:

### Read
```json
secretsmanager:DescribeSecret
```

### Create
```json
secretsmanager:RotateSecret,
secretsmanager:DescribeSecret,
lambda:InvokeFunction
```

### Update
```json
secretsmanager:RotateSecret,
secretsmanager:DescribeSecret,
lambda:InvokeFunction
```

### List
```json
secretsmanager:DescribeSecret,
secretsmanager:ListSecrets
```

### Delete
```json
secretsmanager:CancelRotateSecret,
secretsmanager:DescribeSecret
```

---
title: state_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machines
  - stepfunctions
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

Creates, updates, deletes or gets a <code>state_machine</code> resource or lists <code>state_machines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for StateMachine</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.stepfunctions.state_machines" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="definition_string" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_machine_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_machine_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_machine_revision_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tracing_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="definition_s3_location" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="definition_substitutions" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html"><code>AWS::StepFunctions::StateMachine</code></a>.

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
    <td><CopyableCode code="RoleArn, region" /></td>
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
Gets all <code>state_machines</code> in a region.
```sql
SELECT
region,
arn,
name,
definition_string,
role_arn,
state_machine_name,
state_machine_type,
state_machine_revision_id,
logging_configuration,
tracing_configuration,
encryption_configuration,
definition_s3_location,
definition_substitutions,
definition,
tags
FROM aws.stepfunctions.state_machines
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>state_machine</code>.
```sql
SELECT
region,
arn,
name,
definition_string,
role_arn,
state_machine_name,
state_machine_type,
state_machine_revision_id,
logging_configuration,
tracing_configuration,
encryption_configuration,
definition_s3_location,
definition_substitutions,
definition,
tags
FROM aws.stepfunctions.state_machines
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>state_machine</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.stepfunctions.state_machines (
 RoleArn,
 region
)
SELECT 
'{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.stepfunctions.state_machines (
 DefinitionString,
 RoleArn,
 StateMachineName,
 StateMachineType,
 LoggingConfiguration,
 TracingConfiguration,
 EncryptionConfiguration,
 DefinitionS3Location,
 DefinitionSubstitutions,
 Definition,
 Tags,
 region
)
SELECT 
 '{{ DefinitionString }}',
 '{{ RoleArn }}',
 '{{ StateMachineName }}',
 '{{ StateMachineType }}',
 '{{ LoggingConfiguration }}',
 '{{ TracingConfiguration }}',
 '{{ EncryptionConfiguration }}',
 '{{ DefinitionS3Location }}',
 '{{ DefinitionSubstitutions }}',
 '{{ Definition }}',
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
  - name: state_machine
    props:
      - name: DefinitionString
        value: '{{ DefinitionString }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: StateMachineName
        value: '{{ StateMachineName }}'
      - name: StateMachineType
        value: '{{ StateMachineType }}'
      - name: LoggingConfiguration
        value:
          Level: '{{ Level }}'
          IncludeExecutionData: '{{ IncludeExecutionData }}'
          Destinations:
            - CloudWatchLogsLogGroup:
                LogGroupArn: '{{ LogGroupArn }}'
      - name: TracingConfiguration
        value:
          Enabled: '{{ Enabled }}'
      - name: EncryptionConfiguration
        value:
          KmsKeyId: '{{ KmsKeyId }}'
          KmsDataKeyReusePeriodSeconds: '{{ KmsDataKeyReusePeriodSeconds }}'
          Type: '{{ Type }}'
      - name: DefinitionS3Location
        value:
          Bucket: '{{ Bucket }}'
          Key: '{{ Key }}'
          Version: '{{ Version }}'
      - name: DefinitionSubstitutions
        value: {}
      - name: Definition
        value: {}
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.stepfunctions.state_machines
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>state_machines</code> resource, the following permissions are required:

### Create
```json
states:CreateStateMachine,
states:DescribeStateMachine,
states:TagResource,
iam:PassRole,
s3:GetObject,
kms:DescribeKey,
kms:GenerateDataKey
```

### Read
```json
states:DescribeStateMachine,
states:ListTagsForResource,
kms:Decrypt
```

### Update
```json
states:UpdateStateMachine,
states:TagResource,
states:UntagResource,
states:ListTagsForResource,
iam:PassRole,
kms:DescribeKey,
kms:GenerateDataKey
```

### Delete
```json
states:DeleteStateMachine,
states:DescribeStateMachine
```

### List
```json
states:ListStateMachines
```

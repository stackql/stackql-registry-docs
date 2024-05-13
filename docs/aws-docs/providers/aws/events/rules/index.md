---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - events
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


Used to retrieve a list of <code>rules</code> in a region or to create or delete a <code>rules</code> resource, use <code>rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Rule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the rule, such as arn:aws:events:us-east-2:123456789012:rule&#x2F;example.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
FROM aws.events.rules
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.events.rules (
 EventBusName,
 EventPattern,
 ScheduleExpression,
 Description,
 State,
 Targets,
 RoleArn,
 Name,
 region
)
SELECT 
'{{ EventBusName }}',
 '{{ EventPattern }}',
 '{{ ScheduleExpression }}',
 '{{ Description }}',
 '{{ State }}',
 '{{ Targets }}',
 '{{ RoleArn }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.events.rules (
 EventBusName,
 EventPattern,
 ScheduleExpression,
 Description,
 State,
 Targets,
 RoleArn,
 Name,
 region
)
SELECT 
 '{{ EventBusName }}',
 '{{ EventPattern }}',
 '{{ ScheduleExpression }}',
 '{{ Description }}',
 '{{ State }}',
 '{{ Targets }}',
 '{{ RoleArn }}',
 '{{ Name }}',
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
  - name: rule
    props:
      - name: EventBusName
        value: '{{ EventBusName }}'
      - name: EventPattern
        value: {}
      - name: ScheduleExpression
        value: '{{ ScheduleExpression }}'
      - name: Description
        value: '{{ Description }}'
      - name: State
        value: '{{ State }}'
      - name: Targets
        value:
          - InputPath: '{{ InputPath }}'
            HttpParameters:
              PathParameterValues:
                - '{{ PathParameterValues[0] }}'
              HeaderParameters: {}
              QueryStringParameters: {}
            DeadLetterConfig:
              Arn: '{{ Arn }}'
            RunCommandParameters:
              RunCommandTargets:
                - Values:
                    - '{{ Values[0] }}'
                  Key: '{{ Key }}'
            InputTransformer:
              InputPathsMap: {}
              InputTemplate: '{{ InputTemplate }}'
            KinesisParameters:
              PartitionKeyPath: '{{ PartitionKeyPath }}'
            RoleArn: '{{ RoleArn }}'
            RedshiftDataParameters:
              StatementName: '{{ StatementName }}'
              Sqls:
                - '{{ Sqls[0] }}'
              Database: '{{ Database }}'
              SecretManagerArn: '{{ SecretManagerArn }}'
              DbUser: '{{ DbUser }}'
              Sql: '{{ Sql }}'
              WithEvent: '{{ WithEvent }}'
            AppSyncParameters:
              GraphQLOperation: '{{ GraphQLOperation }}'
            Input: '{{ Input }}'
            SqsParameters:
              MessageGroupId: '{{ MessageGroupId }}'
            EcsParameters:
              PlatformVersion: '{{ PlatformVersion }}'
              Group: '{{ Group }}'
              EnableECSManagedTags: '{{ EnableECSManagedTags }}'
              EnableExecuteCommand: '{{ EnableExecuteCommand }}'
              PlacementConstraints:
                - Type: '{{ Type }}'
                  Expression: '{{ Expression }}'
              PropagateTags: '{{ PropagateTags }}'
              TaskCount: '{{ TaskCount }}'
              PlacementStrategies:
                - Field: '{{ Field }}'
                  Type: '{{ Type }}'
              CapacityProviderStrategy:
                - CapacityProvider: '{{ CapacityProvider }}'
                  Base: '{{ Base }}'
                  Weight: '{{ Weight }}'
              LaunchType: '{{ LaunchType }}'
              ReferenceId: '{{ ReferenceId }}'
              TagList:
                - Value: '{{ Value }}'
                  Key: '{{ Key }}'
              NetworkConfiguration:
                AwsVpcConfiguration:
                  SecurityGroups:
                    - '{{ SecurityGroups[0] }}'
                  Subnets:
                    - '{{ Subnets[0] }}'
                  AssignPublicIp: '{{ AssignPublicIp }}'
              TaskDefinitionArn: '{{ TaskDefinitionArn }}'
            BatchParameters:
              ArrayProperties:
                Size: '{{ Size }}'
              JobName: '{{ JobName }}'
              RetryStrategy:
                Attempts: '{{ Attempts }}'
              JobDefinition: '{{ JobDefinition }}'
            Id: '{{ Id }}'
            Arn: '{{ Arn }}'
            SageMakerPipelineParameters:
              PipelineParameterList:
                - Value: '{{ Value }}'
                  Name: '{{ Name }}'
            RetryPolicy:
              MaximumRetryAttempts: '{{ MaximumRetryAttempts }}'
              MaximumEventAgeInSeconds: '{{ MaximumEventAgeInSeconds }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.events.rules
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rules</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
events:DescribeRule,
events:PutRule,
events:PutTargets
```

### List
```json
events:ListRules
```

### Delete
```json
iam:PassRole,
events:DescribeRule,
events:DeleteRule,
events:RemoveTargets,
events:ListTargetsByRule
```


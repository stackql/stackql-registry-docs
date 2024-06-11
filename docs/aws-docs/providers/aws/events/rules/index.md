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

Creates, updates, deletes or gets a <code>rule</code> resource or lists <code>rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Rule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="event_bus_name" /></td><td><code>string</code></td><td>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</td></tr>
<tr><td><CopyableCode code="event_pattern" /></td><td><code>object</code></td><td>The event pattern of the rule. For more information, see Events and Event Patterns in the Amazon EventBridge User Guide.</td></tr>
<tr><td><CopyableCode code="schedule_expression" /></td><td><code>string</code></td><td>The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5 minutes)". For more information, see Creating an Amazon EventBridge rule that runs on a schedule.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the rule.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the rule.</td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>array</code></td><td>Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.<br/>Targets are the resources that are invoked when a rule is triggered.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the rule, such as arn:aws:events:us-east-2:123456789012:rule/example.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the role that is used for target invocation.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the rule.</td></tr>
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
List all <code>rules</code> in a region.
```sql
SELECT
region,
arn
FROM aws.events.rules
WHERE region = 'us-east-1';
```
Gets all properties from a <code>rule</code>.
```sql
SELECT
region,
event_bus_name,
event_pattern,
schedule_expression,
description,
state,
targets,
arn,
role_arn,
name
FROM aws.events.rules
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

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

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.events.rules
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rules</code> resource, the following permissions are required:

### Read
```json
iam:PassRole,
events:DescribeRule,
events:ListTargetsByRule
```

### Create
```json
iam:PassRole,
events:DescribeRule,
events:PutRule,
events:PutTargets
```

### Update
```json
iam:PassRole,
events:DescribeRule,
events:PutRule,
events:RemoveTargets,
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


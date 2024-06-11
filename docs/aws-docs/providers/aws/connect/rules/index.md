---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - connect
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS:Connect::Rule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the rule.</td></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the rule.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr>
<tr><td><CopyableCode code="trigger_event_source" /></td><td><code>object</code></td><td>The event source that triggers the rule.</td></tr>
<tr><td><CopyableCode code="function" /></td><td><code>string</code></td><td>The conditions of a rule.</td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>object</code></td><td>The list of actions that will be executed when a rule is triggered.</td></tr>
<tr><td><CopyableCode code="publish_status" /></td><td><code>string</code></td><td>The publish status of a rule, either draft or published.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
    <td><CopyableCode code="Name, InstanceArn, TriggerEventSource, Function, Actions, PublishStatus, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>rule</code>.
```sql
SELECT
region,
name,
rule_arn,
instance_arn,
trigger_event_source,
function,
actions,
publish_status,
tags
FROM aws.connect.rules
WHERE region = 'us-east-1' AND data__Identifier = '<RuleArn>';
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
INSERT INTO aws.connect.rules (
 Name,
 InstanceArn,
 TriggerEventSource,
 Function,
 Actions,
 PublishStatus,
 region
)
SELECT 
'{{ Name }}',
 '{{ InstanceArn }}',
 '{{ TriggerEventSource }}',
 '{{ Function }}',
 '{{ Actions }}',
 '{{ PublishStatus }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.rules (
 Name,
 InstanceArn,
 TriggerEventSource,
 Function,
 Actions,
 PublishStatus,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ InstanceArn }}',
 '{{ TriggerEventSource }}',
 '{{ Function }}',
 '{{ Actions }}',
 '{{ PublishStatus }}',
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
  - name: rule
    props:
      - name: Name
        value: '{{ Name }}'
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: TriggerEventSource
        value:
          EventSourceName: '{{ EventSourceName }}'
          IntegrationAssociationArn: '{{ IntegrationAssociationArn }}'
      - name: Function
        value: '{{ Function }}'
      - name: Actions
        value:
          AssignContactCategoryActions:
            - {}
          EventBridgeActions:
            - Name: '{{ Name }}'
          TaskActions:
            - Name: '{{ Name }}'
              Description: '{{ Description }}'
              ContactFlowArn: '{{ ContactFlowArn }}'
              References: null
          SendNotificationActions:
            - DeliveryMethod: '{{ DeliveryMethod }}'
              Subject: '{{ Subject }}'
              Content: '{{ Content }}'
              ContentType: '{{ ContentType }}'
              Recipient:
                UserTags: null
                UserArns:
                  - '{{ UserArns[0] }}'
          CreateCaseActions:
            - Fields:
                - Id:
                    Name: '{{ Name }}'
                  Description: '{{ Description }}'
                  Type: '{{ Type }}'
                  SingleSelectOptions:
                    - '{{ SingleSelectOptions[0] }}'
              TemplateId: '{{ TemplateId }}'
          UpdateCaseActions:
            - Fields: null
          EndAssociatedTasksActions:
            - {}
      - name: PublishStatus
        value: '{{ PublishStatus }}'
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
DELETE FROM aws.connect.rules
WHERE data__Identifier = '<RuleArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rules</code> resource, the following permissions are required:

### Create
```json
connect:CreateRule,
cases:GetTemplate,
cases:ListFields,
cases:ListFieldOptions
```

### Read
```json
connect:DescribeRule
```

### Delete
```json
connect:DeleteRule,
connect:UntagResource
```

### Update
```json
connect:UpdateRule,
cases:GetTemplate,
cases:ListFields,
cases:ListFieldOptions,
connect:TagResource,
connect:UntagResource
```


---
title: custom_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_actions
  - chatbot
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

Creates, updates, deletes or gets a <code>custom_action</code> resource or lists <code>custom_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Chatbot::CustomAction Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.chatbot.custom_actions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="action_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="alias_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attachments" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_action_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-customaction.html"><code>AWS::Chatbot::CustomAction</code></a>.

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
    <td><CopyableCode code="ActionName, Definition, region" /></td>
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
Gets all <code>custom_actions</code> in a region.
```sql
SELECT
region,
action_name,
alias_name,
attachments,
custom_action_arn,
definition,
tags
FROM aws.chatbot.custom_actions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>custom_action</code>.
```sql
SELECT
region,
action_name,
alias_name,
attachments,
custom_action_arn,
definition,
tags
FROM aws.chatbot.custom_actions
WHERE region = 'us-east-1' AND data__Identifier = '<CustomActionArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_action</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.chatbot.custom_actions (
 ActionName,
 Definition,
 region
)
SELECT 
'{{ ActionName }}',
 '{{ Definition }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.chatbot.custom_actions (
 ActionName,
 AliasName,
 Attachments,
 Definition,
 Tags,
 region
)
SELECT 
 '{{ ActionName }}',
 '{{ AliasName }}',
 '{{ Attachments }}',
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
  - name: custom_action
    props:
      - name: ActionName
        value: '{{ ActionName }}'
      - name: AliasName
        value: '{{ AliasName }}'
      - name: Attachments
        value:
          - NotificationType: '{{ NotificationType }}'
            ButtonText: '{{ ButtonText }}'
            Criteria:
              - Operator: '{{ Operator }}'
                VariableName: '{{ VariableName }}'
                Value: '{{ Value }}'
            Variables: {}
      - name: Definition
        value:
          CommandText: '{{ CommandText }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.chatbot.custom_actions
WHERE data__Identifier = '<CustomActionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>custom_actions</code> resource, the following permissions are required:

### Create
```json
chatbot:CreateCustomAction,
chatbot:GetCustomAction,
chatbot:TagResource,
chatbot:ListTagsForResource
```

### Read
```json
chatbot:GetCustomAction,
chatbot:ListTagsForResource
```

### Update
```json
chatbot:UpdateCustomAction,
chatbot:GetCustomAction,
chatbot:TagResource,
chatbot:UntagResource,
chatbot:ListTagsForResource
```

### Delete
```json
chatbot:DeleteCustomAction
```

### List
```json
chatbot:ListCustomActions
```

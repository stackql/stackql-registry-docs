---
title: commands
hide_title: false
hide_table_of_contents: false
keywords:
  - commands
  - iot
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

Creates, updates, deletes or gets a <code>command</code> resource or lists <code>commands</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents the resource definition of AWS IoT Command.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.commands" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="command_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the command.</td></tr>
<tr><td><CopyableCode code="command_id" /></td><td><code>string</code></td><td>The unique identifier for the command.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time when the command was created.</td></tr>
<tr><td><CopyableCode code="deprecated" /></td><td><code>boolean</code></td><td>A flag indicating whether the command is deprecated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the command.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>The display name for the command.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The date and time when the command was last updated.</td></tr>
<tr><td><CopyableCode code="mandatory_parameters" /></td><td><code>array</code></td><td>The list of mandatory parameters for the command.</td></tr>
<tr><td><CopyableCode code="namespace" /></td><td><code>string</code></td><td>The namespace to which the command belongs.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The customer role associated with the command.</td></tr>
<tr><td><CopyableCode code="payload" /></td><td><code>object</code></td><td>The payload associated with the command.</td></tr>
<tr><td><CopyableCode code="pending_deletion" /></td><td><code>boolean</code></td><td>A flag indicating whether the command is pending deletion.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to be associated with the command.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-command.html"><code>AWS::IoT::Command</code></a>.

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
    <td><CopyableCode code="CommandId, region" /></td>
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
Gets all <code>commands</code> in a region.
```sql
SELECT
region,
command_arn,
command_id,
created_at,
deprecated,
description,
display_name,
last_updated_at,
mandatory_parameters,
namespace,
role_arn,
payload,
pending_deletion,
tags
FROM aws.iot.commands
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>command</code>.
```sql
SELECT
region,
command_arn,
command_id,
created_at,
deprecated,
description,
display_name,
last_updated_at,
mandatory_parameters,
namespace,
role_arn,
payload,
pending_deletion,
tags
FROM aws.iot.commands
WHERE region = 'us-east-1' AND data__Identifier = '<CommandId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>command</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.commands (
 CommandId,
 region
)
SELECT 
'{{ CommandId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.commands (
 CommandId,
 CreatedAt,
 Deprecated,
 Description,
 DisplayName,
 LastUpdatedAt,
 MandatoryParameters,
 Namespace,
 RoleArn,
 Payload,
 PendingDeletion,
 Tags,
 region
)
SELECT 
 '{{ CommandId }}',
 '{{ CreatedAt }}',
 '{{ Deprecated }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ LastUpdatedAt }}',
 '{{ MandatoryParameters }}',
 '{{ Namespace }}',
 '{{ RoleArn }}',
 '{{ Payload }}',
 '{{ PendingDeletion }}',
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
  - name: command
    props:
      - name: CommandId
        value: '{{ CommandId }}'
      - name: CreatedAt
        value: '{{ CreatedAt }}'
      - name: Deprecated
        value: '{{ Deprecated }}'
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: LastUpdatedAt
        value: '{{ LastUpdatedAt }}'
      - name: MandatoryParameters
        value:
          - Name: '{{ Name }}'
            Value:
              S: '{{ S }}'
              B: '{{ B }}'
              I: '{{ I }}'
              L: '{{ L }}'
              D: null
              BIN: '{{ BIN }}'
              UL: '{{ UL }}'
            DefaultValue: null
            Description: '{{ Description }}'
      - name: Namespace
        value: '{{ Namespace }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Payload
        value:
          Content: '{{ Content }}'
          ContentType: '{{ ContentType }}'
      - name: PendingDeletion
        value: '{{ PendingDeletion }}'
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
DELETE FROM aws.iot.commands
WHERE data__Identifier = '<CommandId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>commands</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
iot:CreateCommand,
iot:TagResource
```

### Read
```json
iot:GetCommand,
iot:ListTagsForResource
```

### Update
```json
iam:PassRole,
iot:UpdateCommand,
iot:GetCommand,
iot:TagResource,
iot:UntagResource,
iot:ListTagsForResource
```

### Delete
```json
iot:GetCommand,
iot:UpdateCommand,
iot:DeleteCommand
```

### List
```json
iot:ListCommands
```

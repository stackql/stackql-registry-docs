---
title: task_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - task_templates
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

Creates, updates, deletes or gets a <code>task_template</code> resource or lists <code>task_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::TaskTemplate.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.task_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The identifier (arn) of the task template.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier (arn) of the instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the task template.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the task template.</td></tr>
<tr><td><CopyableCode code="contact_flow_arn" /></td><td><code>string</code></td><td>The identifier of the contact flow.</td></tr>
<tr><td><CopyableCode code="self_assign_contact_flow_arn" /></td><td><code>string</code></td><td>The identifier of the contact flow.</td></tr>
<tr><td><CopyableCode code="constraints" /></td><td><code>object</code></td><td>The constraints for the task template</td></tr>
<tr><td><CopyableCode code="defaults" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>array</code></td><td>The list of task template's fields</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the task template</td></tr>
<tr><td><CopyableCode code="client_token" /></td><td><code>string</code></td><td>the client token string in uuid format</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html"><code>AWS::Connect::TaskTemplate</code></a>.

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
    <td><CopyableCode code="InstanceArn, region" /></td>
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
Gets all <code>task_templates</code> in a region.
```sql
SELECT
region,
arn,
instance_arn,
name,
description,
contact_flow_arn,
self_assign_contact_flow_arn,
constraints,
defaults,
fields,
status,
client_token,
tags
FROM aws.connect.task_templates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>task_template</code>.
```sql
SELECT
region,
arn,
instance_arn,
name,
description,
contact_flow_arn,
self_assign_contact_flow_arn,
constraints,
defaults,
fields,
status,
client_token,
tags
FROM aws.connect.task_templates
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>task_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.task_templates (
 InstanceArn,
 region
)
SELECT 
'{{ InstanceArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.task_templates (
 InstanceArn,
 Name,
 Description,
 ContactFlowArn,
 SelfAssignContactFlowArn,
 Constraints,
 Defaults,
 Fields,
 Status,
 ClientToken,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ ContactFlowArn }}',
 '{{ SelfAssignContactFlowArn }}',
 '{{ Constraints }}',
 '{{ Defaults }}',
 '{{ Fields }}',
 '{{ Status }}',
 '{{ ClientToken }}',
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
  - name: task_template
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: ContactFlowArn
        value: '{{ ContactFlowArn }}'
      - name: SelfAssignContactFlowArn
        value: '{{ SelfAssignContactFlowArn }}'
      - name: Constraints
        value:
          InvisibleFields:
            - Id:
                Name: '{{ Name }}'
          RequiredFields:
            - Id: null
          ReadOnlyFields:
            - Id: null
      - name: Defaults
        value:
          - Id: null
            DefaultValue: '{{ DefaultValue }}'
      - name: Fields
        value:
          - Id: null
            Description: '{{ Description }}'
            Type: '{{ Type }}'
            SingleSelectOptions:
              - '{{ SingleSelectOptions[0] }}'
      - name: Status
        value: '{{ Status }}'
      - name: ClientToken
        value: '{{ ClientToken }}'
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
DELETE FROM aws.connect.task_templates
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>task_templates</code> resource, the following permissions are required:

### Create
```json
connect:CreateTaskTemplate,
connect:TagResource
```

### Read
```json
connect:GetTaskTemplate
```

### List
```json
connect:ListTaskTemplates
```

### Update
```json
connect:UpdateTaskTemplate,
connect:TagResource,
connect:UntagResource
```

### Delete
```json
connect:DeleteTaskTemplate,
connect:UntagResource,
connect:GetTaskTemplate
```

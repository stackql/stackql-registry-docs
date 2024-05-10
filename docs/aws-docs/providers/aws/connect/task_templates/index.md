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


Used to retrieve a list of <code>task_templates</code> in a region or to create or delete a <code>task_templates</code> resource, use <code>task_template</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::TaskTemplate.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.task_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The identifier (arn) of the task template.</td></tr>
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
FROM aws.connect.task_templates
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- task_template.iql (required properties only)
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
-- task_template.iql (all properties)
INSERT INTO aws.connect.task_templates (
 InstanceArn,
 Name,
 Description,
 ContactFlowArn,
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

## `DELETE` Example

```sql
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

### List
```json
connect:ListTaskTemplates
```

### Delete
```json
connect:DeleteTaskTemplate,
connect:UntagResource,
connect:GetTaskTemplate
```


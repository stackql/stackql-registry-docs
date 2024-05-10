---
title: evaluation_forms
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluation_forms
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


Used to retrieve a list of <code>evaluation_forms</code> in a region or to create or delete a <code>evaluation_forms</code> resource, use <code>evaluation_form</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>evaluation_forms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::EvaluationForm</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.evaluation_forms" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="evaluation_form_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the evaluation form.</td></tr>
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
evaluation_form_arn
FROM aws.connect.evaluation_forms
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>evaluation_form</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- evaluation_form.iql (required properties only)
INSERT INTO aws.connect.evaluation_forms (
 Title,
 InstanceArn,
 Items,
 Status,
 region
)
SELECT 
'{{ Title }}',
 '{{ InstanceArn }}',
 '{{ Items }}',
 '{{ Status }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- evaluation_form.iql (all properties)
INSERT INTO aws.connect.evaluation_forms (
 Title,
 Description,
 InstanceArn,
 Items,
 ScoringStrategy,
 Status,
 Tags,
 region
)
SELECT 
 '{{ Title }}',
 '{{ Description }}',
 '{{ InstanceArn }}',
 '{{ Items }}',
 '{{ ScoringStrategy }}',
 '{{ Status }}',
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
  - name: evaluation_form
    props:
      - name: Title
        value: '{{ Title }}'
      - name: Description
        value: '{{ Description }}'
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Items
        value:
          - Section:
              Title: '{{ Title }}'
              Instructions: '{{ Instructions }}'
              RefId: '{{ RefId }}'
              Items:
                - Section: null
                  Question:
                    Title: '{{ Title }}'
                    Instructions: '{{ Instructions }}'
                    RefId: null
                    NotApplicableEnabled: '{{ NotApplicableEnabled }}'
                    QuestionType: '{{ QuestionType }}'
                    QuestionTypeProperties:
                      Numeric:
                        MinValue: '{{ MinValue }}'
                        MaxValue: '{{ MaxValue }}'
                        Options:
                          - MinValue: '{{ MinValue }}'
                            MaxValue: '{{ MaxValue }}'
                            Score: '{{ Score }}'
                            AutomaticFail: '{{ AutomaticFail }}'
                        Automation:
                          PropertyValue:
                            Label: '{{ Label }}'
                      SingleSelect:
                        Options:
                          - RefId: null
                            Text: '{{ Text }}'
                            Score: null
                            AutomaticFail: '{{ AutomaticFail }}'
                        DisplayAs: '{{ DisplayAs }}'
                        Automation:
                          Options:
                            - RuleCategory:
                                Category: '{{ Category }}'
                                Condition: '{{ Condition }}'
                                OptionRefId: null
                          DefaultOptionRefId: null
                    Weight: null
              Weight: null
      - name: ScoringStrategy
        value:
          Mode: '{{ Mode }}'
          Status: '{{ Status }}'
      - name: Status
        value: '{{ Status }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.connect.evaluation_forms
WHERE data__Identifier = '<EvaluationFormArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>evaluation_forms</code> resource, the following permissions are required:

### Create
```json
connect:CreateEvaluationForm,
connect:ActivateEvaluationForm,
connect:TagResource
```

### List
```json
connect:ListEvaluationForms
```

### Delete
```json
connect:DeleteEvaluationForm,
connect:UntagResource
```


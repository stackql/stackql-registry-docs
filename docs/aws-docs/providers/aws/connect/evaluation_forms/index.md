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

Creates, updates, deletes or gets an <code>evaluation_form</code> resource or lists <code>evaluation_forms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>evaluation_forms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::EvaluationForm</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.evaluation_forms" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="title" /></td><td><code>string</code></td><td>The title of the evaluation form.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the evaluation form.</td></tr>
<tr><td><CopyableCode code="evaluation_form_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the evaluation form.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr>
<tr><td><CopyableCode code="items" /></td><td><code>array</code></td><td>The list of evaluation form items.</td></tr>
<tr><td><CopyableCode code="scoring_strategy" /></td><td><code>object</code></td><td>The scoring strategy.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the evaluation form.</td></tr>
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
    <td><CopyableCode code="Title, InstanceArn, Items, Status, region" /></td>
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
Gets all <code>evaluation_forms</code> in a region.
```sql
SELECT
region,
title,
description,
evaluation_form_arn,
instance_arn,
items,
scoring_strategy,
status,
tags
FROM aws.connect.evaluation_forms
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>evaluation_form</code>.
```sql
SELECT
region,
title,
description,
evaluation_form_arn,
instance_arn,
items,
scoring_strategy,
status,
tags
FROM aws.connect.evaluation_forms
WHERE region = 'us-east-1' AND data__Identifier = '<EvaluationFormArn>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
connect:DescribeEvaluationForm,
connect:ListEvaluationFormVersions
```

### List
```json
connect:ListEvaluationForms
```

### Update
```json
connect:UpdateEvaluationForm,
connect:ListEvaluationFormVersions,
connect:ActivateEvaluationForm,
connect:DeactivateEvaluationForm,
connect:TagResource,
connect:UntagResource
```

### Delete
```json
connect:DeleteEvaluationForm,
connect:UntagResource
```


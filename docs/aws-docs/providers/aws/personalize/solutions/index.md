---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - personalize
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

Creates, updates, deletes or gets a <code>solution</code> resource or lists <code>solutions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Personalize::Solution.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.personalize.solutions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the solution</td></tr>
<tr><td><CopyableCode code="solution_arn" /></td><td><code>The ARN of the solution</code></td><td></td></tr>
<tr><td><CopyableCode code="event_type" /></td><td><code>string</code></td><td>When your have multiple event types (using an EVENT_TYPE schema field), this parameter specifies which event type (for example, 'click' or 'like') is used for training the model. If you do not provide an eventType, Amazon Personalize will use all interactions for training with equal weight regardless of type.</td></tr>
<tr><td><CopyableCode code="dataset_group_arn" /></td><td><code>string</code></td><td>The ARN of the dataset group that provides the training data.</td></tr>
<tr><td><CopyableCode code="perform_auto_ml" /></td><td><code>boolean</code></td><td>Whether to perform automated machine learning (AutoML). The default is false. For this case, you must specify recipeArn.</td></tr>
<tr><td><CopyableCode code="perform_hpo" /></td><td><code>boolean</code></td><td>Whether to perform hyperparameter optimization (HPO) on the specified or selected recipe. The default is false. When performing AutoML, this parameter is always true and you should not set it to false.</td></tr>
<tr><td><CopyableCode code="recipe_arn" /></td><td><code>string</code></td><td>The ARN of the recipe to use for model training. Only specified when performAutoML is false.</td></tr>
<tr><td><CopyableCode code="solution_config" /></td><td><code>The configuration to use with the solution. When performAutoML is set to true, Amazon Personalize only evaluates the autoMLConfig section of the solution configuration.</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, DatasetGroupArn, region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>solutions</code> in a region.
```sql
SELECT
region,
solution_arn
FROM aws.personalize.solutions
WHERE region = 'us-east-1';
```
Gets all properties from a <code>solution</code>.
```sql
SELECT
region,
name,
solution_arn,
event_type,
dataset_group_arn,
perform_auto_ml,
perform_hpo,
recipe_arn,
solution_config
FROM aws.personalize.solutions
WHERE region = 'us-east-1' AND data__Identifier = '<SolutionArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>solution</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.personalize.solutions (
 Name,
 DatasetGroupArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ DatasetGroupArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.personalize.solutions (
 Name,
 EventType,
 DatasetGroupArn,
 PerformAutoML,
 PerformHPO,
 RecipeArn,
 SolutionConfig,
 region
)
SELECT 
 '{{ Name }}',
 '{{ EventType }}',
 '{{ DatasetGroupArn }}',
 '{{ PerformAutoML }}',
 '{{ PerformHPO }}',
 '{{ RecipeArn }}',
 '{{ SolutionConfig }}',
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
  - name: solution
    props:
      - name: Name
        value: '{{ Name }}'
      - name: EventType
        value: '{{ EventType }}'
      - name: DatasetGroupArn
        value: '{{ DatasetGroupArn }}'
      - name: PerformAutoML
        value: '{{ PerformAutoML }}'
      - name: PerformHPO
        value: '{{ PerformHPO }}'
      - name: RecipeArn
        value: '{{ RecipeArn }}'
      - name: SolutionConfig
        value:
          AlgorithmHyperParameters: {}
          AutoMLConfig:
            MetricName: '{{ MetricName }}'
            RecipeList:
              - '{{ RecipeList[0] }}'
          EventValueThreshold: '{{ EventValueThreshold }}'
          FeatureTransformationParameters: {}
          HpoConfig:
            AlgorithmHyperParameterRanges:
              CategoricalHyperParameterRanges:
                - Name: '{{ Name }}'
                  Values:
                    - '{{ Values[0] }}'
              ContinuousHyperParameterRanges:
                - Name: '{{ Name }}'
                  MinValue: null
                  MaxValue: null
              IntegerHyperParameterRanges:
                - Name: '{{ Name }}'
                  MinValue: '{{ MinValue }}'
                  MaxValue: '{{ MaxValue }}'
            HpoObjective:
              MetricName: '{{ MetricName }}'
              Type: '{{ Type }}'
              MetricRegex: '{{ MetricRegex }}'
            HpoResourceConfig:
              MaxNumberOfTrainingJobs: '{{ MaxNumberOfTrainingJobs }}'
              MaxParallelTrainingJobs: '{{ MaxParallelTrainingJobs }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.personalize.solutions
WHERE data__Identifier = '<SolutionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>solutions</code> resource, the following permissions are required:

### Create
```json
personalize:CreateSolution,
personalize:DescribeSolution
```

### Read
```json
personalize:DescribeSolution
```

### Delete
```json
personalize:DeleteSolution,
personalize:DescribeSolution
```

### List
```json
personalize:ListSolutions
```


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


Used to retrieve a list of <code>solutions</code> in a region or to create or delete a <code>solutions</code> resource, use <code>solution</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Personalize::Solution.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.personalize.solutions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="solution_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
solution_arn
FROM aws.personalize.solutions
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

### Delete
```json
personalize:DeleteSolution,
personalize:DescribeSolution
```

### List
```json
personalize:ListSolutions
```


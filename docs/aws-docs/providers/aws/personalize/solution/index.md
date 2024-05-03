---
title: solution
hide_title: false
hide_table_of_contents: false
keywords:
  - solution
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

Gets or operates on an individual <code>solution</code> resource, use <code>solutions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Personalize::Solution.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.personalize.solution" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the solution</td></tr>
<tr><td><CopyableCode code="solution_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="event_type" /></td><td><code>string</code></td><td>When your have multiple event types (using an EVENT_TYPE schema field), this parameter specifies which event type (for example, 'click' or 'like') is used for training the model. If you do not provide an eventType, Amazon Personalize will use all interactions for training with equal weight regardless of type.</td></tr>
<tr><td><CopyableCode code="dataset_group_arn" /></td><td><code>string</code></td><td>The ARN of the dataset group that provides the training data.</td></tr>
<tr><td><CopyableCode code="perform_auto_ml" /></td><td><code>boolean</code></td><td>Whether to perform automated machine learning (AutoML). The default is false. For this case, you must specify recipeArn.</td></tr>
<tr><td><CopyableCode code="perform_hpo" /></td><td><code>boolean</code></td><td>Whether to perform hyperparameter optimization (HPO) on the specified or selected recipe. The default is false. When performing AutoML, this parameter is always true and you should not set it to false.</td></tr>
<tr><td><CopyableCode code="recipe_arn" /></td><td><code>string</code></td><td>The ARN of the recipe to use for model training. Only specified when performAutoML is false.</td></tr>
<tr><td><CopyableCode code="solution_config" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.personalize.solution
WHERE data__Identifier = '<SolutionArn>';
```

## Permissions

To operate on the <code>solution</code> resource, the following permissions are required:

### Read
```json
personalize:DescribeSolution
```

### Delete
```json
personalize:DeleteSolution,
personalize:DescribeSolution
```


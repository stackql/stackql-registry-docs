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
Gets an individual <code>solution</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>solution</td></tr>
<tr><td><b>Id</b></td><td><code>aws.personalize.solution</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name for the solution</td></tr>
<tr><td><code>solution_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>event_type</code></td><td><code>string</code></td><td>When your have multiple event types (using an EVENT_TYPE schema field), this parameter specifies which event type (for example, 'click' or 'like') is used for training the model. If you do not provide an eventType, Amazon Personalize will use all interactions for training with equal weight regardless of type.</td></tr>
<tr><td><code>dataset_group_arn</code></td><td><code>string</code></td><td>The ARN of the dataset group that provides the training data.</td></tr>
<tr><td><code>perform_auto_ml</code></td><td><code>boolean</code></td><td>Whether to perform automated machine learning (AutoML). The default is false. For this case, you must specify recipeArn.</td></tr>
<tr><td><code>perform_hp_o</code></td><td><code>boolean</code></td><td>Whether to perform hyperparameter optimization (HPO) on the specified or selected recipe. The default is false. When performing AutoML, this parameter is always true and you should not set it to false.</td></tr>
<tr><td><code>recipe_arn</code></td><td><code>string</code></td><td>The ARN of the recipe to use for model training. Only specified when performAutoML is false.</td></tr>
<tr><td><code>solution_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
solution_arn,
event_type,
dataset_group_arn,
perform_auto_ml,
perform_hp_o,
recipe_arn,
solution_config
FROM aws.personalize.solution
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;SolutionArn&gt;'
```

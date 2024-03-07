---
title: evaluation_form
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluation_form
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
Gets an individual <code>evaluation_form</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>evaluation_form</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>evaluation_form</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.evaluation_form</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>title</code></td><td><code>string</code></td><td>The title of the evaluation form.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the evaluation form.</td></tr>
<tr><td><code>evaluation_form_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the evaluation form.</td></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr>
<tr><td><code>items</code></td><td><code>array</code></td><td>The list of evaluation form items.</td></tr>
<tr><td><code>scoring_strategy</code></td><td><code>object</code></td><td>The scoring strategy.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the evaluation form.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>evaluation_form</code> resource, the following permissions are required:

### Read
<pre>
connect:DescribeEvaluationForm,
connect:ListEvaluationFormVersions</pre>

### Update
<pre>
connect:UpdateEvaluationForm,
connect:ListEvaluationFormVersions,
connect:ActivateEvaluationForm,
connect:DeactivateEvaluationForm,
connect:TagResource,
connect:UntagResource</pre>

### Delete
<pre>
connect:DeleteEvaluationForm,
connect:UntagResource</pre>


## Example
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
FROM awscc.connect.evaluation_form
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;EvaluationFormArn&gt;'
```

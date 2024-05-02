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
Gets or operates on an individual <code>evaluation_form</code> resource, use <code>evaluation_forms</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>evaluation_form</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::EvaluationForm</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.evaluation_form</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.connect.evaluation_form
WHERE data__Identifier = '<EvaluationFormArn>';
```

## Permissions

To operate on the <code>evaluation_form</code> resource, the following permissions are required:

### Read
```json
connect:DescribeEvaluationForm,
connect:ListEvaluationFormVersions
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


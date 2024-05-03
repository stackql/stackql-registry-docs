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

Used to retrieve a list of <code>evaluation_forms</code> in a region or create a <code>evaluation_forms</code> resource, use <code>evaluation_form</code> to operate on an individual resource.

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
WHERE region = 'us-east-1'
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


---
title: assessment_target
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_target
  - inspector
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>assessment_target</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessment_target</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>assessment_target</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.inspector.assessment_target</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>assessment_target_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_group_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
assessment_target_name,
resource_group_arn
FROM awscc.inspector.assessment_target
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>assessment_target</code> resource, the following permissions are required:

### Update
```json
inspector:DescribeAssessmentTargets,
inspector:UpdateAssessmentTarget
```

### Read
```json
inspector:DescribeAssessmentTargets
```

### Delete
```json
inspector:DeleteAssessmentTarget
```


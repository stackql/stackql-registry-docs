---
title: assessment_template
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_template
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
Gets an individual <code>assessment_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessment_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>assessment_template</td></tr>
<tr><td><b>Id</b></td><td><code>aws.inspector.assessment_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>assessment_target_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>duration_in_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>assessment_template_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rules_package_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>user_attributes_for_findings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
assessment_target_arn,
duration_in_seconds,
assessment_template_name,
rules_package_arns,
user_attributes_for_findings
FROM aws.inspector.assessment_template
WHERE region = 'us-east-1'
AND data__Identifier = '<Arn>'
```

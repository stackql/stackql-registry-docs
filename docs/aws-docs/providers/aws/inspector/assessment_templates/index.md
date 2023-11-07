---
title: assessment_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_templates
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
Retrieves a list of <code>assessment_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessment_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>assessment_templates</td></tr>
<tr><td><b>Id</b></td><td><code>aws.inspector.assessment_templates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AssessmentTargetArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DurationInSeconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>AssessmentTemplateName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RulesPackageArns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>UserAttributesForFindings</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.inspector.assessment_templates
WHERE region = 'us-east-1'
</pre>

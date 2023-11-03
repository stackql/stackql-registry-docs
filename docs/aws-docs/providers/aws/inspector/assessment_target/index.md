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
<tr><td><b>Id</b></td><td><code>aws.inspector.assessment_target</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AssessmentTargetName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResourceGroupArn</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.inspector.assessment_target
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
</pre>

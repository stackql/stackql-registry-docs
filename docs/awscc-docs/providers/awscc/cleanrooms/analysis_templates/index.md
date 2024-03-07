---
title: analysis_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - analysis_templates
  - cleanrooms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>analysis_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analysis_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>analysis_templates</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cleanrooms.analysis_templates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>analysis_template_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>membership_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>analysis_templates</code> resource, the following permissions are required:

### Create
<pre>
cleanrooms:CreateAnalysisTemplate,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetAnalysisTemplate,
cleanrooms:ListAnalysisTemplates</pre>

### List
<pre>
cleanrooms:ListAnalysisTemplates</pre>


## Example
```sql
SELECT
region,
analysis_template_identifier,
membership_identifier
FROM awscc.cleanrooms.analysis_templates
WHERE region = 'us-east-1'
```

---
title: analysis_template
hide_title: false
hide_table_of_contents: false
keywords:
  - analysis_template
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
Gets an individual <code>analysis_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analysis_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>analysis_template</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cleanrooms.analysis_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>collaboration_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>collaboration_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms analysis template.</td></tr>
<tr><td><code>analysis_parameters</code></td><td><code>array</code></td><td>The member who can query can provide this placeholder for a literal data value in an analysis template</td></tr>
<tr><td><code>analysis_template_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>membership_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>membership_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schema</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>format</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>analysis_template</code> resource, the following permissions are required:

### Read
```json
cleanrooms:GetAnalysisTemplate,
cleanrooms:ListTagsForResource
```

### Update
```json
cleanrooms:UpdateAnalysisTemplate,
cleanrooms:GetAnalysisTemplate,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:UntagResource
```

### Delete
```json
cleanrooms:DeleteAnalysisTemplate,
cleanrooms:GetAnalysisTemplate,
cleanrooms:ListAnalysisTemplates,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource
```


## Example
```sql
SELECT
region,
arn,
collaboration_arn,
collaboration_identifier,
tags,
analysis_parameters,
analysis_template_identifier,
description,
membership_arn,
membership_identifier,
name,
schema,
source,
format
FROM awscc.cleanrooms.analysis_template
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AnalysisTemplateIdentifier&gt;'
AND data__Identifier = '&lt;MembershipIdentifier&gt;'
```

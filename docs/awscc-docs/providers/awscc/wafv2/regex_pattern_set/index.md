---
title: regex_pattern_set
hide_title: false
hide_table_of_contents: false
keywords:
  - regex_pattern_set
  - wafv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>regex_pattern_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regex_pattern_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>regex_pattern_set</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.wafv2.regex_pattern_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>ARN of the WAF entity.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Description of the entity.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the RegexPatternSet.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id of the RegexPatternSet</td></tr>
<tr><td><code>regular_expression_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>scope</code></td><td><code>string</code></td><td>Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
description,
name,
id,
regular_expression_list,
scope,
tags
FROM awscc.wafv2.regex_pattern_set
WHERE data__Identifier = '<Name>|<Id>|<Scope>';
```

## Permissions

To operate on the <code>regex_pattern_set</code> resource, the following permissions are required:

### Delete
```json
wafv2:DeleteRegexPatternSet,
wafv2:GetRegexPatternSet
```

### Read
```json
wafv2:GetRegexPatternSet,
wafv2:ListTagsForResource
```

### Update
```json
wafv2:UpdateRegexPatternSet,
wafv2:GetRegexPatternSet,
wafv2:ListTagsForResource
```


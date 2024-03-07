---
title: regex_pattern_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - regex_pattern_sets
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
Retrieves a list of <code>regex_pattern_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>regex_pattern_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>regex_pattern_sets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.wafv2.regex_pattern_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the RegexPatternSet.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id of the RegexPatternSet</td></tr>
<tr><td><code>scope</code></td><td><code>string</code></td><td>Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>regex_pattern_sets</code> resource, the following permissions are required:

### Create
<pre>
wafv2:CreateRegexPatternSet,
wafv2:GetRegexPatternSet,
wafv2:ListTagsForResource</pre>

### List
<pre>
wafv2:listRegexPatternSets</pre>


## Example
```sql
SELECT
region,
name,
id,
scope
FROM awscc.wafv2.regex_pattern_sets

```

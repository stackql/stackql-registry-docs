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
null
<tr><td><b>Id</b></td><td><code>aws.wafv2.regex_pattern_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>ARN of the WAF entity.</td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>Description of the entity.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the RegexPatternSet.</td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td>Id of the RegexPatternSet</td></tr><tr><td><code>RegularExpressionList</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Scope</code></td><td><code>string</code></td><td>Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.wafv2.regex_pattern_sets
WHERE region = 'us-east-1'
</pre>

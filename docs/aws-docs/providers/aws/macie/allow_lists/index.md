---
title: allow_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - allow_lists
  - macie
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>allow_lists</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>allow_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>allow_lists</td></tr>
<tr><td><b>Id</b></td><td><code>aws.macie.allow_lists</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of AllowList.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Description of AllowList.</td></tr>
<tr><td><code>Criteria</code></td><td><code>undefined</code></td><td>AllowList criteria.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>AllowList ID.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>AllowList ARN.</td></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td>AllowList status.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.macie.allow_lists
WHERE region = 'us-east-1'
</pre>

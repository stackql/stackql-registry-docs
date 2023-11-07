---
title: findings_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - findings_filters
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
Retrieves a list of <code>findings_filters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>findings_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>findings_filters</td></tr>
<tr><td><b>Id</b></td><td><code>aws.macie.findings_filters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Findings filter name</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Findings filter description</td></tr>
<tr><td><code>FindingCriteria</code></td><td><code>undefined</code></td><td>Findings filter criteria.</td></tr>
<tr><td><code>Action</code></td><td><code>undefined</code></td><td>Findings filter action.</td></tr>
<tr><td><code>Position</code></td><td><code>integer</code></td><td>Findings filter position.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>Findings filter ID.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Findings filter ARN.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.macie.findings_filters
WHERE region = 'us-east-1'
</pre>

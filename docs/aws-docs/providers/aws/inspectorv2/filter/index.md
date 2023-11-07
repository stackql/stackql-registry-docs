---
title: filter
hide_title: false
hide_table_of_contents: false
keywords:
  - filter
  - inspectorv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>filter</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.inspectorv2.filter</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Findings filter name.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Findings filter description.</td></tr>
<tr><td><code>FilterCriteria</code></td><td><code>undefined</code></td><td>Findings filter criteria.</td></tr>
<tr><td><code>FilterAction</code></td><td><code>undefined</code></td><td>Findings filter action.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Findings filter ARN.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.inspectorv2.filter
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Arn&gt;'
</pre>

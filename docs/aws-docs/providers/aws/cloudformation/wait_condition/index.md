---
title: wait_condition
hide_title: false
hide_table_of_contents: false
keywords:
  - wait_condition
  - cloudformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>wait_condition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wait_condition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.cloudformation.wait_condition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Data</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Handle</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Timeout</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cloudformation.wait_condition
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>

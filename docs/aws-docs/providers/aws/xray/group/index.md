---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
  - xray
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.xray.group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FilterExpression</code></td><td><code>string</code></td><td>The filter expression defining criteria by which to group traces.</td></tr>
<tr><td><code>GroupName</code></td><td><code>string</code></td><td>The case-sensitive name of the new group. Names must be unique.</td></tr>
<tr><td><code>GroupARN</code></td><td><code>string</code></td><td>The ARN of the group that was generated on creation.</td></tr>
<tr><td><code>InsightsConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.xray.group
WHERE region = 'us-east-1' AND data__Identifier = '&lt;GroupARN&gt;'
</pre>

---
title: stream
hide_title: false
hide_table_of_contents: false
keywords:
  - stream
  - qldb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>stream</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.qldb.stream</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>LedgerName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StreamName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>InclusiveStartTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ExclusiveEndTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KinesisConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.qldb.stream
WHERE region = 'us-east-1' AND data__Identifier = '&lt;LedgerName&gt;' AND data__Identifier = '&lt;Id&gt;'
</pre>

---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
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
Retrieves a list of <code>streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>streams</td></tr>
<tr><td><b>Id</b></td><td><code>aws.qldb.streams</code></td></tr>
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
FROM aws.qldb.streams
WHERE region = 'us-east-1'
</pre>

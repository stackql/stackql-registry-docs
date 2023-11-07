---
title: stream_consumers
hide_title: false
hide_table_of_contents: false
keywords:
  - stream_consumers
  - kinesis
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>stream_consumers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_consumers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stream_consumers</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kinesis.stream_consumers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ConsumerCreationTimestamp</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ConsumerName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ConsumerARN</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ConsumerStatus</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StreamARN</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.kinesis.stream_consumers<br/>WHERE region = 'us-east-1'
</pre>

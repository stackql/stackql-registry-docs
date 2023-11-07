---
title: stream_consumer
hide_title: false
hide_table_of_contents: false
keywords:
  - stream_consumer
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
Gets an individual <code>stream_consumer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stream_consumer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stream_consumer</td></tr>
<tr><td><b>Id</b></td><td><code>aws.kinesis.stream_consumer</code></td></tr>
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
SELECT *<br/>FROM aws.kinesis.stream_consumer<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Id&gt;'
</pre>

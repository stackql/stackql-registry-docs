---
title: event_bus
hide_title: false
hide_table_of_contents: false
keywords:
  - event_bus
  - events
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>event_bus</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_bus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_bus</td></tr>
<tr><td><b>Id</b></td><td><code>aws.events.event_bus</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EventSourceName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.events.event_bus
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>

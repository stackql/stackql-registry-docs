---
title: api_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - api_destination
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
Gets an individual <code>api_destination</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.events.api_destination</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the apiDestination.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ConnectionArn</code></td><td><code>string</code></td><td>The arn of the connection.</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The arn of the api destination.</td></tr>
<tr><td><code>InvocationRateLimitPerSecond</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>InvocationEndpoint</code></td><td><code>string</code></td><td>Url endpoint to invoke.</td></tr>
<tr><td><code>HttpMethod</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.events.api_destination
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Name&gt;'
</pre>

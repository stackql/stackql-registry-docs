---
title: endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint
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
Gets an individual <code>endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.events.endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RoutingConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ReplicationConfig</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>EventBuses</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>EndpointId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EndpointUrl</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StateReason</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.events.endpoint<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Name&gt;'
</pre>

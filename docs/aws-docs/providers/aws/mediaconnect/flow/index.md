---
title: flow
hide_title: false
hide_table_of_contents: false
keywords:
  - flow
  - mediaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>flow</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flow</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediaconnect.flow</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FlowArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the flow.</td></tr>
<tr><td><code>AvailabilityZone</code></td><td><code>string</code></td><td>The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.</td></tr>
<tr><td><code>FlowAvailabilityZone</code></td><td><code>string</code></td><td>The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS.(ReadOnly)</td></tr>
<tr><td><code>Source</code></td><td><code>undefined</code></td><td>The source of the flow.</td></tr>
<tr><td><code>SourceFailoverConfig</code></td><td><code>undefined</code></td><td>The source failover config of the flow.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.mediaconnect.flow<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;FlowArn&gt;'
</pre>

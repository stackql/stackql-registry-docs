---
title: listener
hide_title: false
hide_table_of_contents: false
keywords:
  - listener
  - globalaccelerator
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>listener</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>listener</td></tr>
<tr><td><b>Id</b></td><td><code>aws.globalaccelerator.listener</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>listener_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the listener.</td></tr>
<tr><td><code>accelerator_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the accelerator.</td></tr>
<tr><td><code>port_ranges</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>protocol</code></td><td><code>string</code></td><td>The protocol for the listener.</td></tr>
<tr><td><code>client_affinity</code></td><td><code>string</code></td><td>Client affinity lets you direct all requests from a user to the same endpoint.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
listener_arn,
accelerator_arn,
port_ranges,
protocol,
client_affinity
FROM aws.globalaccelerator.listener
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ListenerArn&gt;'
```

---
title: game_session_queue
hide_title: false
hide_table_of_contents: false
keywords:
  - game_session_queue
  - gamelift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>game_session_queue</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>game_session_queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>game_session_queue</td></tr>
<tr><td><b>Id</b></td><td><code>aws.gamelift.game_session_queue</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>timeout_in_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>player_latency_policies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>destinations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>notification_target</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>filter_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_event_data</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>priority_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
timeout_in_seconds,
player_latency_policies,
destinations,
notification_target,
filter_configuration,
id,
arn,
custom_event_data,
tags,
name,
priority_configuration
FROM aws.gamelift.game_session_queue
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```

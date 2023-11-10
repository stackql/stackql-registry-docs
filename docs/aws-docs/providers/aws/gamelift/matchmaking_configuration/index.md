---
title: matchmaking_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - matchmaking_configuration
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
Gets an individual <code>matchmaking_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>matchmaking_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>matchmaking_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.gamelift.matchmaking_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>game_properties</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>game_session_data</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>acceptance_timeout_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>notification_target</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>custom_event_data</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>additional_player_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>backfill_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>request_timeout_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>acceptance_required</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>flex_match_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_set_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>game_session_queue_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
game_properties,
game_session_data,
description,
acceptance_timeout_seconds,
notification_target,
custom_event_data,
name,
additional_player_count,
backfill_mode,
request_timeout_seconds,
acceptance_required,
flex_match_mode,
id,
arn,
rule_set_name,
game_session_queue_arns,
tags
FROM aws.gamelift.matchmaking_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```

---
title: game_session_queue_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - game_session_queue_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>game_session_queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>game_session_queue_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::GameSessionQueue resource creates an Amazon GameLift (GameLift) game session queue.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.game_session_queue_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label that is associated with game session queue. Queue names must be unique within each Region.</td></tr>
<tr><td><CopyableCode code="timeout_in_seconds" /></td><td><code>integer</code></td><td>The maximum time, in seconds, that a new game session placement request remains in the queue.</td></tr>
<tr><td><CopyableCode code="destinations" /></td><td><code>array</code></td><td>A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue.</td></tr>
<tr><td><CopyableCode code="player_latency_policies" /></td><td><code>array</code></td><td>A set of policies that act as a sliding cap on player latency.</td></tr>
<tr><td><CopyableCode code="custom_event_data" /></td><td><code>string</code></td><td>Information that is added to all events that are related to this game session queue.</td></tr>
<tr><td><CopyableCode code="notification_target" /></td><td><code>string</code></td><td>An SNS topic ARN that is set up to receive game session placement notifications.</td></tr>
<tr><td><CopyableCode code="filter_configuration" /></td><td><code>object</code></td><td>A list of locations where a queue is allowed to place new game sessions.</td></tr>
<tr><td><CopyableCode code="priority_configuration" /></td><td><code>object</code></td><td>Custom settings to use when prioritizing destinations and locations for game session placements.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>game_session_queues</code> in a region.
```sql
SELECT
region,
name,
timeout_in_seconds,
destinations,
player_latency_policies,
custom_event_data,
notification_target,
filter_configuration,
priority_configuration,
arn,
tag_key,
tag_value
FROM aws.gamelift.game_session_queue_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>game_session_queue_tags</code> resource, see <a href="/providers/aws/gamelift/game_session_queues/#permissions"><code>game_session_queues</code></a>



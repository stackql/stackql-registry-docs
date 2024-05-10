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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>game_session_queue</code> resource, use <code>game_session_queues</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>game_session_queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::GameSessionQueue resource creates an Amazon GameLift (GameLift) game session queue.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.game_session_queue" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label that is associated with game session queue. Queue names must be unique within each Region.</td></tr>
<tr><td><CopyableCode code="timeout_in_seconds" /></td><td><code>integer</code></td><td>The maximum time, in seconds, that a new game session placement request remains in the queue.</td></tr>
<tr><td><CopyableCode code="destinations" /></td><td><code>array</code></td><td>A list of fleets and&#x2F;or fleet aliases that can be used to fulfill game session placement requests in the queue.</td></tr>
<tr><td><CopyableCode code="player_latency_policies" /></td><td><code>array</code></td><td>A set of policies that act as a sliding cap on player latency.</td></tr>
<tr><td><CopyableCode code="custom_event_data" /></td><td><code>string</code></td><td>Information that is added to all events that are related to this game session queue.</td></tr>
<tr><td><CopyableCode code="notification_target" /></td><td><code>string</code></td><td>An SNS topic ARN that is set up to receive game session placement notifications.</td></tr>
<tr><td><CopyableCode code="filter_configuration" /></td><td><code>object</code></td><td>A list of locations where a queue is allowed to place new game sessions.</td></tr>
<tr><td><CopyableCode code="priority_configuration" /></td><td><code>object</code></td><td>Custom settings to use when prioritizing destinations and locations for game session placements.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
tags
FROM aws.gamelift.game_session_queue
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>game_session_queue</code> resource, the following permissions are required:

### Read
```json
gamelift:DescribeGameSessionQueues,
gamelift:ListTagsForResource
```

### Update
```json
gamelift:UpdateGameSessionQueue,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:UntagResource
```


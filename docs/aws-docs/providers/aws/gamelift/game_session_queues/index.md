---
title: game_session_queues
hide_title: false
hide_table_of_contents: false
keywords:
  - game_session_queues
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


Used to retrieve a list of <code>game_session_queues</code> in a region or to create or delete a <code>game_session_queues</code> resource, use <code>game_session_queue</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>game_session_queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::GameSessionQueue resource creates an Amazon GameLift (GameLift) game session queue.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.game_session_queues" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label that is associated with game session queue. Queue names must be unique within each Region.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name
FROM aws.gamelift.game_session_queues
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.gamelift.game_session_queues (
 Name,
 region
)
SELECT 
{{ Name }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "TimeoutInSeconds": "{{ TimeoutInSeconds }}",
 "Destinations": [
  {
   "DestinationArn": "{{ DestinationArn }}"
  }
 ],
 "PlayerLatencyPolicies": [
  {
   "MaximumIndividualPlayerLatencyMilliseconds": "{{ MaximumIndividualPlayerLatencyMilliseconds }}",
   "PolicyDurationSeconds": "{{ PolicyDurationSeconds }}"
  }
 ],
 "CustomEventData": "{{ CustomEventData }}",
 "NotificationTarget": "{{ NotificationTarget }}",
 "FilterConfiguration": {
  "AllowedLocations": [
   "{{ AllowedLocations[0] }}"
  ]
 },
 "PriorityConfiguration": {
  "LocationOrder": [
   "{{ LocationOrder[0] }}"
  ],
  "PriorityOrder": [
   "{{ PriorityOrder[0] }}"
  ]
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.gamelift.game_session_queues (
 Name,
 TimeoutInSeconds,
 Destinations,
 PlayerLatencyPolicies,
 CustomEventData,
 NotificationTarget,
 FilterConfiguration,
 PriorityConfiguration,
 Tags,
 region
)
SELECT 
 {{ Name }},
 {{ TimeoutInSeconds }},
 {{ Destinations }},
 {{ PlayerLatencyPolicies }},
 {{ CustomEventData }},
 {{ NotificationTarget }},
 {{ FilterConfiguration }},
 {{ PriorityConfiguration }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.gamelift.game_session_queues
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>game_session_queues</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateGameSessionQueue,
gamelift:ListTagsForResource,
gamelift:TagResource
```

### Delete
```json
gamelift:DescribeGameSessionQueues,
gamelift:DeleteGameSessionQueue
```

### List
```json
gamelift:DescribeGameSessionQueues
```


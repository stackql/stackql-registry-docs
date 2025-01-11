---
title: matchmaking_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - matchmaking_configurations
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

Creates, updates, deletes or gets a <code>matchmaking_configuration</code> resource or lists <code>matchmaking_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>matchmaking_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::MatchmakingConfiguration resource creates an Amazon GameLift (GameLift) matchmaking configuration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.matchmaking_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="acceptance_required" /></td><td><code>boolean</code></td><td>A flag that indicates whether a match that was created with this configuration must be accepted by the matched players</td></tr>
<tr><td><CopyableCode code="acceptance_timeout_seconds" /></td><td><code>integer</code></td><td>The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.</td></tr>
<tr><td><CopyableCode code="additional_player_count" /></td><td><code>integer</code></td><td>The number of player slots in a match to keep open for future players.</td></tr>
<tr><td><CopyableCode code="backfill_mode" /></td><td><code>string</code></td><td>The method used to backfill game sessions created with this matchmaking configuration.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift matchmaking configuration resource and uniquely identifies it.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>A time stamp indicating when this data object was created.</td></tr>
<tr><td><CopyableCode code="custom_event_data" /></td><td><code>string</code></td><td>Information to attach to all events related to the matchmaking configuration.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A descriptive label that is associated with matchmaking configuration.</td></tr>
<tr><td><CopyableCode code="flex_match_mode" /></td><td><code>string</code></td><td>Indicates whether this matchmaking configuration is being used with Amazon GameLift hosting or as a standalone matchmaking solution.</td></tr>
<tr><td><CopyableCode code="game_properties" /></td><td><code>array</code></td><td>A set of custom properties for a game session, formatted as key:value pairs.</td></tr>
<tr><td><CopyableCode code="game_session_data" /></td><td><code>string</code></td><td>A set of custom game session properties, formatted as a single string value.</td></tr>
<tr><td><CopyableCode code="game_session_queue_arns" /></td><td><code>array</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A unique identifier for the matchmaking configuration.</td></tr>
<tr><td><CopyableCode code="notification_target" /></td><td><code>string</code></td><td>An SNS topic ARN that is set up to receive matchmaking notifications.</td></tr>
<tr><td><CopyableCode code="request_timeout_seconds" /></td><td><code>integer</code></td><td>The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out.</td></tr>
<tr><td><CopyableCode code="rule_set_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) associated with the GameLift matchmaking rule set resource that this configuration uses.</td></tr>
<tr><td><CopyableCode code="rule_set_name" /></td><td><code>string</code></td><td>A unique identifier for the matchmaking rule set to use with this configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html"><code>AWS::GameLift::MatchmakingConfiguration</code></a>.

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
    <td><CopyableCode code="AcceptanceRequired, Name, RequestTimeoutSeconds, RuleSetName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>matchmaking_configurations</code> in a region.
```sql
SELECT
region,
acceptance_required,
acceptance_timeout_seconds,
additional_player_count,
backfill_mode,
arn,
creation_time,
custom_event_data,
description,
flex_match_mode,
game_properties,
game_session_data,
game_session_queue_arns,
name,
notification_target,
request_timeout_seconds,
rule_set_arn,
rule_set_name,
tags
FROM aws.gamelift.matchmaking_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>matchmaking_configuration</code>.
```sql
SELECT
region,
acceptance_required,
acceptance_timeout_seconds,
additional_player_count,
backfill_mode,
arn,
creation_time,
custom_event_data,
description,
flex_match_mode,
game_properties,
game_session_data,
game_session_queue_arns,
name,
notification_target,
request_timeout_seconds,
rule_set_arn,
rule_set_name,
tags
FROM aws.gamelift.matchmaking_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>matchmaking_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.gamelift.matchmaking_configurations (
 AcceptanceRequired,
 Name,
 RequestTimeoutSeconds,
 RuleSetName,
 region
)
SELECT 
'{{ AcceptanceRequired }}',
 '{{ Name }}',
 '{{ RequestTimeoutSeconds }}',
 '{{ RuleSetName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.gamelift.matchmaking_configurations (
 AcceptanceRequired,
 AcceptanceTimeoutSeconds,
 AdditionalPlayerCount,
 BackfillMode,
 CreationTime,
 CustomEventData,
 Description,
 FlexMatchMode,
 GameProperties,
 GameSessionData,
 GameSessionQueueArns,
 Name,
 NotificationTarget,
 RequestTimeoutSeconds,
 RuleSetArn,
 RuleSetName,
 Tags,
 region
)
SELECT 
 '{{ AcceptanceRequired }}',
 '{{ AcceptanceTimeoutSeconds }}',
 '{{ AdditionalPlayerCount }}',
 '{{ BackfillMode }}',
 '{{ CreationTime }}',
 '{{ CustomEventData }}',
 '{{ Description }}',
 '{{ FlexMatchMode }}',
 '{{ GameProperties }}',
 '{{ GameSessionData }}',
 '{{ GameSessionQueueArns }}',
 '{{ Name }}',
 '{{ NotificationTarget }}',
 '{{ RequestTimeoutSeconds }}',
 '{{ RuleSetArn }}',
 '{{ RuleSetName }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: matchmaking_configuration
    props:
      - name: AcceptanceRequired
        value: '{{ AcceptanceRequired }}'
      - name: AcceptanceTimeoutSeconds
        value: '{{ AcceptanceTimeoutSeconds }}'
      - name: AdditionalPlayerCount
        value: '{{ AdditionalPlayerCount }}'
      - name: BackfillMode
        value: '{{ BackfillMode }}'
      - name: CreationTime
        value: '{{ CreationTime }}'
      - name: CustomEventData
        value: '{{ CustomEventData }}'
      - name: Description
        value: '{{ Description }}'
      - name: FlexMatchMode
        value: '{{ FlexMatchMode }}'
      - name: GameProperties
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: GameSessionData
        value: '{{ GameSessionData }}'
      - name: GameSessionQueueArns
        value:
          - '{{ GameSessionQueueArns[0] }}'
      - name: Name
        value: '{{ Name }}'
      - name: NotificationTarget
        value: '{{ NotificationTarget }}'
      - name: RequestTimeoutSeconds
        value: '{{ RequestTimeoutSeconds }}'
      - name: RuleSetArn
        value: '{{ RuleSetArn }}'
      - name: RuleSetName
        value: '{{ RuleSetName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.gamelift.matchmaking_configurations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>matchmaking_configurations</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateMatchmakingConfiguration,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:DescribeMatchmakingConfigurations
```

### Read
```json
gamelift:DescribeMatchmakingConfigurations,
gamelift:ListTagsForResource
```

### Delete
```json
gamelift:DescribeMatchmakingConfigurations,
gamelift:DeleteMatchmakingConfiguration
```

### List
```json
gamelift:DescribeMatchmakingConfigurations
```

### Update
```json
gamelift:DescribeMatchmakingConfigurations,
gamelift:UpdateMatchmakingConfiguration,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:UntagResource
```

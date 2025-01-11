---
title: routing_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_profiles
  - connect
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

Creates, updates, deletes or gets a <code>routing_profile</code> resource or lists <code>routing_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::RoutingProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.routing_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the routing profile.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the routing profile.</td></tr>
<tr><td><CopyableCode code="media_concurrencies" /></td><td><code>array</code></td><td>The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.</td></tr>
<tr><td><CopyableCode code="default_outbound_queue_arn" /></td><td><code>string</code></td><td>The identifier of the default outbound queue for this routing profile.</td></tr>
<tr><td><CopyableCode code="routing_profile_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the routing profile.</td></tr>
<tr><td><CopyableCode code="queue_configs" /></td><td><code>array</code></td><td>The queues to associate with this routing profile.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="agent_availability_timer" /></td><td><code>string</code></td><td>Whether agents with this routing profile will have their routing order calculated based on longest idle time or time since their last inbound contact.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html"><code>AWS::Connect::RoutingProfile</code></a>.

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
    <td><CopyableCode code="InstanceArn, Name, Description, MediaConcurrencies, DefaultOutboundQueueArn, region" /></td>
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
Gets all <code>routing_profiles</code> in a region.
```sql
SELECT
region,
instance_arn,
name,
description,
media_concurrencies,
default_outbound_queue_arn,
routing_profile_arn,
queue_configs,
tags,
agent_availability_timer
FROM aws.connect.routing_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>routing_profile</code>.
```sql
SELECT
region,
instance_arn,
name,
description,
media_concurrencies,
default_outbound_queue_arn,
routing_profile_arn,
queue_configs,
tags,
agent_availability_timer
FROM aws.connect.routing_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<RoutingProfileArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>routing_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.routing_profiles (
 InstanceArn,
 Name,
 Description,
 MediaConcurrencies,
 DefaultOutboundQueueArn,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ MediaConcurrencies }}',
 '{{ DefaultOutboundQueueArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.routing_profiles (
 InstanceArn,
 Name,
 Description,
 MediaConcurrencies,
 DefaultOutboundQueueArn,
 QueueConfigs,
 Tags,
 AgentAvailabilityTimer,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Name }}',
 '{{ Description }}',
 '{{ MediaConcurrencies }}',
 '{{ DefaultOutboundQueueArn }}',
 '{{ QueueConfigs }}',
 '{{ Tags }}',
 '{{ AgentAvailabilityTimer }}',
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
  - name: routing_profile
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: MediaConcurrencies
        value:
          - Channel: '{{ Channel }}'
            Concurrency: '{{ Concurrency }}'
            CrossChannelBehavior:
              BehaviorType: '{{ BehaviorType }}'
      - name: DefaultOutboundQueueArn
        value: '{{ DefaultOutboundQueueArn }}'
      - name: QueueConfigs
        value:
          - Delay: '{{ Delay }}'
            Priority: '{{ Priority }}'
            QueueReference:
              Channel: null
              QueueArn: '{{ QueueArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AgentAvailabilityTimer
        value: '{{ AgentAvailabilityTimer }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.routing_profiles
WHERE data__Identifier = '<RoutingProfileArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>routing_profiles</code> resource, the following permissions are required:

### Create
```json
connect:CreateRoutingProfile,
connect:TagResource
```

### Read
```json
connect:DescribeRoutingProfile,
connect:ListRoutingProfileQueues
```

### Delete
```json
connect:DeleteRoutingProfile,
connect:UntagResource
```

### Update
```json
connect:AssociateRoutingProfileQueues,
connect:DisassociateRoutingProfileQueues,
connect:UpdateRoutingProfileConcurrency,
connect:UpdateRoutingProfileName,
connect:UpdateRoutingProfileDefaultOutboundQueue,
connect:UpdateRoutingProfileQueues,
connect:TagResource,
connect:UntagResource,
connect:ListRoutingProfileQueues,
connect:UpdateRoutingProfileAgentAvailabilityTimer
```

### List
```json
connect:ListRoutingProfiles,
connect:ListRoutingProfileQueues
```

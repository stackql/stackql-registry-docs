---
title: routing_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_profile
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

Gets or operates on an individual <code>routing_profile</code> resource, use <code>routing_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::RoutingProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.routing_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
instance_arn,
name,
description,
media_concurrencies,
default_outbound_queue_arn,
routing_profile_arn,
queue_configs,
tags,
agent_availability_timer
FROM aws.connect.routing_profile
WHERE data__Identifier = '<RoutingProfileArn>';
```

## Permissions

To operate on the <code>routing_profile</code> resource, the following permissions are required:

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


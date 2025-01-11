---
title: routing_profile_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_profile_tags
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

Expands all tag keys and values for <code>routing_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_profile_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::RoutingProfile</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.routing_profile_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the routing profile.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the routing profile.</td></tr>
<tr><td><CopyableCode code="media_concurrencies" /></td><td><code>array</code></td><td>The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.</td></tr>
<tr><td><CopyableCode code="default_outbound_queue_arn" /></td><td><code>string</code></td><td>The identifier of the default outbound queue for this routing profile.</td></tr>
<tr><td><CopyableCode code="routing_profile_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the routing profile.</td></tr>
<tr><td><CopyableCode code="queue_configs" /></td><td><code>array</code></td><td>The queues to associate with this routing profile.</td></tr>
<tr><td><CopyableCode code="agent_availability_timer" /></td><td><code>string</code></td><td>Whether agents with this routing profile will have their routing order calculated based on longest idle time or time since their last inbound contact.</td></tr>
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
Expands tags for all <code>routing_profiles</code> in a region.
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
agent_availability_timer,
tag_key,
tag_value
FROM aws.connect.routing_profile_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>routing_profile_tags</code> resource, see <a href="/providers/aws/connect/routing_profiles/#permissions"><code>routing_profiles</code></a>


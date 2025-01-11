---
title: signal_map_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_map_tags
  - medialive
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

Expands all tag keys and values for <code>signal_maps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signal_map_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::SignalMap Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.signal_map_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>A signal map's ARN (Amazon Resource Name)</td></tr>
<tr><td><CopyableCode code="cloud_watch_alarm_template_group_identifiers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="cloud_watch_alarm_template_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A resource's optional description.</td></tr>
<tr><td><CopyableCode code="discovery_entry_point_arn" /></td><td><code>string</code></td><td>A top-level supported AWS resource ARN to discovery a signal map from.</td></tr>
<tr><td><CopyableCode code="error_message" /></td><td><code>string</code></td><td>Error message associated with a failed creation or failed update attempt of a signal map.</td></tr>
<tr><td><CopyableCode code="event_bridge_rule_template_group_identifiers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="event_bridge_rule_template_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="failed_media_resource_map" /></td><td><code>object</code></td><td>A map representing an incomplete AWS media workflow as a graph.</td></tr>
<tr><td><CopyableCode code="force_rediscovery" /></td><td><code>boolean</code></td><td>If true, will force a rediscovery of a signal map if an unchanged discoveryEntryPointArn is provided.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>A signal map's id.</td></tr>
<tr><td><CopyableCode code="identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_discovered_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_successful_monitor_deployment" /></td><td><code>object</code></td><td>Represents the latest successful monitor deployment of a signal map.</td></tr>
<tr><td><CopyableCode code="media_resource_map" /></td><td><code>object</code></td><td>A map representing an AWS media workflow as a graph.</td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="monitor_changes_pending_deployment" /></td><td><code>boolean</code></td><td>If true, there are pending monitor changes for this signal map that can be deployed.</td></tr>
<tr><td><CopyableCode code="monitor_deployment" /></td><td><code>object</code></td><td>Represents the latest monitor deployment of a signal map.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A resource's name. Names must be unique within the scope of a resource type in a specific region.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>A signal map's current status which is dependent on its lifecycle actions or associated jobs.</td></tr>
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
Expands tags for all <code>signal_maps</code> in a region.
```sql
SELECT
region,
arn,
cloud_watch_alarm_template_group_identifiers,
cloud_watch_alarm_template_group_ids,
created_at,
description,
discovery_entry_point_arn,
error_message,
event_bridge_rule_template_group_identifiers,
event_bridge_rule_template_group_ids,
failed_media_resource_map,
force_rediscovery,
id,
identifier,
last_discovered_at,
last_successful_monitor_deployment,
media_resource_map,
modified_at,
monitor_changes_pending_deployment,
monitor_deployment,
name,
status,
tag_key,
tag_value
FROM aws.medialive.signal_map_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>signal_map_tags</code> resource, see <a href="/providers/aws/medialive/signal_maps/#permissions"><code>signal_maps</code></a>


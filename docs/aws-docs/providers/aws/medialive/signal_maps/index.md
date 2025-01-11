---
title: signal_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - signal_maps
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

Creates, updates, deletes or gets a <code>signal_map</code> resource or lists <code>signal_maps</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signal_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::SignalMap Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.signal_maps" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Represents the tags associated with a resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-signalmap.html"><code>AWS::MediaLive::SignalMap</code></a>.

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
    <td><CopyableCode code="DiscoveryEntryPointArn, Name, region" /></td>
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
Gets all <code>signal_maps</code> in a region.
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
tags
FROM aws.medialive.signal_maps
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>signal_map</code>.
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
tags
FROM aws.medialive.signal_maps
WHERE region = 'us-east-1' AND data__Identifier = '<Identifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>signal_map</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.medialive.signal_maps (
 DiscoveryEntryPointArn,
 Name,
 region
)
SELECT 
'{{ DiscoveryEntryPointArn }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.medialive.signal_maps (
 CloudWatchAlarmTemplateGroupIdentifiers,
 Description,
 DiscoveryEntryPointArn,
 EventBridgeRuleTemplateGroupIdentifiers,
 ForceRediscovery,
 Name,
 Tags,
 region
)
SELECT 
 '{{ CloudWatchAlarmTemplateGroupIdentifiers }}',
 '{{ Description }}',
 '{{ DiscoveryEntryPointArn }}',
 '{{ EventBridgeRuleTemplateGroupIdentifiers }}',
 '{{ ForceRediscovery }}',
 '{{ Name }}',
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
  - name: signal_map
    props:
      - name: CloudWatchAlarmTemplateGroupIdentifiers
        value:
          - '{{ CloudWatchAlarmTemplateGroupIdentifiers[0] }}'
      - name: Description
        value: '{{ Description }}'
      - name: DiscoveryEntryPointArn
        value: '{{ DiscoveryEntryPointArn }}'
      - name: EventBridgeRuleTemplateGroupIdentifiers
        value:
          - '{{ EventBridgeRuleTemplateGroupIdentifiers[0] }}'
      - name: ForceRediscovery
        value: '{{ ForceRediscovery }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.medialive.signal_maps
WHERE data__Identifier = '<Identifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>signal_maps</code> resource, the following permissions are required:

### Create
```json
medialive:CreateSignalMap,
medialive:GetSignalMap,
medialive:CreateTags,
medialive:DescribeChannel,
medialive:DescribeInput,
medialive:DescribeInputDevice,
medialive:DescribeInputSecurityGroup,
medialive:DescribeMultiplex,
medialive:DescribeMultiplexProgram,
medialive:ListChannels,
medialive:ListInputDevices,
medialive:ListInputSecurityGroups,
medialive:ListInputs,
medialive:ListMultiplexPrograms,
medialive:ListMultiplexes,
medialive:ListOfferings,
medialive:ListReservations,
medialive:ListTagsForResource,
cloudfront:ListDistributions,
cloudfront:GetDistribution,
ec2:DescribeNetworkInterfaces,
mediaconnect:ListEntitlements,
mediaconnect:ListFlows,
mediaconnect:ListOfferings,
mediaconnect:ListReservations,
mediaconnect:DescribeFlow,
mediapackage:ListChannels,
mediapackage:ListOriginEndpoints,
mediapackage:DescribeChannel,
mediapackage:DescribeOriginEndpoint,
mediapackagev2:ListChannelGroups,
mediapackagev2:ListChannels,
mediapackagev2:ListOriginEndpoints,
mediapackagev2:GetChannelGroup,
mediapackagev2:GetChannel,
mediapackagev2:GetOriginEndpoint,
tag:GetResources
```

### Read
```json
medialive:GetSignalMap,
tag:GetResources
```

### Update
```json
medialive:StartUpdateSignalMap,
medialive:GetSignalMap,
medialive:CreateTags,
medialive:DeleteTags,
medialive:DescribeChannel,
medialive:DescribeInput,
medialive:DescribeInputDevice,
medialive:DescribeInputSecurityGroup,
medialive:DescribeMultiplex,
medialive:DescribeMultiplexProgram,
medialive:ListChannels,
medialive:ListInputDevices,
medialive:ListInputSecurityGroups,
medialive:ListInputs,
medialive:ListMultiplexPrograms,
medialive:ListMultiplexes,
medialive:ListOfferings,
medialive:ListReservations,
medialive:ListTagsForResource,
cloudfront:ListDistributions,
cloudfront:GetDistribution,
ec2:DescribeNetworkInterfaces,
mediaconnect:ListEntitlements,
mediaconnect:ListFlows,
mediaconnect:ListOfferings,
mediaconnect:ListReservations,
mediaconnect:DescribeFlow,
mediapackage:ListChannels,
mediapackage:ListOriginEndpoints,
mediapackage:DescribeChannel,
mediapackage:DescribeOriginEndpoint,
mediapackagev2:ListChannelGroups,
mediapackagev2:ListChannels,
mediapackagev2:ListOriginEndpoints,
mediapackagev2:GetChannelGroup,
mediapackagev2:GetChannel,
mediapackagev2:GetOriginEndpoint,
tag:GetResources
```

### Delete
```json
medialive:GetSignalMap,
medialive:DeleteSignalMap
```

### List
```json
medialive:ListSignalMaps
```

---
title: channel_placement_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_placement_groups
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

Creates, updates, deletes or gets a <code>channel_placement_group</code> resource or lists <code>channel_placement_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_placement_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::ChannelPlacementGroup Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.channel_placement_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the channel placement group.</td></tr>
<tr><td><CopyableCode code="channels" /></td><td><code>array</code></td><td>List of channel IDs added to the channel placement group.</td></tr>
<tr><td><CopyableCode code="cluster_id" /></td><td><code>string</code></td><td>The ID of the cluster the node is on.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique internal identifier.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the channel placement group.</td></tr>
<tr><td><CopyableCode code="nodes" /></td><td><code>array</code></td><td>List of nodes added to the channel placement group</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The current state of the ChannelPlacementGroupState</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of key-value pairs.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channelplacementgroup.html"><code>AWS::MediaLive::ChannelPlacementGroup</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>channel_placement_groups</code> in a region.
```sql
SELECT
region,
arn,
channels,
cluster_id,
id,
name,
nodes,
state,
tags
FROM aws.medialive.channel_placement_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>channel_placement_group</code>.
```sql
SELECT
region,
arn,
channels,
cluster_id,
id,
name,
nodes,
state,
tags
FROM aws.medialive.channel_placement_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Id>|<ClusterId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channel_placement_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.medialive.channel_placement_groups (
 ClusterId,
 Name,
 Nodes,
 Tags,
 region
)
SELECT 
'{{ ClusterId }}',
 '{{ Name }}',
 '{{ Nodes }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.medialive.channel_placement_groups (
 ClusterId,
 Name,
 Nodes,
 Tags,
 region
)
SELECT 
 '{{ ClusterId }}',
 '{{ Name }}',
 '{{ Nodes }}',
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
  - name: channel_placement_group
    props:
      - name: ClusterId
        value: '{{ ClusterId }}'
      - name: Name
        value: '{{ Name }}'
      - name: Nodes
        value:
          - '{{ Nodes[0] }}'
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
DELETE FROM aws.medialive.channel_placement_groups
WHERE data__Identifier = '<Id|ClusterId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channel_placement_groups</code> resource, the following permissions are required:

### Create
```json
medialive:CreateChannelPlacementGroup,
medialive:DescribeChannelPlacementGroup,
medialive:CreateTags,
medialive:ListTagsForResource
```

### Read
```json
medialive:DescribeChannelPlacementGroup,
medialive:ListTagsForResource
```

### Update
```json
medialive:UpdateChannelPlacementGroup,
medialive:DescribeChannelPlacementGroup,
medialive:CreateTags,
medialive:DeleteTags,
medialive:ListTagsForResource
```

### Delete
```json
medialive:DeleteChannelPlacementGroup,
medialive:DescribeChannelPlacementGroup
```

### List
```json
medialive:ListChannelPlacementGroups
```

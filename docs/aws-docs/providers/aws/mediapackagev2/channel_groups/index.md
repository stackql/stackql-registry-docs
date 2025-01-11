---
title: channel_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_groups
  - mediapackagev2
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

Creates, updates, deletes or gets a <code>channel_group</code> resource or lists <code>channel_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td><p>Represents a channel group that facilitates the grouping of multiple channels.</p></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.channel_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) associated with the resource.</p></td></tr>
<tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td><p>The date and time the channel group was created.</p></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>Enter any descriptive text that helps you to identify the channel group.</p></td></tr>
<tr><td><CopyableCode code="egress_domain" /></td><td><code>string</code></td><td><p>The output domain where the source stream should be sent. Integrate the domain with a downstream CDN (such as Amazon CloudFront) or playback device.</p></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td><p>The date and time the channel group was modified.</p></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelgroup.html"><code>AWS::MediaPackageV2::ChannelGroup</code></a>.

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
    <td><CopyableCode code="ChannelGroupName, region" /></td>
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
Gets all <code>channel_groups</code> in a region.
```sql
SELECT
region,
arn,
channel_group_name,
created_at,
description,
egress_domain,
modified_at,
tags
FROM aws.mediapackagev2.channel_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>channel_group</code>.
```sql
SELECT
region,
arn,
channel_group_name,
created_at,
description,
egress_domain,
modified_at,
tags
FROM aws.mediapackagev2.channel_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channel_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediapackagev2.channel_groups (
 ChannelGroupName,
 region
)
SELECT 
'{{ ChannelGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediapackagev2.channel_groups (
 ChannelGroupName,
 Description,
 Tags,
 region
)
SELECT 
 '{{ ChannelGroupName }}',
 '{{ Description }}',
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
  - name: channel_group
    props:
      - name: ChannelGroupName
        value: '{{ ChannelGroupName }}'
      - name: Description
        value: '{{ Description }}'
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
DELETE FROM aws.mediapackagev2.channel_groups
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channel_groups</code> resource, the following permissions are required:

### Create
```json
mediapackagev2:TagResource,
mediapackagev2:CreateChannelGroup
```

### Read
```json
mediapackagev2:GetChannelGroup
```

### Update
```json
mediapackagev2:TagResource,
mediapackagev2:UntagResource,
mediapackagev2:ListTagsForResource,
mediapackagev2:UpdateChannelGroup
```

### Delete
```json
mediapackagev2:GetChannelGroup,
mediapackagev2:DeleteChannelGroup
```

### List
```json
mediapackagev2:ListChannelGroups
```

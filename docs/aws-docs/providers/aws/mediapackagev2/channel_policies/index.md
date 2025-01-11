---
title: channel_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_policies
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

Creates, updates, deletes or gets a <code>channel_policy</code> resource or lists <code>channel_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td><p>Represents a resource-based policy that allows or denies access to a channel.</p></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.channel_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackagev2-channelpolicy.html"><code>AWS::MediaPackageV2::ChannelPolicy</code></a>.

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
    <td><CopyableCode code="ChannelGroupName, ChannelName, Policy, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>channel_policy</code>.
```sql
SELECT
region,
channel_group_name,
channel_name,
policy
FROM aws.mediapackagev2.channel_policies
WHERE region = 'us-east-1' AND data__Identifier = '<ChannelGroupName>|<ChannelName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channel_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediapackagev2.channel_policies (
 ChannelGroupName,
 ChannelName,
 Policy,
 region
)
SELECT 
'{{ ChannelGroupName }}',
 '{{ ChannelName }}',
 '{{ Policy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediapackagev2.channel_policies (
 ChannelGroupName,
 ChannelName,
 Policy,
 region
)
SELECT 
 '{{ ChannelGroupName }}',
 '{{ ChannelName }}',
 '{{ Policy }}',
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
  - name: channel_policy
    props:
      - name: ChannelGroupName
        value: '{{ ChannelGroupName }}'
      - name: ChannelName
        value: '{{ ChannelName }}'
      - name: Policy
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediapackagev2.channel_policies
WHERE data__Identifier = '<ChannelGroupName|ChannelName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channel_policies</code> resource, the following permissions are required:

### Create
```json
mediapackagev2:GetChannelPolicy,
mediapackagev2:PutChannelPolicy
```

### Read
```json
mediapackagev2:GetChannelPolicy
```

### Update
```json
mediapackagev2:GetChannelPolicy,
mediapackagev2:PutChannelPolicy
```

### Delete
```json
mediapackagev2:GetChannelPolicy,
mediapackagev2:DeleteChannelPolicy
```

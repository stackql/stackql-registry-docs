---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - cloudtrail
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

Creates, updates, deletes or gets a <code>channel</code> resource or lists <code>channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A channel receives events from a specific source (such as an on-premises storage solution or application, or a partner event data source), and delivers the events to one or more event data stores. You use channels to ingest events into CloudTrail from sources outside AWS.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the channel.</td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>string</code></td><td>The ARN of an on-premises storage solution or application, or a partner event source.</td></tr>
<tr><td><CopyableCode code="destinations" /></td><td><code>array</code></td><td>One or more resources to which events arriving through a channel are logged and stored.</td></tr>
<tr><td><CopyableCode code="channel_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of a channel.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>channels</code> in a region.
```sql
SELECT
region,
name,
source,
destinations,
channel_arn,
tags
FROM aws.cloudtrail.channels
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>channel</code>.
```sql
SELECT
region,
name,
source,
destinations,
channel_arn,
tags
FROM aws.cloudtrail.channels
WHERE region = 'us-east-1' AND data__Identifier = '<ChannelArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channel</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudtrail.channels (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudtrail.channels (
 Name,
 Source,
 Destinations,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Source }}',
 '{{ Destinations }}',
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
  - name: channel
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Source
        value: '{{ Source }}'
      - name: Destinations
        value:
          - Type: '{{ Type }}'
            Location: '{{ Location }}'
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
DELETE FROM aws.cloudtrail.channels
WHERE data__Identifier = '<ChannelArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channels</code> resource, the following permissions are required:

### Create
```json
CloudTrail:CreateChannel,
CloudTrail:AddTags
```

### Read
```json
CloudTrail:GetChannel,
CloudTrail:ListChannels
```

### Update
```json
CloudTrail:UpdateChannel,
CloudTrail:GetChannel,
CloudTrail:AddTags,
CloudTrail:RemoveTags
```

### Delete
```json
CloudTrail:DeleteChannel
```

### List
```json
CloudTrail:ListChannels
```


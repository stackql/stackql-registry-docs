---
title: rooms
hide_title: false
hide_table_of_contents: false
keywords:
  - rooms
  - ivschat
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

Creates, updates, deletes or gets a <code>room</code> resource or lists <code>rooms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rooms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::IVSChat::Room.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivschat.rooms" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Room ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The system-generated ID of the room.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the room. The value does not need to be unique.</td></tr>
<tr><td><CopyableCode code="logging_configuration_identifiers" /></td><td><code>array</code></td><td>Array of logging configuration identifiers attached to the room.</td></tr>
<tr><td><CopyableCode code="maximum_message_length" /></td><td><code>integer</code></td><td>The maximum number of characters in a single message.</td></tr>
<tr><td><CopyableCode code="maximum_message_rate_per_second" /></td><td><code>integer</code></td><td>The maximum number of messages per second that can be sent to the room.</td></tr>
<tr><td><CopyableCode code="message_review_handler" /></td><td><code>object</code></td><td>Configuration information for optional review of messages.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html"><code>AWS::IVSChat::Room</code></a>.

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
Gets all <code>rooms</code> in a region.
```sql
SELECT
region,
arn,
id,
name,
logging_configuration_identifiers,
maximum_message_length,
maximum_message_rate_per_second,
message_review_handler,
tags
FROM aws.ivschat.rooms
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>room</code>.
```sql
SELECT
region,
arn,
id,
name,
logging_configuration_identifiers,
maximum_message_length,
maximum_message_rate_per_second,
message_review_handler,
tags
FROM aws.ivschat.rooms
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>room</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ivschat.rooms (
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
INSERT INTO aws.ivschat.rooms (
 Name,
 LoggingConfigurationIdentifiers,
 MaximumMessageLength,
 MaximumMessageRatePerSecond,
 MessageReviewHandler,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ LoggingConfigurationIdentifiers }}',
 '{{ MaximumMessageLength }}',
 '{{ MaximumMessageRatePerSecond }}',
 '{{ MessageReviewHandler }}',
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
  - name: room
    props:
      - name: Name
        value: '{{ Name }}'
      - name: LoggingConfigurationIdentifiers
        value:
          - '{{ LoggingConfigurationIdentifiers[0] }}'
      - name: MaximumMessageLength
        value: '{{ MaximumMessageLength }}'
      - name: MaximumMessageRatePerSecond
        value: '{{ MaximumMessageRatePerSecond }}'
      - name: MessageReviewHandler
        value:
          FallbackResult: '{{ FallbackResult }}'
          Uri: '{{ Uri }}'
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
DELETE FROM aws.ivschat.rooms
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rooms</code> resource, the following permissions are required:

### Create
```json
ivschat:CreateRoom,
ivschat:TagResource
```

### Read
```json
ivschat:GetRoom,
ivschat:ListTagsForResource
```

### Update
```json
ivschat:UpdateRoom,
ivschat:TagResource,
ivschat:UntagResource,
ivschat:ListTagsForResource
```

### Delete
```json
ivschat:DeleteRoom,
ivschat:UntagResource
```

### List
```json
ivschat:ListRooms,
ivschat:ListTagsForResource
```

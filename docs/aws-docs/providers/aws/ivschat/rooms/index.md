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


Used to retrieve a list of <code>rooms</code> in a region or to create or delete a <code>rooms</code> resource, use <code>room</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rooms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::IVSChat::Room.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivschat.rooms" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Room ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.ivschat.rooms
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{}
>>>
--required properties only
INSERT INTO aws.ivschat.rooms (
 ,
 region
)
SELECT 
{{  }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "LoggingConfigurationIdentifiers": [
  "{{ LoggingConfigurationIdentifiers[0] }}"
 ],
 "MaximumMessageLength": "{{ MaximumMessageLength }}",
 "MaximumMessageRatePerSecond": "{{ MaximumMessageRatePerSecond }}",
 "MessageReviewHandler": {
  "FallbackResult": "{{ FallbackResult }}",
  "Uri": "{{ Uri }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ Name }},
 {{ LoggingConfigurationIdentifiers }},
 {{ MaximumMessageLength }},
 {{ MaximumMessageRatePerSecond }},
 {{ MessageReviewHandler }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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


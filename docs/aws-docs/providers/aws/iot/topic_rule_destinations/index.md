---
title: topic_rule_destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_rule_destinations
  - iot
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


Used to retrieve a list of <code>topic_rule_destinations</code> in a region or to create or delete a <code>topic_rule_destinations</code> resource, use <code>topic_rule_destination</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_rule_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::TopicRuleDestination</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.topic_rule_destinations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN).</td></tr>
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
FROM aws.iot.topic_rule_destinations
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
{
 "Status": "{{ Status }}",
 "HttpUrlProperties": {
  "ConfirmationUrl": "{{ ConfirmationUrl }}"
 },
 "VpcProperties": {
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ],
  "SecurityGroups": [
   "{{ SecurityGroups[0] }}"
  ],
  "VpcId": "{{ VpcId }}",
  "RoleArn": "{{ RoleArn }}"
 }
}
>>>
--required properties only
INSERT INTO aws.iot.topic_rule_destinations (
 Status,
 HttpUrlProperties,
 VpcProperties,
 region
)
SELECT 
{{ Status }},
 {{ HttpUrlProperties }},
 {{ VpcProperties }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Status": "{{ Status }}",
 "HttpUrlProperties": {
  "ConfirmationUrl": "{{ ConfirmationUrl }}"
 },
 "VpcProperties": {
  "SubnetIds": [
   "{{ SubnetIds[0] }}"
  ],
  "SecurityGroups": [
   "{{ SecurityGroups[0] }}"
  ],
  "VpcId": "{{ VpcId }}",
  "RoleArn": "{{ RoleArn }}"
 }
}
>>>
--all properties
INSERT INTO aws.iot.topic_rule_destinations (
 Status,
 HttpUrlProperties,
 VpcProperties,
 region
)
SELECT 
 {{ Status }},
 {{ HttpUrlProperties }},
 {{ VpcProperties }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.topic_rule_destinations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>topic_rule_destinations</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
iot:CreateTopicRuleDestination,
iot:GetTopicRuleDestination,
iot:UpdateTopicRuleDestination
```

### Delete
```json
iot:GetTopicRuleDestination,
iot:DeleteTopicRuleDestination
```

### List
```json
iot:ListTopicRuleDestinations
```


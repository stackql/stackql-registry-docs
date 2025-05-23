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

Creates, updates, deletes or gets a <code>topic_rule_destination</code> resource or lists <code>topic_rule_destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_rule_destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::TopicRuleDestination</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.topic_rule_destinations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the TopicRuleDestination.</td></tr>
<tr><td><CopyableCode code="http_url_properties" /></td><td><code>object</code></td><td>HTTP URL destination properties.</td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td>The reasoning for the current status of the TopicRuleDestination.</td></tr>
<tr><td><CopyableCode code="vpc_properties" /></td><td><code>object</code></td><td>VPC destination properties.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicruledestination.html"><code>AWS::IoT::TopicRuleDestination</code></a>.

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
Gets all <code>topic_rule_destinations</code> in a region.
```sql
SELECT
region,
arn,
status,
http_url_properties,
status_reason,
vpc_properties
FROM aws.iot.topic_rule_destinations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>topic_rule_destination</code>.
```sql
SELECT
region,
arn,
status,
http_url_properties,
status_reason,
vpc_properties
FROM aws.iot.topic_rule_destinations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>topic_rule_destination</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.topic_rule_destinations (
 Status,
 HttpUrlProperties,
 VpcProperties,
 region
)
SELECT 
'{{ Status }}',
 '{{ HttpUrlProperties }}',
 '{{ VpcProperties }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.topic_rule_destinations (
 Status,
 HttpUrlProperties,
 VpcProperties,
 region
)
SELECT 
 '{{ Status }}',
 '{{ HttpUrlProperties }}',
 '{{ VpcProperties }}',
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
  - name: topic_rule_destination
    props:
      - name: Status
        value: '{{ Status }}'
      - name: HttpUrlProperties
        value:
          ConfirmationUrl: '{{ ConfirmationUrl }}'
      - name: VpcProperties
        value:
          SubnetIds:
            - '{{ SubnetIds[0] }}'
          SecurityGroups:
            - '{{ SecurityGroups[0] }}'
          VpcId: '{{ VpcId }}'
          RoleArn: '{{ RoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iot:GetTopicRuleDestination
```

### Update
```json
iam:PassRole,
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

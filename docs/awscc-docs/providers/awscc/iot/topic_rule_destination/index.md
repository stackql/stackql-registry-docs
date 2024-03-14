---
title: topic_rule_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_rule_destination
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
Gets an individual <code>topic_rule_destination</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_rule_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>topic_rule_destination</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.topic_rule_destination</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN).</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the TopicRuleDestination.</td></tr>
<tr><td><code>http_url_properties</code></td><td><code>object</code></td><td>HTTP URL destination properties.</td></tr>
<tr><td><code>status_reason</code></td><td><code>string</code></td><td>The reasoning for the current status of the TopicRuleDestination.</td></tr>
<tr><td><code>vpc_properties</code></td><td><code>object</code></td><td>VPC destination properties.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
status,
http_url_properties,
status_reason,
vpc_properties
FROM awscc.iot.topic_rule_destination
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>topic_rule_destination</code> resource, the following permissions are required:

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


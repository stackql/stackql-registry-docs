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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>topic_rule_destination</code> resource, use <code>topic_rule_destinations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_rule_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::TopicRuleDestination</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.topic_rule_destination" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the TopicRuleDestination.</td></tr>
<tr><td><CopyableCode code="http_url_properties" /></td><td><code>object</code></td><td>HTTP URL destination properties.</td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td>The reasoning for the current status of the TopicRuleDestination.</td></tr>
<tr><td><CopyableCode code="vpc_properties" /></td><td><code>object</code></td><td>VPC destination properties.</td></tr>
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

## `SELECT` Example
```sql
SELECT
region,
arn,
status,
http_url_properties,
status_reason,
vpc_properties
FROM aws.iot.topic_rule_destination
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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


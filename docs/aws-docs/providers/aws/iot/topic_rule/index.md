---
title: topic_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_rule
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
Gets an individual <code>topic_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::TopicRule</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.topic_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>topic_rule_payload</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
rule_name,
topic_rule_payload,
tags
FROM aws.iot.topic_rule
WHERE data__Identifier = '<RuleName>';
```

## Permissions

To operate on the <code>topic_rule</code> resource, the following permissions are required:

### Read
```json
iot:GetTopicRule,
iot:ListTagsForResource
```

### Update
```json
iam:PassRole,
iot:GetTopicRule,
iot:ListTagsForResource,
iot:ReplaceTopicRule,
iot:TagResource,
iot:UntagResource
```

### Delete
```json
iot:GetTopicRule,
iot:DeleteTopicRule
```


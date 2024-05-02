---
title: slack_channel_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - slack_channel_configurations
  - chatbot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>slack_channel_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slack_channel_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Chatbot::SlackChannelConfiguration.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.chatbot.slack_channel_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the configuration</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.chatbot.slack_channel_configurations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>slack_channel_configurations</code> resource, the following permissions are required:

### Create
```json
chatbot:CreateSlackChannelConfiguration,
iam:PassRole,
iam:CreateServiceLinkedRole
```

### List
```json
chatbot:DescribeSlackChannelConfigurations
```


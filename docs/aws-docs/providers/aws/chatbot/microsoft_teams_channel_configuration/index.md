---
title: microsoft_teams_channel_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - microsoft_teams_channel_configuration
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
Gets or operates on an individual <code>microsoft_teams_channel_configuration</code> resource, use <code>microsoft_teams_channel_configurations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>microsoft_teams_channel_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Chatbot::MicrosoftTeamsChannelConfiguration.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.chatbot.microsoft_teams_channel_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>team_id</code></td><td><code>string</code></td><td>The id of the Microsoft Teams team</td></tr>
<tr><td><code>teams_channel_id</code></td><td><code>string</code></td><td>The id of the Microsoft Teams channel</td></tr>
<tr><td><code>teams_tenant_id</code></td><td><code>string</code></td><td>The id of the Microsoft Teams tenant</td></tr>
<tr><td><code>configuration_name</code></td><td><code>string</code></td><td>The name of the configuration</td></tr>
<tr><td><code>iam_role_arn</code></td><td><code>string</code></td><td>The ARN of the IAM role that defines the permissions for AWS Chatbot</td></tr>
<tr><td><code>sns_topic_arns</code></td><td><code>array</code></td><td>ARNs of SNS topics which delivers notifications to AWS Chatbot, for example CloudWatch alarm notifications.</td></tr>
<tr><td><code>logging_level</code></td><td><code>string</code></td><td>Specifies the logging level for this configuration:ERROR,INFO or NONE. This property affects the log entries pushed to Amazon CloudWatch logs</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the configuration</td></tr>
<tr><td><code>guardrail_policies</code></td><td><code>array</code></td><td>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.</td></tr>
<tr><td><code>user_role_required</code></td><td><code>boolean</code></td><td>Enables use of a user role requirement in your chat configuration</td></tr>
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
team_id,
teams_channel_id,
teams_tenant_id,
configuration_name,
iam_role_arn,
sns_topic_arns,
logging_level,
arn,
guardrail_policies,
user_role_required
FROM aws.chatbot.microsoft_teams_channel_configuration
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>microsoft_teams_channel_configuration</code> resource, the following permissions are required:

### Read
```json
chatbot:GetMicrosoftTeamsChannelConfiguration
```

### Update
```json
chatbot:UpdateMicrosoftTeamsChannelConfiguration,
iam:PassRole
```

### Delete
```json
chatbot:GetMicrosoftTeamsChannelConfiguration,
chatbot:DeleteMicrosoftTeamsChannelConfiguration
```


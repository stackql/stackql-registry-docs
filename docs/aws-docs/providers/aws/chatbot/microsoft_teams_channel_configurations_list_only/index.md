---
title: microsoft_teams_channel_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - microsoft_teams_channel_configurations_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>microsoft_teams_channel_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/microsoft_teams_channel_configurations/"><code>microsoft_teams_channel_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>microsoft_teams_channel_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Chatbot::MicrosoftTeamsChannelConfiguration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.chatbot.microsoft_teams_channel_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="team_id" /></td><td><code>string</code></td><td>The id of the Microsoft Teams team</td></tr>
<tr><td><CopyableCode code="teams_channel_id" /></td><td><code>string</code></td><td>The id of the Microsoft Teams channel</td></tr>
<tr><td><CopyableCode code="teams_tenant_id" /></td><td><code>string</code></td><td>The id of the Microsoft Teams tenant</td></tr>
<tr><td><CopyableCode code="configuration_name" /></td><td><code>string</code></td><td>The name of the configuration</td></tr>
<tr><td><CopyableCode code="iam_role_arn" /></td><td><code>string</code></td><td>The ARN of the IAM role that defines the permissions for AWS Chatbot</td></tr>
<tr><td><CopyableCode code="sns_topic_arns" /></td><td><code>array</code></td><td>ARNs of SNS topics which delivers notifications to AWS Chatbot, for example CloudWatch alarm notifications.</td></tr>
<tr><td><CopyableCode code="logging_level" /></td><td><code>string</code></td><td>Specifies the logging level for this configuration:ERROR,INFO or NONE. This property affects the log entries pushed to Amazon CloudWatch logs</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the configuration</td></tr>
<tr><td><CopyableCode code="guardrail_policies" /></td><td><code>array</code></td><td>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.</td></tr>
<tr><td><CopyableCode code="user_role_required" /></td><td><code>boolean</code></td><td>Enables use of a user role requirement in your chat configuration</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to add to the configuration</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>microsoft_teams_channel_configurations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.chatbot.microsoft_teams_channel_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>microsoft_teams_channel_configurations_list_only</code> resource, see <a href="/providers/aws/chatbot/microsoft_teams_channel_configurations/#permissions"><code>microsoft_teams_channel_configurations</code></a>



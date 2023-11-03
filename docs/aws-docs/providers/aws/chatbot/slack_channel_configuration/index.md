---
title: slack_channel_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - slack_channel_configuration
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
Gets an individual <code>slack_channel_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slack_channel_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.chatbot.slack_channel_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SlackWorkspaceId</code></td><td><code>string</code></td><td>The id of the Slack workspace</td></tr><tr><td><code>SlackChannelId</code></td><td><code>string</code></td><td>The id of the Slack channel</td></tr><tr><td><code>ConfigurationName</code></td><td><code>string</code></td><td>The name of the configuration</td></tr><tr><td><code>IamRoleArn</code></td><td><code>string</code></td><td>The ARN of the IAM role that defines the permissions for AWS Chatbot</td></tr><tr><td><code>SnsTopicArns</code></td><td><code>array</code></td><td>ARNs of SNS topics which delivers notifications to AWS Chatbot, for example CloudWatch alarm notifications.</td></tr><tr><td><code>LoggingLevel</code></td><td><code>string</code></td><td>Specifies the logging level for this configuration:ERROR,INFO or NONE. This property affects the log entries pushed to Amazon CloudWatch logs</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the configuration</td></tr><tr><td><code>GuardrailPolicies</code></td><td><code>array</code></td><td>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.</td></tr><tr><td><code>UserRoleRequired</code></td><td><code>boolean</code></td><td>Enables use of a user role requirement in your chat configuration</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.chatbot.slack_channel_configuration
WHERE region = 'us-east-1' AND data__Identifier = '{Arn}'
</pre>

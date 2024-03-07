---
title: slack_channel_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - slack_channel_configuration
  - supportapp
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
<tr><td><b>Description</b></td><td>slack_channel_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.supportapp.slack_channel_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>team_id</code></td><td><code>string</code></td><td>The team ID in Slack, which uniquely identifies a workspace.</td></tr>
<tr><td><code>channel_id</code></td><td><code>string</code></td><td>The channel ID in Slack, which identifies a channel within a workspace.</td></tr>
<tr><td><code>channel_name</code></td><td><code>string</code></td><td>The channel name in Slack.</td></tr>
<tr><td><code>notify_on_create_or_reopen_case</code></td><td><code>boolean</code></td><td>Whether to notify when a case is created or reopened.</td></tr>
<tr><td><code>notify_on_add_correspondence_to_case</code></td><td><code>boolean</code></td><td>Whether to notify when a correspondence is added to a case.</td></tr>
<tr><td><code>notify_on_resolve_case</code></td><td><code>boolean</code></td><td>Whether to notify when a case is resolved.</td></tr>
<tr><td><code>notify_on_case_severity</code></td><td><code>string</code></td><td>The severity level of a support case that a customer wants to get notified for.</td></tr>
<tr><td><code>channel_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that grants the AWS Support App access to perform operations for AWS services.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>slack_channel_configuration</code> resource, the following permissions are required:

### Read
<pre>
supportapp:ListSlackChannelConfigurations</pre>

### Update
<pre>
supportapp:UpdateSlackChannelConfiguration,
supportapp:ListSlackChannelConfigurations</pre>

### Delete
<pre>
supportapp:DeleteSlackChannelConfiguration,
supportapp:ListSlackChannelConfigurations</pre>


## Example
```sql
SELECT
region,
team_id,
channel_id,
channel_name,
notify_on_create_or_reopen_case,
notify_on_add_correspondence_to_case,
notify_on_resolve_case,
notify_on_case_severity,
channel_role_arn
FROM awscc.supportapp.slack_channel_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TeamId&gt;'
AND data__Identifier = '&lt;ChannelId&gt;'
```

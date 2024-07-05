---
title: slack_channel_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - slack_channel_configurations_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>slack_channel_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/slack_channel_configurations/"><code>slack_channel_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slack_channel_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An AWS Support App resource that creates, updates, lists and deletes Slack channel configurations.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.supportapp.slack_channel_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="team_id" /></td><td><code>string</code></td><td>The team ID in Slack, which uniquely identifies a workspace.</td></tr>
<tr><td><CopyableCode code="channel_id" /></td><td><code>string</code></td><td>The channel ID in Slack, which identifies a channel within a workspace.</td></tr>
<tr><td><CopyableCode code="channel_name" /></td><td><code>string</code></td><td>The channel name in Slack.</td></tr>
<tr><td><CopyableCode code="notify_on_create_or_reopen_case" /></td><td><code>boolean</code></td><td>Whether to notify when a case is created or reopened.</td></tr>
<tr><td><CopyableCode code="notify_on_add_correspondence_to_case" /></td><td><code>boolean</code></td><td>Whether to notify when a correspondence is added to a case.</td></tr>
<tr><td><CopyableCode code="notify_on_resolve_case" /></td><td><code>boolean</code></td><td>Whether to notify when a case is resolved.</td></tr>
<tr><td><CopyableCode code="notify_on_case_severity" /></td><td><code>string</code></td><td>The severity level of a support case that a customer wants to get notified for.</td></tr>
<tr><td><CopyableCode code="channel_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that grants the AWS Support App access to perform operations for AWS services.</td></tr>
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
Lists all <code>slack_channel_configurations</code> in a region.
```sql
SELECT
region,
team_id,
channel_id
FROM aws.supportapp.slack_channel_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>slack_channel_configurations_list_only</code> resource, see <a href="/providers/aws/supportapp/slack_channel_configurations/#permissions"><code>slack_channel_configurations</code></a>



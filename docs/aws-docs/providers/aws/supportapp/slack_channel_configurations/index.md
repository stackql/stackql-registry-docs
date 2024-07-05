---
title: slack_channel_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - slack_channel_configurations
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

Creates, updates, deletes or gets a <code>slack_channel_configuration</code> resource or lists <code>slack_channel_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slack_channel_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An AWS Support App resource that creates, updates, lists and deletes Slack channel configurations.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.supportapp.slack_channel_configurations" /></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="TeamId, ChannelId, NotifyOnCaseSeverity, ChannelRoleArn, region" /></td>
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
Gets all <code>slack_channel_configurations</code> in a region.
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
FROM aws.supportapp.slack_channel_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>slack_channel_configuration</code>.
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
FROM aws.supportapp.slack_channel_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<TeamId>|<ChannelId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>slack_channel_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.supportapp.slack_channel_configurations (
 TeamId,
 ChannelId,
 NotifyOnCaseSeverity,
 ChannelRoleArn,
 region
)
SELECT 
'{{ TeamId }}',
 '{{ ChannelId }}',
 '{{ NotifyOnCaseSeverity }}',
 '{{ ChannelRoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.supportapp.slack_channel_configurations (
 TeamId,
 ChannelId,
 ChannelName,
 NotifyOnCreateOrReopenCase,
 NotifyOnAddCorrespondenceToCase,
 NotifyOnResolveCase,
 NotifyOnCaseSeverity,
 ChannelRoleArn,
 region
)
SELECT 
 '{{ TeamId }}',
 '{{ ChannelId }}',
 '{{ ChannelName }}',
 '{{ NotifyOnCreateOrReopenCase }}',
 '{{ NotifyOnAddCorrespondenceToCase }}',
 '{{ NotifyOnResolveCase }}',
 '{{ NotifyOnCaseSeverity }}',
 '{{ ChannelRoleArn }}',
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
  - name: slack_channel_configuration
    props:
      - name: TeamId
        value: '{{ TeamId }}'
      - name: ChannelId
        value: '{{ ChannelId }}'
      - name: ChannelName
        value: '{{ ChannelName }}'
      - name: NotifyOnCreateOrReopenCase
        value: '{{ NotifyOnCreateOrReopenCase }}'
      - name: NotifyOnAddCorrespondenceToCase
        value: '{{ NotifyOnAddCorrespondenceToCase }}'
      - name: NotifyOnResolveCase
        value: '{{ NotifyOnResolveCase }}'
      - name: NotifyOnCaseSeverity
        value: '{{ NotifyOnCaseSeverity }}'
      - name: ChannelRoleArn
        value: '{{ ChannelRoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.supportapp.slack_channel_configurations
WHERE data__Identifier = '<TeamId|ChannelId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>slack_channel_configurations</code> resource, the following permissions are required:

### Create
```json
supportapp:CreateSlackChannelConfiguration,
supportapp:ListSlackChannelConfigurations
```

### Read
```json
supportapp:ListSlackChannelConfigurations
```

### Update
```json
supportapp:UpdateSlackChannelConfiguration,
supportapp:ListSlackChannelConfigurations
```

### Delete
```json
supportapp:DeleteSlackChannelConfiguration,
supportapp:ListSlackChannelConfigurations
```

### List
```json
supportapp:ListSlackChannelConfigurations
```


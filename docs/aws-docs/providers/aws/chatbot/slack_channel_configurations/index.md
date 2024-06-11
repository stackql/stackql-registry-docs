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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>slack_channel_configuration</code> resource or lists <code>slack_channel_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slack_channel_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Chatbot::SlackChannelConfiguration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.chatbot.slack_channel_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="slack_workspace_id" /></td><td><code>string</code></td><td>The id of the Slack workspace</td></tr>
<tr><td><CopyableCode code="slack_channel_id" /></td><td><code>string</code></td><td>The id of the Slack channel</td></tr>
<tr><td><CopyableCode code="configuration_name" /></td><td><code>string</code></td><td>The name of the configuration</td></tr>
<tr><td><CopyableCode code="iam_role_arn" /></td><td><code>string</code></td><td>The ARN of the IAM role that defines the permissions for AWS Chatbot</td></tr>
<tr><td><CopyableCode code="sns_topic_arns" /></td><td><code>array</code></td><td>ARNs of SNS topics which delivers notifications to AWS Chatbot, for example CloudWatch alarm notifications.</td></tr>
<tr><td><CopyableCode code="logging_level" /></td><td><code>string</code></td><td>Specifies the logging level for this configuration:ERROR,INFO or NONE. This property affects the log entries pushed to Amazon CloudWatch logs</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the configuration</td></tr>
<tr><td><CopyableCode code="guardrail_policies" /></td><td><code>array</code></td><td>The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to add to the configuration</td></tr>
<tr><td><CopyableCode code="user_role_required" /></td><td><code>boolean</code></td><td>Enables use of a user role requirement in your chat configuration</td></tr>
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
    <td><CopyableCode code="SlackWorkspaceId, SlackChannelId, ConfigurationName, IamRoleArn, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>slack_channel_configurations</code> in a region.
```sql
SELECT
region,
arn
FROM aws.chatbot.slack_channel_configurations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>slack_channel_configuration</code>.
```sql
SELECT
region,
slack_workspace_id,
slack_channel_id,
configuration_name,
iam_role_arn,
sns_topic_arns,
logging_level,
arn,
guardrail_policies,
tags,
user_role_required
FROM aws.chatbot.slack_channel_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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
INSERT INTO aws.chatbot.slack_channel_configurations (
 SlackWorkspaceId,
 SlackChannelId,
 ConfigurationName,
 IamRoleArn,
 region
)
SELECT 
'{{ SlackWorkspaceId }}',
 '{{ SlackChannelId }}',
 '{{ ConfigurationName }}',
 '{{ IamRoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.chatbot.slack_channel_configurations (
 SlackWorkspaceId,
 SlackChannelId,
 ConfigurationName,
 IamRoleArn,
 SnsTopicArns,
 LoggingLevel,
 GuardrailPolicies,
 Tags,
 UserRoleRequired,
 region
)
SELECT 
 '{{ SlackWorkspaceId }}',
 '{{ SlackChannelId }}',
 '{{ ConfigurationName }}',
 '{{ IamRoleArn }}',
 '{{ SnsTopicArns }}',
 '{{ LoggingLevel }}',
 '{{ GuardrailPolicies }}',
 '{{ Tags }}',
 '{{ UserRoleRequired }}',
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
      - name: SlackWorkspaceId
        value: '{{ SlackWorkspaceId }}'
      - name: SlackChannelId
        value: '{{ SlackChannelId }}'
      - name: ConfigurationName
        value: '{{ ConfigurationName }}'
      - name: IamRoleArn
        value: '{{ IamRoleArn }}'
      - name: SnsTopicArns
        value:
          - '{{ SnsTopicArns[0] }}'
      - name: LoggingLevel
        value: '{{ LoggingLevel }}'
      - name: GuardrailPolicies
        value:
          - '{{ GuardrailPolicies[0] }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: UserRoleRequired
        value: '{{ UserRoleRequired }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.chatbot.slack_channel_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>slack_channel_configurations</code> resource, the following permissions are required:

### Create
```json
chatbot:CreateSlackChannelConfiguration,
chatbot:TagResource,
iam:PassRole,
iam:CreateServiceLinkedRole
```

### Read
```json
chatbot:DescribeSlackChannelConfigurations
```

### Update
```json
chatbot:UpdateSlackChannelConfiguration,
chatbot:TagResource,
chatbot:UntagResource,
chatbot:ListTagsForResource,
iam:PassRole
```

### Delete
```json
chatbot:DeleteSlackChannelConfiguration
```

### List
```json
chatbot:DescribeSlackChannelConfigurations
```


---
title: microsoft_teams_channel_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - microsoft_teams_channel_configurations
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


Used to retrieve a list of <code>microsoft_teams_channel_configurations</code> in a region or to create or delete a <code>microsoft_teams_channel_configurations</code> resource, use <code>microsoft_teams_channel_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>microsoft_teams_channel_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Chatbot::MicrosoftTeamsChannelConfiguration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.chatbot.microsoft_teams_channel_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the configuration</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.chatbot.microsoft_teams_channel_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>microsoft_teams_channel_configuration</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- microsoft_teams_channel_configuration.iql (required properties only)
INSERT INTO aws.chatbot.microsoft_teams_channel_configurations (
 TeamId,
 TeamsChannelId,
 TeamsTenantId,
 ConfigurationName,
 IamRoleArn,
 region
)
SELECT 
'{{ TeamId }}',
 '{{ TeamsChannelId }}',
 '{{ TeamsTenantId }}',
 '{{ ConfigurationName }}',
 '{{ IamRoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- microsoft_teams_channel_configuration.iql (all properties)
INSERT INTO aws.chatbot.microsoft_teams_channel_configurations (
 TeamId,
 TeamsChannelId,
 TeamsTenantId,
 ConfigurationName,
 IamRoleArn,
 SnsTopicArns,
 LoggingLevel,
 GuardrailPolicies,
 UserRoleRequired,
 region
)
SELECT 
 '{{ TeamId }}',
 '{{ TeamsChannelId }}',
 '{{ TeamsTenantId }}',
 '{{ ConfigurationName }}',
 '{{ IamRoleArn }}',
 '{{ SnsTopicArns }}',
 '{{ LoggingLevel }}',
 '{{ GuardrailPolicies }}',
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
  - name: microsoft_teams_channel_configuration
    props:
      - name: TeamId
        value: '{{ TeamId }}'
      - name: TeamsChannelId
        value: '{{ TeamsChannelId }}'
      - name: TeamsTenantId
        value: '{{ TeamsTenantId }}'
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
      - name: UserRoleRequired
        value: '{{ UserRoleRequired }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.chatbot.microsoft_teams_channel_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>microsoft_teams_channel_configurations</code> resource, the following permissions are required:

### Create
```json
chatbot:CreateMicrosoftTeamsChannelConfiguration,
iam:PassRole,
iam:CreateServiceLinkedRole
```

### Delete
```json
chatbot:GetMicrosoftTeamsChannelConfiguration,
chatbot:DeleteMicrosoftTeamsChannelConfiguration
```

### List
```json
chatbot:ListMicrosoftTeamsChannelConfigurations
```


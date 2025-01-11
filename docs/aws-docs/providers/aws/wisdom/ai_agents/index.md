---
title: ai_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - ai_agents
  - wisdom
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

Creates, updates, deletes or gets an <code>ai_agent</code> resource or lists <code>ai_agents</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ai_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Wisdom::AIAgent Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.ai_agents" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="a_iagent_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="a_iagent_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assistant_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assistant_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_time_seconds" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-aiagent.html"><code>AWS::Wisdom::AIAgent</code></a>.

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
    <td><CopyableCode code="AssistantId, Configuration, Type, region" /></td>
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
Gets all <code>ai_agents</code> in a region.
```sql
SELECT
region,
a_iagent_id,
a_iagent_arn,
assistant_id,
assistant_arn,
configuration,
description,
name,
tags,
type,
modified_time_seconds
FROM aws.wisdom.ai_agents
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ai_agent</code>.
```sql
SELECT
region,
a_iagent_id,
a_iagent_arn,
assistant_id,
assistant_arn,
configuration,
description,
name,
tags,
type,
modified_time_seconds
FROM aws.wisdom.ai_agents
WHERE region = 'us-east-1' AND data__Identifier = '<AIAgentId>|<AssistantId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ai_agent</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.wisdom.ai_agents (
 AssistantId,
 Configuration,
 Type,
 region
)
SELECT 
'{{ AssistantId }}',
 '{{ Configuration }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wisdom.ai_agents (
 AssistantId,
 Configuration,
 Description,
 Name,
 Tags,
 Type,
 region
)
SELECT 
 '{{ AssistantId }}',
 '{{ Configuration }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ Tags }}',
 '{{ Type }}',
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
  - name: ai_agent
    props:
      - name: AssistantId
        value: '{{ AssistantId }}'
      - name: Configuration
        value: null
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value: {}
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.wisdom.ai_agents
WHERE data__Identifier = '<AIAgentId|AssistantId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ai_agents</code> resource, the following permissions are required:

### Create
```json
wisdom:CreateAIAgent,
wisdom:TagResource
```

### Read
```json
wisdom:GetAIAgent
```

### Update
```json
wisdom:UpdateAIAgent
```

### Delete
```json
wisdom:DeleteAIAgent
```

### List
```json
wisdom:ListAIAgents
```

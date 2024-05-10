---
title: agent_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_aliases
  - bedrock
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


Used to retrieve a list of <code>agent_aliases</code> in a region or to create or delete a <code>agent_aliases</code> resource, use <code>agent_alias</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::AgentAlias Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.agent_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="agent_id" /></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><CopyableCode code="agent_alias_id" /></td><td><code>string</code></td><td>Id for an Agent Alias generated at the server side.</td></tr>
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
agent_id,
agent_alias_id
FROM aws.bedrock.agent_aliases
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "AgentAliasName": "{{ AgentAliasName }}",
 "AgentId": "{{ AgentId }}"
}
>>>
--required properties only
INSERT INTO aws.bedrock.agent_aliases (
 AgentAliasName,
 AgentId,
 region
)
SELECT 
{{ AgentAliasName }},
 {{ AgentId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AgentAliasName": "{{ AgentAliasName }}",
 "AgentId": "{{ AgentId }}",
 "Description": "{{ Description }}",
 "RoutingConfiguration": [
  {
   "AgentVersion": "{{ AgentVersion }}"
  }
 ],
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.bedrock.agent_aliases (
 AgentAliasName,
 AgentId,
 Description,
 RoutingConfiguration,
 Tags,
 region
)
SELECT 
 {{ AgentAliasName }},
 {{ AgentId }},
 {{ Description }},
 {{ RoutingConfiguration }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.bedrock.agent_aliases
WHERE data__Identifier = '<AgentId|AgentAliasId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>agent_aliases</code> resource, the following permissions are required:

### Create
```json
bedrock:PrepareAgent,
bedrock:GetAgent,
bedrock:CreateAgentAlias,
bedrock:TagResource,
bedrock:GetAgentAlias,
bedrock:ListTagsForResource
```

### Delete
```json
bedrock:DeleteAgentAlias
```

### List
```json
bedrock:ListAgentAliases
```


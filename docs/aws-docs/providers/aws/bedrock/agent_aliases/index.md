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
Retrieves a list of <code>agent_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::AgentAlias Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.bedrock.agent_aliases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>agent_id</code></td><td><code>string</code></td><td>Identifier for a resource.</td></tr>
<tr><td><code>agent_alias_id</code></td><td><code>string</code></td><td>Id for an Agent Alias generated at the server side.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
agent_id,
agent_alias_id
FROM aws.bedrock.agent_aliases
WHERE region = 'us-east-1'
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

### List
```json
bedrock:ListAgentAliases
```


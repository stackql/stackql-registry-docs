---
title: agents
hide_title: false
hide_table_of_contents: false
keywords:
  - agents
  - datasync
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


Used to retrieve a list of <code>agents</code> in a region or to create or delete a <code>agents</code> resource, use <code>agent</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::Agent.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.agents" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="agent_arn" /></td><td><code>string</code></td><td>The DataSync Agent ARN.</td></tr>
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
agent_arn
FROM aws.datasync.agents
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>agent</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- agent.iql (required properties only)
INSERT INTO aws.datasync.agents (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- agent.iql (all properties)
INSERT INTO aws.datasync.agents (
 AgentName,
 ActivationKey,
 SecurityGroupArns,
 SubnetArns,
 VpcEndpointId,
 Tags,
 region
)
SELECT 
 '{{ AgentName }}',
 '{{ ActivationKey }}',
 '{{ SecurityGroupArns }}',
 '{{ SubnetArns }}',
 '{{ VpcEndpointId }}',
 '{{ Tags }}',
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
  - name: agent
    props:
      - name: AgentName
        value: '{{ AgentName }}'
      - name: ActivationKey
        value: '{{ ActivationKey }}'
      - name: SecurityGroupArns
        value:
          - '{{ SecurityGroupArns[0] }}'
      - name: SubnetArns
        value:
          - '{{ SubnetArns[0] }}'
      - name: VpcEndpointId
        value: '{{ VpcEndpointId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.datasync.agents
WHERE data__Identifier = '<AgentArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>agents</code> resource, the following permissions are required:

### Create
```json
datasync:CreateAgent,
datasync:TagResource,
datasync:DescribeAgent,
datasync:ListTagsForResource,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcEndpoints
```

### Delete
```json
datasync:DeleteAgent
```

### List
```json
datasync:ListAgents
```


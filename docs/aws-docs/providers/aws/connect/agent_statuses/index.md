---
title: agent_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_statuses
  - connect
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

Creates, updates, deletes or gets an <code>agent_status</code> resource or lists <code>agent_statuses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::AgentStatus</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.agent_statuses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="agent_status_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the agent status.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the status.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the status.</td></tr>
<tr><td><CopyableCode code="display_order" /></td><td><code>integer</code></td><td>The display order of the status.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the status.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of agent status.</td></tr>
<tr><td><CopyableCode code="reset_order_number" /></td><td><code>boolean</code></td><td>A number indicating the reset order of the agent status.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="last_modified_region" /></td><td><code>string</code></td><td>Last modified region.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>number</code></td><td>Last modified time.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-agentstatus.html"><code>AWS::Connect::AgentStatus</code></a>.

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
    <td><CopyableCode code="InstanceArn, Name, State, region" /></td>
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
Gets all <code>agent_statuses</code> in a region.
```sql
SELECT
region,
instance_arn,
agent_status_arn,
description,
name,
display_order,
state,
type,
reset_order_number,
tags,
last_modified_region,
last_modified_time
FROM aws.connect.agent_statuses
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>agent_status</code>.
```sql
SELECT
region,
instance_arn,
agent_status_arn,
description,
name,
display_order,
state,
type,
reset_order_number,
tags,
last_modified_region,
last_modified_time
FROM aws.connect.agent_statuses
WHERE region = 'us-east-1' AND data__Identifier = '<AgentStatusArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>agent_status</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.agent_statuses (
 InstanceArn,
 Name,
 State,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ Name }}',
 '{{ State }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.agent_statuses (
 InstanceArn,
 Description,
 Name,
 DisplayOrder,
 State,
 Type,
 ResetOrderNumber,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ DisplayOrder }}',
 '{{ State }}',
 '{{ Type }}',
 '{{ ResetOrderNumber }}',
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
  - name: agent_status
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: DisplayOrder
        value: '{{ DisplayOrder }}'
      - name: State
        value: '{{ State }}'
      - name: Type
        value: '{{ Type }}'
      - name: ResetOrderNumber
        value: '{{ ResetOrderNumber }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## Permissions

To operate on the <code>agent_statuses</code> resource, the following permissions are required:

### Create
```json
connect:CreateAgentStatus,
connect:TagResource,
connect:ListAgentStatuses
```

### Read
```json
connect:DescribeAgentStatus
```

### Update
```json
connect:UpdateAgentStatus,
connect:UntagResource,
connect:TagResource
```

### List
```json
connect:ListAgentStatuses
```

---
title: flow_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_aliases
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

Creates, updates, deletes or gets a <code>flow_alias</code> resource or lists <code>flow_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::FlowAlias Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.flow_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn of the Flow Alias</td></tr>
<tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>Arn representation of the Flow</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Resource.</td></tr>
<tr><td><CopyableCode code="flow_id" /></td><td><code>string</code></td><td>Identifier for a flow resource.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id for a Flow Alias generated at the server side.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name for a resource.</td></tr>
<tr><td><CopyableCode code="routing_configuration" /></td><td><code>array</code></td><td>Routing configuration for a Flow alias.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tag keys and values</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-flowalias.html"><code>AWS::Bedrock::FlowAlias</code></a>.

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
    <td><CopyableCode code="Name, FlowArn, RoutingConfiguration, region" /></td>
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
Gets all <code>flow_aliases</code> in a region.
```sql
SELECT
region,
arn,
flow_arn,
created_at,
description,
flow_id,
id,
name,
routing_configuration,
updated_at,
tags
FROM aws.bedrock.flow_aliases
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>flow_alias</code>.
```sql
SELECT
region,
arn,
flow_arn,
created_at,
description,
flow_id,
id,
name,
routing_configuration,
updated_at,
tags
FROM aws.bedrock.flow_aliases
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>|<FlowArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow_alias</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.bedrock.flow_aliases (
 FlowArn,
 Name,
 RoutingConfiguration,
 region
)
SELECT 
'{{ FlowArn }}',
 '{{ Name }}',
 '{{ RoutingConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.bedrock.flow_aliases (
 FlowArn,
 Description,
 Name,
 RoutingConfiguration,
 Tags,
 region
)
SELECT 
 '{{ FlowArn }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ RoutingConfiguration }}',
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
  - name: flow_alias
    props:
      - name: FlowArn
        value: '{{ FlowArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: RoutingConfiguration
        value:
          - FlowVersion: '{{ FlowVersion }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.bedrock.flow_aliases
WHERE data__Identifier = '<Arn|FlowArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flow_aliases</code> resource, the following permissions are required:

### Create
```json
bedrock:CreateFlowAlias,
bedrock:GetFlowAlias,
bedrock:TagResource,
bedrock:ListTagsForResource
```

### Read
```json
bedrock:GetFlowAlias,
bedrock:ListTagsForResource
```

### Update
```json
bedrock:UpdateFlowAlias,
bedrock:GetFlowAlias,
bedrock:TagResource,
bedrock:UntagResource,
bedrock:ListTagsForResource
```

### Delete
```json
bedrock:DeleteFlowAlias
```

### List
```json
bedrock:ListFlowAliases
```

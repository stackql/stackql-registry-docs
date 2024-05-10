---
title: graphs
hide_title: false
hide_table_of_contents: false
keywords:
  - graphs
  - neptunegraph
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


Used to retrieve a list of <code>graphs</code> in a region or to create or delete a <code>graphs</code> resource, use <code>graph</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graphs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NeptuneGraph::Graph resource creates an Amazon NeptuneGraph Graph.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.neptunegraph.graphs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="graph_id" /></td><td><code>string</code></td><td>The auto-generated id assigned by the service.</td></tr>
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
graph_id
FROM aws.neptunegraph.graphs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>graph</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- graph.iql (required properties only)
INSERT INTO aws.neptunegraph.graphs (
 ProvisionedMemory,
 region
)
SELECT 
'{{ ProvisionedMemory }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- graph.iql (all properties)
INSERT INTO aws.neptunegraph.graphs (
 DeletionProtection,
 GraphName,
 ProvisionedMemory,
 PublicConnectivity,
 ReplicaCount,
 Tags,
 VectorSearchConfiguration,
 region
)
SELECT 
 '{{ DeletionProtection }}',
 '{{ GraphName }}',
 '{{ ProvisionedMemory }}',
 '{{ PublicConnectivity }}',
 '{{ ReplicaCount }}',
 '{{ Tags }}',
 '{{ VectorSearchConfiguration }}',
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
  - name: graph
    props:
      - name: DeletionProtection
        value: '{{ DeletionProtection }}'
      - name: GraphName
        value: '{{ GraphName }}'
      - name: ProvisionedMemory
        value: '{{ ProvisionedMemory }}'
      - name: PublicConnectivity
        value: '{{ PublicConnectivity }}'
      - name: ReplicaCount
        value: '{{ ReplicaCount }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VectorSearchConfiguration
        value:
          VectorSearchDimension: '{{ VectorSearchDimension }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.neptunegraph.graphs
WHERE data__Identifier = '<GraphId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>graphs</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
neptune-graph:CreateGraph,
neptune-graph:GetGraph,
neptune-graph:ListTagsForResource,
neptune-graph:TagResource,
kms:DescribeKey,
kms:CreateGrant,
kms:Decrypt,
iam:CreateServiceLinkedRole
```

### Delete
```json
neptune-graph:DeleteGraph,
neptune-graph:GetGraph,
kms:DescribeKey,
kms:CreateGrant,
kms:Decrypt
```

### List
```json
neptune-graph:GetGraph,
neptune-graph:ListGraphs,
kms:DescribeKey,
kms:CreateGrant,
kms:Decrypt
```


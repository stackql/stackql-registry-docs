---
title: core_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - core_networks
  - networkmanager
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

Creates, updates, deletes or gets a <code>core_network</code> resource or lists <code>core_networks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>core_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::CoreNetwork Resource Type Definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.core_networks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network that your core network is a part of.</td></tr>
<tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>The Id of core network</td></tr>
<tr><td><CopyableCode code="core_network_arn" /></td><td><code>string</code></td><td>The ARN (Amazon resource name) of core network</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>Live policy document for the core network, you must provide PolicyDocument in Json Format</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of core network</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The creation time of core network</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of core network</td></tr>
<tr><td><CopyableCode code="segments" /></td><td><code>array</code></td><td>The segments within a core network.</td></tr>
<tr><td><CopyableCode code="network_function_groups" /></td><td><code>array</code></td><td>The network function groups within a core network.</td></tr>
<tr><td><CopyableCode code="edges" /></td><td><code>array</code></td><td>The edges within a core network.</td></tr>
<tr><td><CopyableCode code="owner_account" /></td><td><code>string</code></td><td>Owner of the core network</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the global network.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html"><code>AWS::NetworkManager::CoreNetwork</code></a>.

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
    <td><CopyableCode code="GlobalNetworkId, region" /></td>
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
Gets all <code>core_networks</code> in a region.
```sql
SELECT
region,
global_network_id,
core_network_id,
core_network_arn,
policy_document,
description,
created_at,
state,
segments,
network_function_groups,
edges,
owner_account,
tags
FROM aws.networkmanager.core_networks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>core_network</code>.
```sql
SELECT
region,
global_network_id,
core_network_id,
core_network_arn,
policy_document,
description,
created_at,
state,
segments,
network_function_groups,
edges,
owner_account,
tags
FROM aws.networkmanager.core_networks
WHERE region = 'us-east-1' AND data__Identifier = '<CoreNetworkId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>core_network</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.networkmanager.core_networks (
 GlobalNetworkId,
 region
)
SELECT 
'{{ GlobalNetworkId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.networkmanager.core_networks (
 GlobalNetworkId,
 PolicyDocument,
 Description,
 Tags,
 region
)
SELECT 
 '{{ GlobalNetworkId }}',
 '{{ PolicyDocument }}',
 '{{ Description }}',
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
  - name: core_network
    props:
      - name: GlobalNetworkId
        value: '{{ GlobalNetworkId }}'
      - name: PolicyDocument
        value: {}
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.networkmanager.core_networks
WHERE data__Identifier = '<CoreNetworkId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>core_networks</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateCoreNetwork,
networkmanager:GetCoreNetwork,
networkmanager:GetCoreNetworkPolicy,
networkmanager:TagResource,
ec2:DescribeRegions
```

### Read
```json
networkmanager:GetCoreNetwork,
networkmanager:GetCoreNetworkPolicy
```

### Update
```json
networkmanager:UpdateCoreNetwork,
networkmanager:GetCoreNetwork,
networkmanager:ListTagsForResource,
networkmanager:PutCoreNetworkPolicy,
networkmanager:GetCoreNetworkPolicy,
networkmanager:ExecuteCoreNetworkChangeSet,
networkmanager:TagResource,
networkmanager:UntagResource,
ec2:DescribeRegions
```

### Delete
```json
networkmanager:DeleteCoreNetwork,
networkmanager:UntagResource,
networkmanager:GetCoreNetwork,
networkmanager:GetCoreNetworkPolicy,
ec2:DescribeRegions
```

### List
```json
networkmanager:ListCoreNetworks
```

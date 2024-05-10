---
title: global_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - global_networks
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


Used to retrieve a list of <code>global_networks</code> in a region or to create or delete a <code>global_networks</code> resource, use <code>global_network</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::GlobalNetwork type specifies a global network of the user's account</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.global_networks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
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
id
FROM aws.networkmanager.global_networks
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>global_network</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- global_network.iql (required properties only)
INSERT INTO aws.networkmanager.global_networks (
 Description,
 Tags,
 CreatedAt,
 State,
 region
)
SELECT 
'{{ Description }}',
 '{{ Tags }}',
 '{{ CreatedAt }}',
 '{{ State }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- global_network.iql (all properties)
INSERT INTO aws.networkmanager.global_networks (
 Description,
 Tags,
 CreatedAt,
 State,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Tags }}',
 '{{ CreatedAt }}',
 '{{ State }}',
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
  - name: global_network
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: CreatedAt
        value: '{{ CreatedAt }}'
      - name: State
        value: '{{ State }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.networkmanager.global_networks
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>global_networks</code> resource, the following permissions are required:

### Create
```json
networkmanager:CreateGlobalNetwork,
networkmanager:DescribeGlobalNetworks,
networkmanager:TagResource,
iam:CreateServiceLinkedRole
```

### Delete
```json
networkmanager:DeleteGlobalNetwork,
networkmanager:DescribeGlobalNetworks
```

### List
```json
networkmanager:DescribeGlobalNetworks
```


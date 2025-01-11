---
title: networks
hide_title: false
hide_table_of_contents: false
keywords:
  - networks
  - medialive
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

Creates, updates, deletes or gets a <code>network</code> resource or lists <code>networks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaLive::Network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.networks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Network.</td></tr>
<tr><td><CopyableCode code="associated_cluster_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique ID of the Network.</td></tr>
<tr><td><CopyableCode code="ip_pools" /></td><td><code>array</code></td><td>The list of IP address cidr pools for the network</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The user-specified name of the Network to be created.</td></tr>
<tr><td><CopyableCode code="routes" /></td><td><code>array</code></td><td>The routes for the network</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The current state of the Network.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of key-value pairs.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-network.html"><code>AWS::MediaLive::Network</code></a>.

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
    <td><CopyableCode code="Name, IpPools, region" /></td>
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
Gets all <code>networks</code> in a region.
```sql
SELECT
region,
arn,
associated_cluster_ids,
id,
ip_pools,
name,
routes,
state,
tags
FROM aws.medialive.networks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>network</code>.
```sql
SELECT
region,
arn,
associated_cluster_ids,
id,
ip_pools,
name,
routes,
state,
tags
FROM aws.medialive.networks
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.medialive.networks (
 IpPools,
 Name,
 region
)
SELECT 
'{{ IpPools }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.medialive.networks (
 IpPools,
 Name,
 Routes,
 Tags,
 region
)
SELECT 
 '{{ IpPools }}',
 '{{ Name }}',
 '{{ Routes }}',
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
  - name: network
    props:
      - name: IpPools
        value:
          - Cidr: '{{ Cidr }}'
      - name: Name
        value: '{{ Name }}'
      - name: Routes
        value:
          - Cidr: '{{ Cidr }}'
            Gateway: '{{ Gateway }}'
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
DELETE FROM aws.medialive.networks
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>networks</code> resource, the following permissions are required:

### Create
```json
medialive:CreateNetwork,
medialive:CreateTags,
medialive:DescribeNetwork,
medialive:ListTagsForResource
```

### Read
```json
medialive:DescribeNetwork,
medialive:ListTagsForResource
```

### Update
```json
medialive:UpdateNetwork,
medialive:CreateTags,
medialive:DeleteTags,
medialive:DescribeNetwork,
medialive:ListTagsForResource
```

### Delete
```json
medialive:DeleteNetwork,
medialive:DescribeNetwork
```

### List
```json
medialive:ListNetworks
```

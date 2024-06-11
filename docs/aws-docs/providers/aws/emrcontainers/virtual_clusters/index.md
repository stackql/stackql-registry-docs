---
title: virtual_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_clusters
  - emrcontainers
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

Creates, updates, deletes or gets a <code>virtual_cluster</code> resource or lists <code>virtual_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EMRContainers::VirtualCluster Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emrcontainers.virtual_clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="container_provider" /></td><td><code>object</code></td><td>Container provider of the virtual cluster.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the virtual cluster.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the virtual cluster.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this virtual cluster.</td></tr>
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
    <td><CopyableCode code="Name, ContainerProvider, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>virtual_clusters</code> in a region.
```sql
SELECT
region,
id
FROM aws.emrcontainers.virtual_clusters
WHERE region = 'us-east-1';
```
Gets all properties from a <code>virtual_cluster</code>.
```sql
SELECT
region,
arn,
container_provider,
id,
name,
tags
FROM aws.emrcontainers.virtual_clusters
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.emrcontainers.virtual_clusters (
 ContainerProvider,
 Name,
 region
)
SELECT 
'{{ ContainerProvider }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.emrcontainers.virtual_clusters (
 ContainerProvider,
 Name,
 Tags,
 region
)
SELECT 
 '{{ ContainerProvider }}',
 '{{ Name }}',
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
  - name: virtual_cluster
    props:
      - name: ContainerProvider
        value:
          Type: '{{ Type }}'
          Id: '{{ Id }}'
          Info:
            EksInfo:
              Namespace: '{{ Namespace }}'
      - name: Name
        value: '{{ Name }}'
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
DELETE FROM aws.emrcontainers.virtual_clusters
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>virtual_clusters</code> resource, the following permissions are required:

### Create
```json
emr-containers:CreateVirtualCluster,
emr-containers:TagResource,
iam:CreateServiceLinkedRole
```

### Read
```json
emr-containers:DescribeVirtualCluster
```

### Delete
```json
emr-containers:DeleteVirtualCluster
```

### List
```json
emr-containers:ListVirtualClusters
```

### Update
```json
emr-containers:DescribeVirtualCluster,
emr-containers:ListTagsForResource,
emr-containers:TagResource,
emr-containers:UntagResource
```


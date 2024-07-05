---
title: replication_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_configurations
  - ecr
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

Creates, updates, deletes or gets a <code>replication_configuration</code> resource or lists <code>replication_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ECR::ReplicationConfiguration resource configures the replication destinations for an Amazon Elastic Container Registry (Amazon Private ECR). For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.replication_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="replication_configuration" /></td><td><code>object</code></td><td>The AWS::ECR::ReplicationConfiguration resource configures the replication destinations for an Amazon Elastic Container Registry (Amazon Private ECR). For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html</td></tr>
<tr><td><CopyableCode code="registry_id" /></td><td><code>string</code></td><td>The RegistryId associated with the aws account.</td></tr>
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
    <td><CopyableCode code="ReplicationConfiguration, region" /></td>
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
Gets all <code>replication_configurations</code> in a region.
```sql
SELECT
region,
replication_configuration,
registry_id
FROM aws.ecr.replication_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>replication_configuration</code>.
```sql
SELECT
region,
replication_configuration,
registry_id
FROM aws.ecr.replication_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<RegistryId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ecr.replication_configurations (
 ReplicationConfiguration,
 region
)
SELECT 
'{{ ReplicationConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ecr.replication_configurations (
 ReplicationConfiguration,
 region
)
SELECT 
 '{{ ReplicationConfiguration }}',
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
  - name: replication_configuration
    props:
      - name: ReplicationConfiguration
        value:
          ReplicationConfiguration: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ecr.replication_configurations
WHERE data__Identifier = '<RegistryId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>replication_configurations</code> resource, the following permissions are required:

### Create
```json
ecr:DescribeRegistry,
ecr:PutReplicationConfiguration,
iam:CreateServiceLinkedRole
```

### Read
```json
ecr:DescribeRegistry
```

### Update
```json
ecr:DescribeRegistry,
ecr:PutReplicationConfiguration,
iam:CreateServiceLinkedRole
```

### Delete
```json
ecr:DescribeRegistry,
ecr:PutReplicationConfiguration,
iam:CreateServiceLinkedRole
```

### List
```json
ecr:DescribeRegistry
```


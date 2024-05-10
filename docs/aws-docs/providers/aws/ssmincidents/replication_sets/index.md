---
title: replication_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_sets
  - ssmincidents
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


Used to retrieve a list of <code>replication_sets</code> in a region or to create or delete a <code>replication_sets</code> resource, use <code>replication_set</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ReplicationSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmincidents.replication_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td>The ARN of the ReplicationSet.</td></tr>
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
arn
FROM aws.ssmincidents.replication_sets
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>replication_set</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- replication_set.iql (required properties only)
INSERT INTO aws.ssmincidents.replication_sets (
 Regions,
 region
)
SELECT 
'{{ Regions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- replication_set.iql (all properties)
INSERT INTO aws.ssmincidents.replication_sets (
 Regions,
 DeletionProtected,
 Tags,
 region
)
SELECT 
 '{{ Regions }}',
 '{{ DeletionProtected }}',
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
  - name: replication_set
    props:
      - name: Regions
        value:
          - RegionName: '{{ RegionName }}'
            RegionConfiguration:
              SseKmsKeyId: '{{ SseKmsKeyId }}'
      - name: DeletionProtected
        value: '{{ DeletionProtected }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ssmincidents.replication_sets
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>replication_sets</code> resource, the following permissions are required:

### Create
```json
ssm-incidents:CreateReplicationSet,
ssm-incidents:ListReplicationSets,
ssm-incidents:UpdateDeletionProtection,
ssm-incidents:GetReplicationSet,
ssm-incidents:TagResource,
ssm-incidents:ListTagsForResource,
iam:CreateServiceLinkedRole
```

### Delete
```json
ssm-incidents:DeleteReplicationSet,
ssm-incidents:GetReplicationSet
```

### List
```json
ssm-incidents:ListReplicationSets
```


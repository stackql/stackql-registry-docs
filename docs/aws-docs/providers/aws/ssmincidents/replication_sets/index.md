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

Creates, updates, deletes or gets a <code>replication_set</code> resource or lists <code>replication_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ReplicationSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmincidents.replication_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the ReplicationSet.</td></tr>
<tr><td><CopyableCode code="regions" /></td><td><code>array</code></td><td>The ReplicationSet configuration.</td></tr>
<tr><td><CopyableCode code="deletion_protected" /></td><td><code>boolean</code></td><td>Configures the ReplicationSet deletion protection.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to apply to the replication set.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmincidents-replicationset.html"><code>AWS::SSMIncidents::ReplicationSet</code></a>.

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
    <td><CopyableCode code="Regions, region" /></td>
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
Gets all <code>replication_sets</code> in a region.
```sql
SELECT
region,
arn,
regions,
deletion_protected,
tags
FROM aws.ssmincidents.replication_sets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>replication_set</code>.
```sql
SELECT
region,
arn,
regions,
deletion_protected,
tags
FROM aws.ssmincidents.replication_sets
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
ssm-incidents:ListReplicationSets,
ssm-incidents:GetReplicationSet,
ssm-incidents:ListTagsForResource
```

### Update
```json
ssm-incidents:UpdateReplicationSet,
ssm-incidents:UpdateDeletionProtection,
ssm-incidents:GetReplicationSet,
ssm-incidents:TagResource,
ssm-incidents:UntagResource,
ssm-incidents:ListTagsForResource
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

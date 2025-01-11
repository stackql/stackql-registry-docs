---
title: table_bucket_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - table_bucket_policies
  - s3tables
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

Creates, updates, deletes or gets a <code>table_bucket_policy</code> resource or lists <code>table_bucket_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_bucket_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Applies an IAM resource policy to a table bucket.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3tables.table_bucket_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resource_policy" /></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified table bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.</td></tr>
<tr><td><CopyableCode code="table_bucket_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the table bucket to which the policy applies.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3tables-tablebucketpolicy.html"><code>AWS::S3Tables::TableBucketPolicy</code></a>.

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
    <td><CopyableCode code="ResourcePolicy, TableBucketARN, region" /></td>
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
Gets all <code>table_bucket_policies</code> in a region.
```sql
SELECT
region,
resource_policy,
table_bucket_arn
FROM aws.s3tables.table_bucket_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>table_bucket_policy</code>.
```sql
SELECT
region,
resource_policy,
table_bucket_arn
FROM aws.s3tables.table_bucket_policies
WHERE region = 'us-east-1' AND data__Identifier = '<TableBucketARN>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>table_bucket_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.s3tables.table_bucket_policies (
 ResourcePolicy,
 TableBucketARN,
 region
)
SELECT 
'{{ ResourcePolicy }}',
 '{{ TableBucketARN }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.s3tables.table_bucket_policies (
 ResourcePolicy,
 TableBucketARN,
 region
)
SELECT 
 '{{ ResourcePolicy }}',
 '{{ TableBucketARN }}',
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
  - name: table_bucket_policy
    props:
      - name: ResourcePolicy
        value: {}
      - name: TableBucketARN
        value: '{{ TableBucketARN }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.s3tables.table_bucket_policies
WHERE data__Identifier = '<TableBucketARN>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>table_bucket_policies</code> resource, the following permissions are required:

### Create
```json
s3tables:GetTableBucket,
s3tables:GetTableBucketPolicy,
s3tables:PutTableBucketPolicy
```

### Read
```json
s3tables:GetTableBucketPolicy
```

### Update
```json
s3tables:GetTableBucketPolicy,
s3tables:PutTableBucketPolicy
```

### Delete
```json
s3tables:GetTableBucketPolicy,
s3tables:DeleteTableBucketPolicy
```

### List
```json
s3tables:GetTableBucketPolicy,
s3tables:ListTableBuckets
```

---
title: secret_target_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_target_attachments
  - secretsmanager
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

Creates, updates, deletes or gets a <code>secret_target_attachment</code> resource or lists <code>secret_target_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret_target_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecretsManager::SecretTargetAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.secretsmanager.secret_target_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="secret_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html"><code>AWS::SecretsManager::SecretTargetAttachment</code></a>.

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
    <td><CopyableCode code="TargetType, TargetId, SecretId, region" /></td>
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
Gets all <code>secret_target_attachments</code> in a region.
```sql
SELECT
region,
id,
secret_id,
target_type,
target_id
FROM aws.secretsmanager.secret_target_attachments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>secret_target_attachment</code>.
```sql
SELECT
region,
id,
secret_id,
target_type,
target_id
FROM aws.secretsmanager.secret_target_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>secret_target_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.secretsmanager.secret_target_attachments (
 SecretId,
 TargetType,
 TargetId,
 region
)
SELECT 
'{{ SecretId }}',
 '{{ TargetType }}',
 '{{ TargetId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.secretsmanager.secret_target_attachments (
 SecretId,
 TargetType,
 TargetId,
 region
)
SELECT 
 '{{ SecretId }}',
 '{{ TargetType }}',
 '{{ TargetId }}',
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
  - name: secret_target_attachment
    props:
      - name: SecretId
        value: '{{ SecretId }}'
      - name: TargetType
        value: '{{ TargetType }}'
      - name: TargetId
        value: '{{ TargetId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.secretsmanager.secret_target_attachments
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>secret_target_attachments</code> resource, the following permissions are required:

### Read
```json
secretsmanager:GetSecretValue
```

### List
```json
secretsmanager:GetSecretValue,
secretsmanager:ListSecrets
```

### Create
```json
secretsmanager:GetSecretValue,
secretsmanager:PutSecretValue,
rds:DescribeDBInstances,
redshift:DescribeClusters,
rds:DescribeDBClusters,
docdb-elastic:GetCluster,
redshift-serverless:ListWorkgroups,
redshift-serverless:GetNamespace
```

### Delete
```json
secretsmanager:GetSecretValue,
secretsmanager:PutSecretValue
```

### Update
```json
secretsmanager:GetSecretValue,
secretsmanager:PutSecretValue,
rds:DescribeDBInstances,
redshift:DescribeClusters,
rds:DescribeDBClusters,
docdb-elastic:GetCluster,
redshift-serverless:ListWorkgroups,
redshift-serverless:GetNamespace
```

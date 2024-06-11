---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - rds
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

Creates, updates, deletes or gets an <code>integration</code> resource or lists <code>integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a zero-ETL integration with Amazon Redshift.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="integration_name" /></td><td><code>string</code></td><td>The name of the integration.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the integration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="data_filter" /></td><td><code>string</code></td><td>The data filter for the integration.</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Aurora DB cluster to use as the source for replication.</td></tr>
<tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td>The ARN of the Redshift data warehouse to use as the target for replication.</td></tr>
<tr><td><CopyableCode code="integration_arn" /></td><td><code>string</code></td><td>The ARN of the integration.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>An optional AWS Key Management System (AWS KMS) key ARN for the key used to to encrypt the integration. The resource accepts the key ID and the key ARN forms. The key ID form can be used if the KMS key is owned by te same account. If the KMS key belongs to a different account than the calling account, the full key ARN must be specified. Do not use the key alias or the key alias ARN as this will cause a false drift of the resource.</td></tr>
<tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>An optional set of non-secret key–value pairs that contains additional contextual information about the data.</code></td><td></td></tr>
<tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="SourceArn, TargetArn, region" /></td>
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
List all <code>integrations</code> in a region.
```sql
SELECT
region,
integration_arn
FROM aws.rds.integrations
WHERE region = 'us-east-1';
```
Gets all properties from an <code>integration</code>.
```sql
SELECT
region,
integration_name,
description,
tags,
data_filter,
source_arn,
target_arn,
integration_arn,
kms_key_id,
additional_encryption_context,
create_time
FROM aws.rds.integrations
WHERE region = 'us-east-1' AND data__Identifier = '<IntegrationArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rds.integrations (
 SourceArn,
 TargetArn,
 region
)
SELECT 
'{{ SourceArn }}',
 '{{ TargetArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.integrations (
 IntegrationName,
 Description,
 Tags,
 DataFilter,
 SourceArn,
 TargetArn,
 KMSKeyId,
 AdditionalEncryptionContext,
 region
)
SELECT 
 '{{ IntegrationName }}',
 '{{ Description }}',
 '{{ Tags }}',
 '{{ DataFilter }}',
 '{{ SourceArn }}',
 '{{ TargetArn }}',
 '{{ KMSKeyId }}',
 '{{ AdditionalEncryptionContext }}',
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
  - name: integration
    props:
      - name: IntegrationName
        value: '{{ IntegrationName }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: DataFilter
        value: '{{ DataFilter }}'
      - name: SourceArn
        value: '{{ SourceArn }}'
      - name: TargetArn
        value: '{{ TargetArn }}'
      - name: KMSKeyId
        value: '{{ KMSKeyId }}'
      - name: AdditionalEncryptionContext
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.rds.integrations
WHERE data__Identifier = '<IntegrationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>integrations</code> resource, the following permissions are required:

### Create
```json
rds:CreateIntegration,
rds:DescribeIntegrations,
rds:AddTagsToResource,
kms:CreateGrant,
kms:DescribeKey,
redshift:CreateInboundIntegration
```

### Read
```json
rds:DescribeIntegrations
```

### Update
```json
rds:DescribeIntegrations,
rds:AddTagsToResource,
rds:RemoveTagsFromResource,
rds:ModifyIntegration
```

### Delete
```json
rds:DeleteIntegration,
rds:DescribeIntegrations
```

### List
```json
rds:DescribeIntegrations
```


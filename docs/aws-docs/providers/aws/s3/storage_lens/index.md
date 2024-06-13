---
title: storage_lens
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_lens
  - s3
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

Creates, updates, deletes or gets a <code>storage_len</code> resource or lists <code>storage_lens</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_lens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::StorageLens resource is an Amazon S3 resource type that you can use to create Storage Lens configurations.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.storage_lens" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="storage_lens_configuration" /></td><td><code>object</code></td><td>Specifies the details of Amazon S3 Storage Lens configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.</td></tr>
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
    <td><CopyableCode code="StorageLensConfiguration, region" /></td>
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
List all <code>storage_lens</code> in a region.
```sql
SELECT
region,
storage_lens_configuration/id
FROM aws.s3.storage_lens
WHERE region = 'us-east-1';
```
Gets all properties from a <code>storage_len</code>.
```sql
SELECT
region,
storage_lens_configuration,
tags
FROM aws.s3.storage_lens
WHERE region = 'us-east-1' AND data__Identifier = '<StorageLensConfiguration/Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_len</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.s3.storage_lens (
 StorageLensConfiguration,
 region
)
SELECT 
'{{ StorageLensConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.s3.storage_lens (
 StorageLensConfiguration,
 Tags,
 region
)
SELECT 
 '{{ StorageLensConfiguration }}',
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
  - name: storage_len
    props:
      - name: StorageLensConfiguration
        value:
          Id: '{{ Id }}'
          Include:
            Buckets:
              - '{{ Buckets[0] }}'
            Regions:
              - '{{ Regions[0] }}'
          Exclude: null
          AwsOrg:
            Arn: null
          AccountLevel:
            ActivityMetrics:
              IsEnabled: '{{ IsEnabled }}'
            AdvancedCostOptimizationMetrics:
              IsEnabled: '{{ IsEnabled }}'
            AdvancedDataProtectionMetrics:
              IsEnabled: '{{ IsEnabled }}'
            DetailedStatusCodesMetrics:
              IsEnabled: '{{ IsEnabled }}'
            BucketLevel:
              ActivityMetrics: null
              AdvancedCostOptimizationMetrics: null
              AdvancedDataProtectionMetrics: null
              DetailedStatusCodesMetrics: null
              PrefixLevel:
                StorageMetrics:
                  IsEnabled: '{{ IsEnabled }}'
                  SelectionCriteria:
                    MaxDepth: '{{ MaxDepth }}'
                    Delimiter: '{{ Delimiter }}'
                    MinStorageBytesPercentage: null
            StorageLensGroupLevel:
              StorageLensGroupSelectionCriteria:
                Include:
                  - '{{ Include[0] }}'
                Exclude:
                  - null
          DataExport:
            S3BucketDestination:
              OutputSchemaVersion: '{{ OutputSchemaVersion }}'
              Format: '{{ Format }}'
              AccountId: '{{ AccountId }}'
              Arn: '{{ Arn }}'
              Prefix: '{{ Prefix }}'
              Encryption: {}
            CloudWatchMetrics:
              IsEnabled: '{{ IsEnabled }}'
          IsEnabled: '{{ IsEnabled }}'
          StorageLensArn: '{{ StorageLensArn }}'
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
DELETE FROM aws.s3.storage_lens
WHERE data__Identifier = '<StorageLensConfiguration/Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>storage_lens</code> resource, the following permissions are required:

### Create
```json
s3:PutStorageLensConfiguration,
s3:PutStorageLensConfigurationTagging,
s3:GetStorageLensConfiguration,
s3:GetStorageLensConfigurationTagging,
organizations:DescribeOrganization,
organizations:ListAccounts,
organizations:ListAWSServiceAccessForOrganization,
organizations:ListDelegatedAdministrators,
iam:CreateServiceLinkedRole
```

### Read
```json
s3:GetStorageLensConfiguration,
s3:GetStorageLensConfigurationTagging
```

### Update
```json
s3:PutStorageLensConfiguration,
s3:PutStorageLensConfigurationTagging,
s3:GetStorageLensConfiguration,
s3:GetStorageLensConfigurationTagging,
organizations:DescribeOrganization,
organizations:ListAccounts,
organizations:ListAWSServiceAccessForOrganization,
organizations:ListDelegatedAdministrators,
iam:CreateServiceLinkedRole
```

### Delete
```json
s3:DeleteStorageLensConfiguration,
s3:DeleteStorageLensConfigurationTagging
```

### List
```json
s3:ListStorageLensConfigurations
```


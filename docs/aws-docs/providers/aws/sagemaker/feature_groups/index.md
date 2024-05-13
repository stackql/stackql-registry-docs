---
title: feature_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_groups
  - sagemaker
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


Used to retrieve a list of <code>feature_groups</code> in a region or to create or delete a <code>feature_groups</code> resource, use <code>feature_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::FeatureGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.feature_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="feature_group_name" /></td><td><code>string</code></td><td>The Name of the FeatureGroup.</td></tr>
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
    <td><CopyableCode code="FeatureGroupName, RecordIdentifierFeatureName, EventTimeFeatureName, FeatureDefinitions, region" /></td>
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
feature_group_name
FROM aws.sagemaker.feature_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>feature_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.feature_groups (
 FeatureGroupName,
 RecordIdentifierFeatureName,
 EventTimeFeatureName,
 FeatureDefinitions,
 region
)
SELECT 
'{{ FeatureGroupName }}',
 '{{ RecordIdentifierFeatureName }}',
 '{{ EventTimeFeatureName }}',
 '{{ FeatureDefinitions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.feature_groups (
 FeatureGroupName,
 RecordIdentifierFeatureName,
 EventTimeFeatureName,
 FeatureDefinitions,
 OnlineStoreConfig,
 OfflineStoreConfig,
 ThroughputConfig,
 RoleArn,
 Description,
 Tags,
 region
)
SELECT 
 '{{ FeatureGroupName }}',
 '{{ RecordIdentifierFeatureName }}',
 '{{ EventTimeFeatureName }}',
 '{{ FeatureDefinitions }}',
 '{{ OnlineStoreConfig }}',
 '{{ OfflineStoreConfig }}',
 '{{ ThroughputConfig }}',
 '{{ RoleArn }}',
 '{{ Description }}',
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
  - name: feature_group
    props:
      - name: FeatureGroupName
        value: '{{ FeatureGroupName }}'
      - name: RecordIdentifierFeatureName
        value: '{{ RecordIdentifierFeatureName }}'
      - name: EventTimeFeatureName
        value: '{{ EventTimeFeatureName }}'
      - name: FeatureDefinitions
        value:
          - FeatureName: '{{ FeatureName }}'
            FeatureType: '{{ FeatureType }}'
      - name: OnlineStoreConfig
        value:
          SecurityConfig:
            KmsKeyId: '{{ KmsKeyId }}'
          EnableOnlineStore: '{{ EnableOnlineStore }}'
          StorageType: '{{ StorageType }}'
          TtlDuration:
            Unit: '{{ Unit }}'
            Value: '{{ Value }}'
      - name: OfflineStoreConfig
        value:
          S3StorageConfig:
            S3Uri: '{{ S3Uri }}'
            KmsKeyId: null
          DisableGlueTableCreation: '{{ DisableGlueTableCreation }}'
          DataCatalogConfig:
            TableName: '{{ TableName }}'
            Catalog: '{{ Catalog }}'
            Database: '{{ Database }}'
          TableFormat: '{{ TableFormat }}'
      - name: ThroughputConfig
        value:
          ThroughputMode: '{{ ThroughputMode }}'
          ProvisionedReadCapacityUnits: '{{ ProvisionedReadCapacityUnits }}'
          ProvisionedWriteCapacityUnits: '{{ ProvisionedWriteCapacityUnits }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.feature_groups
WHERE data__Identifier = '<FeatureGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>feature_groups</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
kms:CreateGrant,
kms:DescribeKey,
glue:CreateTable,
glue:GetTable,
glue:CreateDatabase,
glue:GetDatabase,
sagemaker:CreateFeatureGroup,
sagemaker:DescribeFeatureGroup,
sagemaker:AddTags,
sagemaker:ListTags
```

### Delete
```json
sagemaker:DeleteFeatureGroup,
sagemaker:DescribeFeatureGroup
```

### List
```json
sagemaker:ListFeatureGroups
```


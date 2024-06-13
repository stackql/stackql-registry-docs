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

Creates, updates, deletes or gets a <code>feature_group</code> resource or lists <code>feature_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::FeatureGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.feature_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="feature_group_name" /></td><td><code>string</code></td><td>The Name of the FeatureGroup.</td></tr>
<tr><td><CopyableCode code="record_identifier_feature_name" /></td><td><code>string</code></td><td>The Record Identifier Feature Name.</td></tr>
<tr><td><CopyableCode code="event_time_feature_name" /></td><td><code>string</code></td><td>The Event Time Feature Name.</td></tr>
<tr><td><CopyableCode code="feature_definitions" /></td><td><code>array</code></td><td>An Array of Feature Definition</td></tr>
<tr><td><CopyableCode code="online_store_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="offline_store_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="throughput_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description about the FeatureGroup.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>A timestamp of FeatureGroup creation time.</td></tr>
<tr><td><CopyableCode code="feature_group_status" /></td><td><code>string</code></td><td>The status of the feature group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pair to apply to this resource.</td></tr>
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
List all <code>feature_groups</code> in a region.
```sql
SELECT
region,
feature_group_name
FROM aws.sagemaker.feature_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>feature_group</code>.
```sql
SELECT
region,
feature_group_name,
record_identifier_feature_name,
event_time_feature_name,
feature_definitions,
online_store_config,
offline_store_config,
throughput_config,
role_arn,
description,
creation_time,
feature_group_status,
tags
FROM aws.sagemaker.feature_groups
WHERE region = 'us-east-1' AND data__Identifier = '<FeatureGroupName>';
```


## `INSERT` example

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

## `DELETE` example

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

### Update
```json
sagemaker:UpdateFeatureGroup,
sagemaker:DescribeFeatureGroup,
sagemaker:AddTags,
sagemaker:ListTags,
sagemaker:DeleteTags
```

### Read
```json
sagemaker:DescribeFeatureGroup,
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


---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
  - qbusiness
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

Creates, updates, deletes or gets a <code>data_source</code> resource or lists <code>data_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::DataSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.data_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code></code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_source_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_source_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="document_enrichment_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="index_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sync_schedule" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_configuration" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="ApplicationId, IndexId, Configuration, DisplayName, region" /></td>
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
List all <code>data_sources</code> in a region.
```sql
SELECT
region,
application_id,
data_source_id,
index_id
FROM aws.qbusiness.data_sources
WHERE region = 'us-east-1';
```
Gets all properties from a <code>data_source</code>.
```sql
SELECT
region,
application_id,
configuration,
created_at,
data_source_arn,
data_source_id,
description,
display_name,
document_enrichment_configuration,
index_id,
role_arn,
status,
sync_schedule,
tags,
type,
updated_at,
vpc_configuration
FROM aws.qbusiness.data_sources
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<DataSourceId>|<IndexId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.qbusiness.data_sources (
 ApplicationId,
 Configuration,
 DisplayName,
 IndexId,
 region
)
SELECT 
'{{ ApplicationId }}',
 '{{ Configuration }}',
 '{{ DisplayName }}',
 '{{ IndexId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.qbusiness.data_sources (
 ApplicationId,
 Configuration,
 Description,
 DisplayName,
 DocumentEnrichmentConfiguration,
 IndexId,
 RoleArn,
 SyncSchedule,
 Tags,
 VpcConfiguration,
 region
)
SELECT 
 '{{ ApplicationId }}',
 '{{ Configuration }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ DocumentEnrichmentConfiguration }}',
 '{{ IndexId }}',
 '{{ RoleArn }}',
 '{{ SyncSchedule }}',
 '{{ Tags }}',
 '{{ VpcConfiguration }}',
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
  - name: data_source
    props:
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: Configuration
        value: null
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: DocumentEnrichmentConfiguration
        value:
          InlineConfigurations:
            - Condition:
                Key: '{{ Key }}'
                Operator: '{{ Operator }}'
                Value: null
              Target:
                Key: '{{ Key }}'
                Value: null
                AttributeValueOperator: '{{ AttributeValueOperator }}'
              DocumentContentOperator: '{{ DocumentContentOperator }}'
          PreExtractionHookConfiguration:
            InvocationCondition: null
            LambdaArn: '{{ LambdaArn }}'
            S3BucketName: '{{ S3BucketName }}'
            RoleArn: '{{ RoleArn }}'
          PostExtractionHookConfiguration: null
      - name: IndexId
        value: '{{ IndexId }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: SyncSchedule
        value: '{{ SyncSchedule }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VpcConfiguration
        value:
          SubnetIds:
            - '{{ SubnetIds[0] }}'
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.qbusiness.data_sources
WHERE data__Identifier = '<ApplicationId|DataSourceId|IndexId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_sources</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
qbusiness:CreateDataSource,
qbusiness:GetDataSource,
qbusiness:ListTagsForResource,
qbusiness:TagResource
```

### Read
```json
qbusiness:GetDataSource,
qbusiness:ListTagsForResource
```

### Update
```json
iam:PassRole,
qbusiness:GetDataSource,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
qbusiness:UntagResource,
qbusiness:UpdateDataSource
```

### Delete
```json
qbusiness:DeleteDataSource,
qbusiness:GetDataSource
```

### List
```json
qbusiness:ListDataSources
```


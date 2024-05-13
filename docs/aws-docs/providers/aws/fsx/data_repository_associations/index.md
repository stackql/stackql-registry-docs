---
title: data_repository_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_repository_associations
  - fsx
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


Used to retrieve a list of <code>data_repository_associations</code> in a region or to create or delete a <code>data_repository_associations</code> resource, use <code>data_repository_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_repository_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon FSx for Lustre data repository association (DRA). A data repository association is a link between a directory on the file system and an Amazon S3 bucket or prefix. You can have a maximum of 8 data repository associations on a file system. Data repository associations are supported on all FSx for Lustre 2.12 and newer file systems, excluding <code>scratch_1</code> deployment type. &lt;br&#x2F;&gt; Each data repository association must have a unique Amazon FSx file system directory and a unique S3 bucket or prefix associated with it. You can configure a data repository association for automatic import only, for automatic export only, or for both. To learn more about linking a data repository to your file system, see &#91;Linking your file system to an S3 bucket&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;fsx&#x2F;latest&#x2F;LustreGuide&#x2F;create-dra-linked-data-repo.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fsx.data_repository_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="FileSystemId, FileSystemPath, DataRepositoryPath, region" /></td>
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
association_id
FROM aws.fsx.data_repository_associations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>data_repository_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.fsx.data_repository_associations (
 FileSystemId,
 FileSystemPath,
 DataRepositoryPath,
 region
)
SELECT 
'{{ FileSystemId }}',
 '{{ FileSystemPath }}',
 '{{ DataRepositoryPath }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.fsx.data_repository_associations (
 FileSystemId,
 FileSystemPath,
 DataRepositoryPath,
 BatchImportMetaDataOnCreate,
 ImportedFileChunkSize,
 S3,
 Tags,
 region
)
SELECT 
 '{{ FileSystemId }}',
 '{{ FileSystemPath }}',
 '{{ DataRepositoryPath }}',
 '{{ BatchImportMetaDataOnCreate }}',
 '{{ ImportedFileChunkSize }}',
 '{{ S3 }}',
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
  - name: data_repository_association
    props:
      - name: FileSystemId
        value: '{{ FileSystemId }}'
      - name: FileSystemPath
        value: '{{ FileSystemPath }}'
      - name: DataRepositoryPath
        value: '{{ DataRepositoryPath }}'
      - name: BatchImportMetaDataOnCreate
        value: '{{ BatchImportMetaDataOnCreate }}'
      - name: ImportedFileChunkSize
        value: '{{ ImportedFileChunkSize }}'
      - name: S3
        value:
          AutoImportPolicy:
            Events:
              - '{{ Events[0] }}'
          AutoExportPolicy:
            Events: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.fsx.data_repository_associations
WHERE data__Identifier = '<AssociationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_repository_associations</code> resource, the following permissions are required:

### Create
```json
fsx:CreateDataRepositoryAssociation,
fsx:DescribeDataRepositoryAssociations,
fsx:TagResource,
s3:ListBucket,
s3:GetBucketPolicy,
s3:PutBucketPolicy,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy
```

### Delete
```json
fsx:DescribeDataRepositoryAssociations,
fsx:DeleteDataRepositoryAssociation
```

### List
```json
fsx:DescribeDataRepositoryAssociations
```


---
title: data_repository_association
hide_title: false
hide_table_of_contents: false
keywords:
  - data_repository_association
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
Gets or operates on an individual <code>data_repository_association</code> resource, use <code>data_repository_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_repository_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon FSx for Lustre data repository association (DRA). A data repository association is a link between a directory on the file system and an Amazon S3 bucket or prefix. You can have a maximum of 8 data repository associations on a file system. Data repository associations are supported on all FSx for Lustre 2.12 and newer file systems, excluding ``scratch_1`` deployment type. &lt;br&#x2F;&gt; Each data repository association must have a unique Amazon FSx file system directory and a unique S3 bucket or prefix associated with it. You can configure a data repository association for automatic import only, for automatic export only, or for both. To learn more about linking a data repository to your file system, see &#91;Linking your file system to an S3 bucket&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;fsx&#x2F;latest&#x2F;LustreGuide&#x2F;create-dra-linked-data-repo.html).</td></tr>
<tr><td><b>Id</b></td><td><code>aws.fsx.data_repository_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>association_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>file_system_id</code></td><td><code>string</code></td><td>The ID of the file system on which the data repository association is configured.</td></tr>
<tr><td><code>file_system_path</code></td><td><code>string</code></td><td>A path on the Amazon FSx for Lustre file system that points to a high-level directory (such as ``&#x2F;ns1&#x2F;``) or subdirectory (such as ``&#x2F;ns1&#x2F;subdir&#x2F;``) that will be mapped 1-1 with ``DataRepositoryPath``. The leading forward slash in the name is required. Two data repository associations cannot have overlapping file system paths. For example, if a data repository is associated with file system path ``&#x2F;ns1&#x2F;``, then you cannot link another data repository with file system path ``&#x2F;ns1&#x2F;ns2``.&lt;br&#x2F;&gt; This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.&lt;br&#x2F;&gt;  If you specify only a forward slash (``&#x2F;``) as the file system path, you can link only one data repository to the file system. You can only specify "&#x2F;" as the file system path for the first data repository associated with a file system.</td></tr>
<tr><td><code>data_repository_path</code></td><td><code>string</code></td><td>The path to the Amazon S3 data repository that will be linked to the file system. The path can be an S3 bucket or prefix in the format ``s3:&#x2F;&#x2F;myBucket&#x2F;myPrefix&#x2F;``. This path specifies where in the S3 data repository files will be imported from or exported to.</td></tr>
<tr><td><code>batch_import_meta_data_on_create</code></td><td><code>boolean</code></td><td>A boolean flag indicating whether an import data repository task to import metadata should run after the data repository association is created. The task runs if this flag is set to ``true``.</td></tr>
<tr><td><code>imported_file_chunk_size</code></td><td><code>integer</code></td><td>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system or cache.&lt;br&#x2F;&gt; The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.</td></tr>
<tr><td><code>s3</code></td><td><code>object</code></td><td>The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.&lt;br&#x2F;&gt; For more information, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
association_id,
resource_arn,
file_system_id,
file_system_path,
data_repository_path,
batch_import_meta_data_on_create,
imported_file_chunk_size,
s3,
tags
FROM aws.fsx.data_repository_association
WHERE data__Identifier = '<AssociationId>';
```

## Permissions

To operate on the <code>data_repository_association</code> resource, the following permissions are required:

### Read
```json
fsx:DescribeDataRepositoryAssociations
```

### Update
```json
fsx:DescribeDataRepositoryAssociations,
fsx:UpdateDataRepositoryAssociation,
fsx:TagResource,
fsx:UntagResource,
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


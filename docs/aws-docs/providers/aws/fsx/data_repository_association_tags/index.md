---
title: data_repository_association_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - data_repository_association_tags
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

Expands all tag keys and values for <code>data_repository_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_repository_association_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon FSx for Lustre data repository association (DRA). A data repository association is a link between a directory on the file system and an Amazon S3 bucket or prefix. You can have a maximum of 8 data repository associations on a file system. Data repository associations are supported on all FSx for Lustre 2.12 and newer file systems, excluding <code>scratch_1</code> deployment type. <br />Each data repository association must have a unique Amazon FSx file system directory and a unique S3 bucket or prefix associated with it. You can configure a data repository association for automatic import only, for automatic export only, or for both. To learn more about linking a data repository to your file system, see &#91;Linking your file system to an S3 bucket&#93;(https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fsx.data_repository_association_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="file_system_id" /></td><td><code>string</code></td><td>The ID of the file system on which the data repository association is configured.</td></tr>
<tr><td><CopyableCode code="file_system_path" /></td><td><code>string</code></td><td>A path on the Amazon FSx for Lustre file system that points to a high-level directory (such as <code>/ns1/</code>) or subdirectory (such as <code>/ns1/subdir/</code>) that will be mapped 1-1 with <code>DataRepositoryPath</code>. The leading forward slash in the name is required. Two data repository associations cannot have overlapping file system paths. For example, if a data repository is associated with file system path <code>/ns1/</code>, then you cannot link another data repository with file system path <code>/ns1/ns2</code>.<br />This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.<br />If you specify only a forward slash (<code>/</code>) as the file system path, you can link only one data repository to the file system. You can only specify "/" as the file system path for the first data repository associated with a file system.</td></tr>
<tr><td><CopyableCode code="data_repository_path" /></td><td><code>string</code></td><td>The path to the Amazon S3 data repository that will be linked to the file system. The path can be an S3 bucket or prefix in the format <code>s3://myBucket/myPrefix/</code>. This path specifies where in the S3 data repository files will be imported from or exported to.</td></tr>
<tr><td><CopyableCode code="batch_import_meta_data_on_create" /></td><td><code>boolean</code></td><td>A boolean flag indicating whether an import data repository task to import metadata should run after the data repository association is created. The task runs if this flag is set to <code>true</code>.</td></tr>
<tr><td><CopyableCode code="imported_file_chunk_size" /></td><td><code>integer</code></td><td>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system or cache.<br />The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.</td></tr>
<tr><td><CopyableCode code="s3" /></td><td><code>object</code></td><td>The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>data_repository_associations</code> in a region.
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
tag_key,
tag_value
FROM aws.fsx.data_repository_association_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_repository_association_tags</code> resource, see <a href="/providers/aws/fsx/data_repository_associations/#permissions"><code>data_repository_associations</code></a>



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
Gets an individual <code>data_repository_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_repository_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.fsx.data_repository_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AssociationId</code></td><td><code>string</code></td><td>The system-generated, unique ID of the data repository association.</td></tr><tr><td><code>ResourceARN</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.</td></tr><tr><td><code>FileSystemId</code></td><td><code>string</code></td><td>The globally unique ID of the file system, assigned by Amazon FSx.</td></tr><tr><td><code>FileSystemPath</code></td><td><code>string</code></td><td>This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.</td></tr><tr><td><code>DataRepositoryPath</code></td><td><code>string</code></td><td>The path to the Amazon S3 data repository that will be linked to the file system. The path can be an S3 bucket or prefix in the format s3://myBucket/myPrefix/ . This path specifies where in the S3 data repository files will be imported from or exported to.</td></tr><tr><td><code>BatchImportMetaDataOnCreate</code></td><td><code>boolean</code></td><td>A boolean flag indicating whether an import data repository task to import metadata should run after the data repository association is created. The task runs if this flag is set to true.</td></tr><tr><td><code>ImportedFileChunkSize</code></td><td><code>integer</code></td><td>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.</td></tr><tr><td><code>S3</code></td><td><code>undefined</code></td><td>The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of Tag values, with a maximum of 50 elements.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.fsx.data_repository_association
WHERE region = 'us-east-1' AND data__Identifier = '{AssociationId}'
```

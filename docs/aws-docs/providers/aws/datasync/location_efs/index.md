---
title: location_efs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_efs
  - datasync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>location_efs</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_efs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datasync.location_efs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Ec2Config</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>EfsFilesystemArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the Amazon EFS file system.</td></tr><tr><td><code>AccessPointArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the Amazon EFS Access point that DataSync uses when accessing the EFS file system.</td></tr><tr><td><code>FileSystemAccessRoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS IAM role that the DataSync will assume when mounting the EFS file system.</td></tr><tr><td><code>InTransitEncryption</code></td><td><code>string</code></td><td>Protocol that is used for encrypting the traffic exchanged between the DataSync Agent and the EFS file system.</td></tr><tr><td><code>Subdirectory</code></td><td><code>string</code></td><td>A subdirectory in the location's path. This subdirectory in the EFS file system is used to read data from the EFS source location or write data to the EFS destination.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>LocationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.</td></tr><tr><td><code>LocationUri</code></td><td><code>string</code></td><td>The URL of the EFS location that was described.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.datasync.location_efs
WHERE region = 'us-east-1' AND data__Identifier = '{LocationArn}'
```

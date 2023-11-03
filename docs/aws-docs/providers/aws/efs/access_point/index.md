---
title: access_point
hide_title: false
hide_table_of_contents: false
keywords:
  - access_point
  - efs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>access_point</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.efs.access_point</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AccessPointId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ClientToken</code></td><td><code>string</code></td><td>(optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.</td></tr><tr><td><code>AccessPointTags</code></td><td><code>array</code></td><td></td></tr><tr><td><code>FileSystemId</code></td><td><code>string</code></td><td>The ID of the EFS file system that the access point provides access to.</td></tr><tr><td><code>PosixUser</code></td><td><code>undefined</code></td><td>The operating system user and group applied to all file system requests made using the access point.</td></tr><tr><td><code>RootDirectory</code></td><td><code>undefined</code></td><td>Specifies the directory on the Amazon EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the RootDirectory>Path specified does not exist, EFS creates it and applies the CreationInfo settings when a client connects to an access point. When specifying a RootDirectory, you need to provide the Path, and the CreationInfo is optional.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.efs.access_point
WHERE region = 'us-east-1' AND data__Identifier = '{AccessPointId}'
</pre>

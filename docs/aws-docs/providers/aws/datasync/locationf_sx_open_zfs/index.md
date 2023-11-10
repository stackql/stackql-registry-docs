---
title: locationf_sx_open_zfs
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_open_zfs
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
Gets an individual <code>locationf_sx_open_zfs</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_open_zfs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>locationf_sx_open_zfs</td></tr>
<tr><td><b>Id</b></td><td><code>aws.datasync.locationf_sx_open_zfs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>fsx_filesystem_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx OpenZFS file system.</td></tr>
<tr><td><code>security_group_arns</code></td><td><code>array</code></td><td>The ARNs of the security groups that are to use to configure the FSx OpenZFS file system.</td></tr>
<tr><td><code>protocol</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>A subdirectory in the location's path.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx OpenZFS file system location that is created.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the FSx OpenZFS that was described.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
fsx_filesystem_arn,
security_group_arns,
protocol,
subdirectory,
tags,
location_arn,
location_uri
FROM aws.datasync.locationf_sx_open_zfs
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;LocationArn&gt;'
```

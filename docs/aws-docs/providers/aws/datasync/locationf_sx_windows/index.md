---
title: locationf_sx_windows
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_windows
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
Gets an individual <code>locationf_sx_windows</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_windows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.datasync.locationf_sx_windows</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Domain</code></td><td><code>string</code></td><td>The name of the Windows domain that the FSx for Windows server belongs to.</td></tr><tr><td><code>FsxFilesystemArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx for Windows file system.</td></tr><tr><td><code>Password</code></td><td><code>string</code></td><td>The password of the user who has the permissions to access files and folders in the FSx for Windows file system.</td></tr><tr><td><code>SecurityGroupArns</code></td><td><code>array</code></td><td>The ARNs of the security groups that are to use to configure the FSx for Windows file system.</td></tr><tr><td><code>Subdirectory</code></td><td><code>string</code></td><td>A subdirectory in the location's path.</td></tr><tr><td><code>User</code></td><td><code>string</code></td><td>The user who has the permissions to access files and folders in the FSx for Windows file system.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>LocationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx for Windows file system location that is created.</td></tr><tr><td><code>LocationUri</code></td><td><code>string</code></td><td>The URL of the FSx for Windows location that was described.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.datasync.locationf_sx_windows
WHERE region = 'us-east-1' AND data__Identifier = '{LocationArn}'
</pre>

---
title: file_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - file_systems
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
Retrieves a list of <code>file_systems</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>file_systems</td></tr>
<tr><td><b>Id</b></td><td><code>aws.efs.file_systems</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FileSystemId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Encrypted</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>FileSystemTags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LifecyclePolicies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>PerformanceMode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProvisionedThroughputInMibps</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>ThroughputMode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>FileSystemPolicy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>BypassPolicyLockoutSafetyCheck</code></td><td><code>boolean</code></td><td>Whether to bypass the FileSystemPolicy lockout safety check. The policy lockout safety check determines whether the policy in the request will prevent the principal making the request to be locked out from making future PutFileSystemPolicy requests on the file system. Set BypassPolicyLockoutSafetyCheck to True only when you intend to prevent the principal that is making the request from making a subsequent PutFileSystemPolicy request on the file system. Defaults to false</td></tr>
<tr><td><code>BackupPolicy</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AvailabilityZoneName</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.efs.file_systems<br/>WHERE region = 'us-east-1'
</pre>

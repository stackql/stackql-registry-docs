---
title: file_system
hide_title: false
hide_table_of_contents: false
keywords:
  - file_system
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
Gets an individual <code>file_system</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_system</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>file_system</td></tr>
<tr><td><b>Id</b></td><td><code>aws.efs.file_system</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>file_system_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>encrypted</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>file_system_tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>lifecycle_policies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>performance_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>provisioned_throughput_in_mibps</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>throughput_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>file_system_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>bypass_policy_lockout_safety_check</code></td><td><code>boolean</code></td><td>Whether to bypass the FileSystemPolicy lockout safety check. The policy lockout safety check determines whether the policy in the request will prevent the principal making the request to be locked out from making future PutFileSystemPolicy requests on the file system. Set BypassPolicyLockoutSafetyCheck to True only when you intend to prevent the principal that is making the request from making a subsequent PutFileSystemPolicy request on the file system. Defaults to false</td></tr>
<tr><td><code>backup_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>availability_zone_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
file_system_id,
arn,
encrypted,
file_system_tags,
kms_key_id,
lifecycle_policies,
performance_mode,
provisioned_throughput_in_mibps,
throughput_mode,
file_system_policy,
bypass_policy_lockout_safety_check,
backup_policy,
availability_zone_name
FROM aws.efs.file_system
WHERE region = 'us-east-1'
AND data__Identifier = '<FileSystemId>'
```

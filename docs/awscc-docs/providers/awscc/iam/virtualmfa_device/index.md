---
title: virtualmfa_device
hide_title: false
hide_table_of_contents: false
keywords:
  - virtualmfa_device
  - iam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>virtualmfa_device</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtualmfa_device</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>virtualmfa_device</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.virtualmfa_device</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>virtual_mfa_device_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>serial_number</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>users</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>virtualmfa_device</code> resource, the following permissions are required:

### Read
<pre>
iam:ListVirtualMFADevices</pre>

### Update
<pre>
iam:TagMFADevice,
iam:UntagMFADevice</pre>

### Delete
<pre>
iam:DeleteVirtualMFADevice,
iam:DeactivateMFADevice</pre>


## Example
```sql
SELECT
region,
virtual_mfa_device_name,
path,
serial_number,
users,
tags
FROM awscc.iam.virtualmfa_device
WHERE data__Identifier = '&lt;SerialNumber&gt;'
```

---
title: virtualmfa_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - virtualmfa_devices
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
Retrieves a list of <code>virtualmfa_devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtualmfa_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>virtualmfa_devices</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iam.virtualmfa_devices</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>serial_number</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>virtualmfa_devices</code> resource, the following permissions are required:

### Create
<pre>
iam:CreateVirtualMFADevice,
iam:EnableMFADevice,
iam:ListVirtualMFADevices</pre>

### List
<pre>
iam:ListVirtualMFADevices</pre>


## Example
```sql
SELECT
region,
serial_number
FROM awscc.iam.virtualmfa_devices

```
---
title: hypervisor
hide_title: false
hide_table_of_contents: false
keywords:
  - hypervisor
  - backupgateway
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>hypervisor</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hypervisor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hypervisor</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.backupgateway.hypervisor</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>host</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>hypervisor_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_group_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>password</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>username</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>hypervisor</code> resource, the following permissions are required:

### Read
<pre>
backup-gateway:GetHypervisor,
backup-gateway:ListHypervisors</pre>

### Update
<pre>
backup-gateway:UpdateHypervisor,
backup-gateway:GetHypervisor,
backup-gateway:ListHypervisors,
backup-gateway:ImportHypervisorConfiguration,
backup-gateway:DeleteHypervisor</pre>

### Delete
<pre>
backup-gateway:DeleteHypervisor,
backup-gateway:GetHypervisor,
backup-gateway:ListHypervisors</pre>


## Example
```sql
SELECT
region,
host,
hypervisor_arn,
kms_key_arn,
log_group_arn,
name,
password,
tags,
username
FROM awscc.backupgateway.hypervisor
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;HypervisorArn&gt;'
```

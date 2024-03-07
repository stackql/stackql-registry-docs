---
title: hypervisors
hide_title: false
hide_table_of_contents: false
keywords:
  - hypervisors
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
Retrieves a list of <code>hypervisors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hypervisors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hypervisors</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.backupgateway.hypervisors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>hypervisor_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>hypervisors</code> resource, the following permissions are required:

### Create
```json
backup-gateway:ImportHypervisorConfiguration,
backup-gateway:GetHypervisor,
backup-gateway:ListHypervisors,
backup-gateway:TagResource,
kms:CreateGrant,
kms:Encrypt,
kms:Decrypt
```

### List
```json
backup-gateway:ListHypervisors
```


## Example
```sql
SELECT
region,
hypervisor_arn
FROM awscc.backupgateway.hypervisors
WHERE region = 'us-east-1'
```

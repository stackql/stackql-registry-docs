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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>hypervisor</code> resource, use <code>hypervisors</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hypervisor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::BackupGateway::Hypervisor Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backupgateway.hypervisor" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="host" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="hypervisor_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="log_group_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="password" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="username" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.backupgateway.hypervisor
WHERE data__Identifier = '<HypervisorArn>';
```

## Permissions

To operate on the <code>hypervisor</code> resource, the following permissions are required:

### Read
```json
backup-gateway:GetHypervisor,
backup-gateway:ListHypervisors
```

### Update
```json
backup-gateway:UpdateHypervisor,
backup-gateway:GetHypervisor,
backup-gateway:ListHypervisors,
backup-gateway:ImportHypervisorConfiguration,
backup-gateway:DeleteHypervisor
```

### Delete
```json
backup-gateway:DeleteHypervisor,
backup-gateway:GetHypervisor,
backup-gateway:ListHypervisors
```


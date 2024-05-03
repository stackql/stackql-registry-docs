---
title: ip_set
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_set
  - guardduty
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

Gets or operates on an individual <code>ip_set</code> resource, use <code>ip_sets</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GuardDuty::IPSet</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.ip_set" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="format" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="activate" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="location" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
id,
format,
activate,
detector_id,
name,
location,
tags
FROM aws.guardduty.ip_set
WHERE data__Identifier = '<Id>|<DetectorId>';
```

## Permissions

To operate on the <code>ip_set</code> resource, the following permissions are required:

### Read
```json
guardduty:GetIPSet
```

### Delete
```json
guardduty:GetDetector,
guardduty:ListDetectors,
guardduty:ListIPSets,
guardduty:GetIPSet,
guardduty:DeleteIPSet,
iam:DeleteRolePolicy
```

### Update
```json
guardduty:UpdateIPSet,
guardduty:GetIPSet,
guardduty:ListIPSets,
iam:PutRolePolicy
```


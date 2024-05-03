---
title: detector
hide_title: false
hide_table_of_contents: false
keywords:
  - detector
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

Gets or operates on an individual <code>detector</code> resource, use <code>detectors</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GuardDuty::Detector</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.detector" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="finding_publishing_frequency" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="data_sources" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="features" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
finding_publishing_frequency,
enable,
data_sources,
features,
id,
tags
FROM aws.guardduty.detector
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>detector</code> resource, the following permissions are required:

### Read
```json
guardduty:GetDetector
```

### Delete
```json
guardduty:ListDetectors,
guardduty:DeleteDetector,
guardduty:GetDetector
```

### Update
```json
guardduty:UpdateDetector,
guardduty:GetDetector,
guardduty:ListDetectors,
iam:CreateServiceLinkedRole,
iam:GetRole
```


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
Gets an individual <code>detector</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GuardDuty::Detector</td></tr>
<tr><td><b>Id</b></td><td><code>aws.guardduty.detector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>finding_publishing_frequency</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>data_sources</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>features</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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


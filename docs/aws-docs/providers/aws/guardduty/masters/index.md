---
title: masters
hide_title: false
hide_table_of_contents: false
keywords:
  - masters
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
Retrieves a list of <code>masters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>masters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>GuardDuty Master resource schema</td></tr>
<tr><td><b>Id</b></td><td><code>aws.guardduty.masters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>detector_id</code></td><td><code>string</code></td><td>Unique ID of the detector of the GuardDuty member account.</td></tr>
<tr><td><code>master_id</code></td><td><code>string</code></td><td>ID of the account used as the master account.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
detector_id,
master_id
FROM aws.guardduty.masters
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>masters</code> resource, the following permissions are required:

### Create
```json
guardduty:ListInvitations,
guardduty:AcceptInvitation,
guardduty:GetMasterAccount
```

### List
```json
guardduty:GetMasterAccount
```


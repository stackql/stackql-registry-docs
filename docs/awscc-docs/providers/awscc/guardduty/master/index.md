---
title: master
hide_title: false
hide_table_of_contents: false
keywords:
  - master
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
Gets an individual <code>master</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>master</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>master</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.guardduty.master</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>master_id</code></td><td><code>string</code></td><td>ID of the account used as the master account.</td></tr>
<tr><td><code>invitation_id</code></td><td><code>string</code></td><td>Value used to validate the master account to the member account.</td></tr>
<tr><td><code>detector_id</code></td><td><code>string</code></td><td>Unique ID of the detector of the GuardDuty member account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
master_id,
invitation_id,
detector_id
FROM awscc.guardduty.master
WHERE data__Identifier = '<DetectorId>|<MasterId>';
```

## Permissions

To operate on the <code>master</code> resource, the following permissions are required:

### Read
```json
guardduty:GetMasterAccount
```

### Delete
```json
guardduty:DisassociateFromMasterAccount
```


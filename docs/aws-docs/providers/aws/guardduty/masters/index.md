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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>masters</code> in a region or to create or delete a <code>masters</code> resource, use <code>master</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>masters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>GuardDuty Master resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.masters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td>Unique ID of the detector of the GuardDuty member account.</td></tr>
<tr><td><CopyableCode code="master_id" /></td><td><code>string</code></td><td>ID of the account used as the master account.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
detector_id,
master_id
FROM aws.guardduty.masters
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "MasterId": "{{ MasterId }}",
 "DetectorId": "{{ DetectorId }}"
}
>>>
--required properties only
INSERT INTO aws.guardduty.masters (
 MasterId,
 DetectorId,
 region
)
SELECT 
{{ MasterId }},
 {{ DetectorId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "MasterId": "{{ MasterId }}",
 "InvitationId": "{{ InvitationId }}",
 "DetectorId": "{{ DetectorId }}"
}
>>>
--all properties
INSERT INTO aws.guardduty.masters (
 MasterId,
 InvitationId,
 DetectorId,
 region
)
SELECT 
 {{ MasterId }},
 {{ InvitationId }},
 {{ DetectorId }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.guardduty.masters
WHERE data__Identifier = '<DetectorId|MasterId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>masters</code> resource, the following permissions are required:

### Create
```json
guardduty:ListInvitations,
guardduty:AcceptInvitation,
guardduty:GetMasterAccount
```

### Delete
```json
guardduty:DisassociateFromMasterAccount
```

### List
```json
guardduty:GetMasterAccount
```


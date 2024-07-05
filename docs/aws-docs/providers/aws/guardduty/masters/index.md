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

Creates, updates, deletes or gets a <code>master</code> resource or lists <code>masters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>masters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>GuardDuty Master resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.guardduty.masters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="master_id" /></td><td><code>string</code></td><td>ID of the account used as the master account.</td></tr>
<tr><td><CopyableCode code="invitation_id" /></td><td><code>string</code></td><td>Value used to validate the master account to the member account.</td></tr>
<tr><td><CopyableCode code="detector_id" /></td><td><code>string</code></td><td>Unique ID of the detector of the GuardDuty member account.</td></tr>
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
    <td><CopyableCode code="MasterId, DetectorId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>masters</code> in a region.
```sql
SELECT
region,
master_id,
invitation_id,
detector_id
FROM aws.guardduty.masters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>master</code>.
```sql
SELECT
region,
master_id,
invitation_id,
detector_id
FROM aws.guardduty.masters
WHERE region = 'us-east-1' AND data__Identifier = '<DetectorId>|<MasterId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>master</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.guardduty.masters (
 MasterId,
 DetectorId,
 region
)
SELECT 
'{{ MasterId }}',
 '{{ DetectorId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.guardduty.masters (
 MasterId,
 InvitationId,
 DetectorId,
 region
)
SELECT 
 '{{ MasterId }}',
 '{{ InvitationId }}',
 '{{ DetectorId }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: master
    props:
      - name: MasterId
        value: '{{ MasterId }}'
      - name: InvitationId
        value: '{{ InvitationId }}'
      - name: DetectorId
        value: '{{ DetectorId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
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


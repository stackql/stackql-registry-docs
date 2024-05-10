---
title: backup_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_plans
  - backup
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


Used to retrieve a list of <code>backup_plans</code> in a region or to create or delete a <code>backup_plans</code> resource, use <code>backup_plan</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Backup::BackupPlan</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.backup_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="backup_plan_id" /></td><td><code>string</code></td><td></td></tr>
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
backup_plan_id
FROM aws.backup.backup_plans
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
 "BackupPlan": {
  "BackupPlanName": "{{ BackupPlanName }}",
  "AdvancedBackupSettings": [
   {
    "BackupOptions": {},
    "ResourceType": "{{ ResourceType }}"
   }
  ],
  "BackupPlanRule": [
   {
    "RuleName": "{{ RuleName }}",
    "TargetBackupVault": "{{ TargetBackupVault }}",
    "StartWindowMinutes": null,
    "CompletionWindowMinutes": null,
    "ScheduleExpression": "{{ ScheduleExpression }}",
    "ScheduleExpressionTimezone": "{{ ScheduleExpressionTimezone }}",
    "RecoveryPointTags": {},
    "CopyActions": [
     {
      "Lifecycle": {
       "MoveToColdStorageAfterDays": null,
       "DeleteAfterDays": null,
       "OptInToArchiveForSupportedResources": "{{ OptInToArchiveForSupportedResources }}"
      },
      "DestinationBackupVaultArn": "{{ DestinationBackupVaultArn }}"
     }
    ],
    "Lifecycle": null,
    "EnableContinuousBackup": "{{ EnableContinuousBackup }}"
   }
  ]
 }
}
>>>
--required properties only
INSERT INTO aws.backup.backup_plans (
 BackupPlan,
 region
)
SELECT 
{{ .BackupPlan }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "BackupPlan": {
  "BackupPlanName": "{{ BackupPlanName }}",
  "AdvancedBackupSettings": [
   {
    "BackupOptions": {},
    "ResourceType": "{{ ResourceType }}"
   }
  ],
  "BackupPlanRule": [
   {
    "RuleName": "{{ RuleName }}",
    "TargetBackupVault": "{{ TargetBackupVault }}",
    "StartWindowMinutes": null,
    "CompletionWindowMinutes": null,
    "ScheduleExpression": "{{ ScheduleExpression }}",
    "ScheduleExpressionTimezone": "{{ ScheduleExpressionTimezone }}",
    "RecoveryPointTags": {},
    "CopyActions": [
     {
      "Lifecycle": {
       "MoveToColdStorageAfterDays": null,
       "DeleteAfterDays": null,
       "OptInToArchiveForSupportedResources": "{{ OptInToArchiveForSupportedResources }}"
      },
      "DestinationBackupVaultArn": "{{ DestinationBackupVaultArn }}"
     }
    ],
    "Lifecycle": null,
    "EnableContinuousBackup": "{{ EnableContinuousBackup }}"
   }
  ]
 },
 "BackupPlanTags": {}
}
>>>
--all properties
INSERT INTO aws.backup.backup_plans (
 BackupPlan,
 BackupPlanTags,
 region
)
SELECT 
 {{ .BackupPlan }},
 {{ .BackupPlanTags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.backup.backup_plans
WHERE data__Identifier = '<BackupPlanId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>backup_plans</code> resource, the following permissions are required:

### Create
```json
backup:GetBackupPlan,
backup:TagResource,
backup:CreateBackupPlan
```

### Delete
```json
backup:GetBackupPlan,
backup:DeleteBackupPlan
```

### List
```json
backup:ListBackupPlans
```


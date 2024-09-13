
---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
  - logging
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>bucket</code> resource or lists <code>buckets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.buckets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the bucket.For example:projects/my-project/locations/global/buckets/my-bucketFor a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support)For the location of global it is unspecified where log entries are actually stored.After a bucket has been created, the location cannot be changed. |
| <CopyableCode code="description" /> | `string` | Optional. Describes this bucket. |
| <CopyableCode code="analyticsEnabled" /> | `boolean` | Whether log analytics is enabled for this bucket.Once enabled, log analytics features cannot be disabled. |
| <CopyableCode code="cmekSettings" /> | `object` | Describes the customer-managed encryption key (CMEK) settings associated with a project, folder, organization, billing account, or flexible resource.Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.See Enabling CMEK for Log Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of the bucket. This is not set for any of the default buckets. |
| <CopyableCode code="indexConfigs" /> | `array` | Optional. A list of indexed fields and related configuration data. |
| <CopyableCode code="lifecycleState" /> | `string` | Output only. The bucket lifecycle state. |
| <CopyableCode code="locked" /> | `boolean` | Optional. Whether the bucket is locked.The retention period on a locked bucket cannot be changed. Locked buckets may only be deleted if they are empty. |
| <CopyableCode code="restrictedFields" /> | `array` | Optional. Log entry field paths that are denied access in this bucket.The following fields and their children are eligible: textPayload, jsonPayload, protoPayload, httpRequest, labels, sourceLocation.Restricting a repeated field will restrict all values. Adding a parent will block all child fields. (e.g. foo.bar will block foo.bar.baz) |
| <CopyableCode code="retentionDays" /> | `integer` | Optional. Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of the bucket. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_buckets_get" /> | `SELECT` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Gets a log bucket. |
| <CopyableCode code="billing_accounts_locations_buckets_list" /> | `SELECT` | <CopyableCode code="billingAccountsId, locationsId" /> | Lists log buckets. |
| <CopyableCode code="folders_locations_buckets_get" /> | `SELECT` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Gets a log bucket. |
| <CopyableCode code="folders_locations_buckets_list" /> | `SELECT` | <CopyableCode code="foldersId, locationsId" /> | Lists log buckets. |
| <CopyableCode code="locations_buckets_list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Lists log buckets. |
| <CopyableCode code="organizations_locations_buckets_get" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Gets a log bucket. |
| <CopyableCode code="organizations_locations_buckets_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists log buckets. |
| <CopyableCode code="projects_locations_buckets_get" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Gets a log bucket. |
| <CopyableCode code="projects_locations_buckets_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists log buckets. |
| <CopyableCode code="billing_accounts_locations_buckets_create" /> | `INSERT` | <CopyableCode code="billingAccountsId, locationsId" /> | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="folders_locations_buckets_create" /> | `INSERT` | <CopyableCode code="foldersId, locationsId" /> | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="locations_buckets_create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="organizations_locations_buckets_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="projects_locations_buckets_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="billing_accounts_locations_buckets_delete" /> | `DELETE` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Deletes a log bucket.Changes the bucket's lifecycle_state to the DELETE_REQUESTED state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |
| <CopyableCode code="folders_locations_buckets_delete" /> | `DELETE` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Deletes a log bucket.Changes the bucket's lifecycle_state to the DELETE_REQUESTED state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |
| <CopyableCode code="organizations_locations_buckets_delete" /> | `DELETE` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Deletes a log bucket.Changes the bucket's lifecycle_state to the DELETE_REQUESTED state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |
| <CopyableCode code="projects_locations_buckets_delete" /> | `DELETE` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Deletes a log bucket.Changes the bucket's lifecycle_state to the DELETE_REQUESTED state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |
| <CopyableCode code="billing_accounts_locations_buckets_patch" /> | `UPDATE` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Updates a log bucket.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="folders_locations_buckets_patch" /> | `UPDATE` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Updates a log bucket.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="organizations_locations_buckets_patch" /> | `UPDATE` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Updates a log bucket.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="projects_locations_buckets_patch" /> | `UPDATE` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Updates a log bucket.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="billing_accounts_locations_buckets_undelete" /> | `EXEC` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |
| <CopyableCode code="folders_locations_buckets_undelete" /> | `EXEC` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |
| <CopyableCode code="locations_buckets_undelete" /> | `EXEC` | <CopyableCode code="name" /> | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |
| <CopyableCode code="organizations_locations_buckets_undelete" /> | `EXEC` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |
| <CopyableCode code="projects_locations_buckets_undelete" /> | `EXEC` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |

## `SELECT` examples

Lists log buckets.

```sql
SELECT
name,
description,
analyticsEnabled,
cmekSettings,
createTime,
indexConfigs,
lifecycleState,
locked,
restrictedFields,
retentionDays,
updateTime
FROM google.logging.buckets
WHERE parent = '{{ parent }}'
AND parentType = '{{ parentType }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>buckets</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.logging.buckets (
parent,
parentType,
name,
description,
createTime,
updateTime,
retentionDays,
locked,
lifecycleState,
analyticsEnabled,
restrictedFields,
indexConfigs,
cmekSettings
)
SELECT 
'{{ parent }}',
'{{ parentType }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ retentionDays }}',
true|false,
'{{ lifecycleState }}',
true|false,
'{{ restrictedFields }}',
'{{ indexConfigs }}',
'{{ cmekSettings }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: retentionDays
        value: '{{ retentionDays }}'
      - name: locked
        value: '{{ locked }}'
      - name: lifecycleState
        value: '{{ lifecycleState }}'
      - name: analyticsEnabled
        value: '{{ analyticsEnabled }}'
      - name: restrictedFields
        value: '{{ restrictedFields }}'
      - name: indexConfigs
        value: '{{ indexConfigs }}'
      - name: cmekSettings
        value: '{{ cmekSettings }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a bucket only if the necessary resources are available.

```sql
UPDATE google.logging.buckets
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
retentionDays = '{{ retentionDays }}',
locked = true|false,
lifecycleState = '{{ lifecycleState }}',
analyticsEnabled = true|false,
restrictedFields = '{{ restrictedFields }}',
indexConfigs = '{{ indexConfigs }}',
cmekSettings = '{{ cmekSettings }}'
WHERE 
bucketsId = '{{ bucketsId }}'
AND foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}';
```

## `DELETE` example

Deletes the specified bucket resource.

```sql
DELETE FROM google.logging.buckets
WHERE bucketsId = '{{ bucketsId }}'
AND foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}';
```

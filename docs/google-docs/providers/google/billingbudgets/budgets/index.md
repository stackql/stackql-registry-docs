---
title: budgets
hide_title: false
hide_table_of_contents: false
keywords:
  - budgets
  - billingbudgets
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

Creates, updates, deletes, gets or lists a <code>budgets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>budgets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.billingbudgets.budgets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the budget. The resource name implies the scope of a budget. Values are of the form `billingAccounts/{billingAccountId}/budgets/{budgetId}`. |
| <CopyableCode code="amount" /> | `object` | The budgeted amount for each usage period. |
| <CopyableCode code="budgetFilter" /> | `object` | A filter for a budget, limiting the scope of the cost to calculate. |
| <CopyableCode code="displayName" /> | `string` | User data for display name in UI. The name must be less than or equal to 60 characters. |
| <CopyableCode code="etag" /> | `string` | Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag causes an update to overwrite other changes. |
| <CopyableCode code="notificationsRule" /> | `object` | NotificationsRule defines notifications that are sent based on budget spend and thresholds. |
| <CopyableCode code="ownershipScope" /> | `string` |  |
| <CopyableCode code="thresholdRules" /> | `array` | Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget. Optional for `pubsubTopic` notifications. Required if using email notifications. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountsId, budgetsId" /> | Returns a budget. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountsId" /> | Returns a list of budgets for a billing account. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="billingAccountsId" /> | Creates a new budget. See [Quotas and limits](https://cloud.google.com/billing/quotas) for more information on the limits of the number of budgets you can create. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="billingAccountsId, budgetsId" /> | Deletes a budget. Returns successfully if already deleted. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="billingAccountsId, budgetsId" /> | Updates a budget and returns the updated budget. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. Budget fields that are not exposed in this API will not be changed by this method. |

## `SELECT` examples

Returns a list of budgets for a billing account. WARNING: There are some fields exposed on the Google Cloud Console that aren't available on this API. When reading from the API, you will not see these fields in the return value, though they may have been set in the Cloud Console.

```sql
SELECT
name,
amount,
budgetFilter,
displayName,
etag,
notificationsRule,
ownershipScope,
thresholdRules
FROM google.billingbudgets.budgets
WHERE billingAccountsId = '{{ billingAccountsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>budgets</code> resource.

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
INSERT INTO google.billingbudgets.budgets (
billingAccountsId,
amount,
etag,
budgetFilter,
notificationsRule,
thresholdRules,
displayName,
ownershipScope
)
SELECT 
'{{ billingAccountsId }}',
'{{ amount }}',
'{{ etag }}',
'{{ budgetFilter }}',
'{{ notificationsRule }}',
'{{ thresholdRules }}',
'{{ displayName }}',
'{{ ownershipScope }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
amount:
  specifiedAmount:
    nanos: integer
    currencyCode: string
    units: string
  lastPeriodAmount: {}
etag: string
budgetFilter:
  projects:
    - type: string
  services:
    - type: string
  resourceAncestors:
    - type: string
  calendarPeriod: string
  subaccounts:
    - type: string
  labels: object
  customPeriod:
    endDate:
      year: integer
      month: integer
      day: integer
  creditTypes:
    - type: string
  creditTypesTreatment: string
notificationsRule:
  schemaVersion: string
  enableProjectLevelRecipients: boolean
  pubsubTopic: string
  disableDefaultIamRecipients: boolean
  monitoringNotificationChannels:
    - type: string
thresholdRules:
  - thresholdPercent: number
    spendBasis: string
displayName: string
ownershipScope: string
name: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>budgets</code> resource.

```sql
/*+ update */
UPDATE google.billingbudgets.budgets
SET 
amount = '{{ amount }}',
etag = '{{ etag }}',
budgetFilter = '{{ budgetFilter }}',
notificationsRule = '{{ notificationsRule }}',
thresholdRules = '{{ thresholdRules }}',
displayName = '{{ displayName }}',
ownershipScope = '{{ ownershipScope }}'
WHERE 
billingAccountsId = '{{ billingAccountsId }}'
AND budgetsId = '{{ budgetsId }}';
```

## `DELETE` example

Deletes the specified <code>budgets</code> resource.

```sql
/*+ delete */
DELETE FROM google.billingbudgets.budgets
WHERE billingAccountsId = '{{ billingAccountsId }}'
AND budgetsId = '{{ budgetsId }}';
```

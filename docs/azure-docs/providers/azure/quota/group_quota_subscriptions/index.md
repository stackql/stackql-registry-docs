---
title: group_quota_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_subscriptions
  - quota
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

Creates, updates, deletes, gets or lists a <code>group_quota_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_quota_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId, subscriptionId" /> | Returns the subscriptionIds along with its provisioning state for being associated with the GroupQuota. If the subscription is not a member of GroupQuota, it will return 404, else 200. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Returns a list of the subscriptionIds associated with the GroupQuotas. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupQuotaName, managementGroupId, subscriptionId" /> | Adds a subscription to GroupQuotas. The subscriptions will be validated based on the additionalAttributes defined in the GroupQuota. The additionalAttributes works as filter for the subscriptions, which can be included in the GroupQuotas. The request's TenantId is validated against the subscription's TenantId. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupQuotaName, managementGroupId, subscriptionId" /> | Removes the subscription from GroupQuotas. The request's TenantId is validated against the subscription's TenantId. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupQuotaName, managementGroupId, subscriptionId" /> | Updates the GroupQuotas with the subscription to add to the subscriptions list. The subscriptions will be validated if additionalAttributes are defined in the GroupQuota. The request's TenantId is validated against the subscription's TenantId. |

## `SELECT` examples

Returns a list of the subscriptionIds associated with the GroupQuotas.


```sql
SELECT
properties
FROM azure.quota.group_quota_subscriptions
WHERE groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>group_quota_subscriptions</code> resource.

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
INSERT INTO azure.quota.group_quota_subscriptions (
groupQuotaName,
managementGroupId,
subscriptionId
)
SELECT 
'{{ groupQuotaName }}',
'{{ managementGroupId }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>group_quota_subscriptions</code> resource.

```sql
/*+ update */
UPDATE azure.quota.group_quota_subscriptions
SET 

WHERE 
groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>group_quota_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.quota.group_quota_subscriptions
WHERE groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```

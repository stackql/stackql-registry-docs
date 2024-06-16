---
title: group_quota_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_subscriptions
  - quota
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_quota_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_subscriptions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId, subscriptionId" /> | Returns the subscriptionIds along with its provisioning state for being associated with the GroupQuota. If the subscription is not a member of GroupQuota, it will return 404, else 200. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Returns a list of the subscriptionIds associated with the GroupQuotas. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupQuotaName, managementGroupId, subscriptionId" /> | Adds a subscription to GroupQuotas. The subscriptions will be validated based on the additionalAttributes defined in the GroupQuota. The additionalAttributes works as filter for the subscriptions, which can be included in the GroupQuotas. The request's TenantId is validated against the subscription's TenantId. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupQuotaName, managementGroupId, subscriptionId" /> | Removes the subscription from GroupQuotas. The request's TenantId is validated against the subscription's TenantId. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="groupQuotaName, managementGroupId, subscriptionId" /> | Updates the GroupQuotas with the subscription to add to the subscriptions list. The subscriptions will be validated if additionalAttributes are defined in the GroupQuota. The request's TenantId is validated against the subscription's TenantId. |

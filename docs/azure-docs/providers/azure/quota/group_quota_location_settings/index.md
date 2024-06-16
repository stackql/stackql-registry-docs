---
title: group_quota_location_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_location_settings
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
<tr><td><b>Name</b></td><td><code>group_quota_location_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_location_settings" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupQuotaName, location, managementGroupId, resourceProviderName" /> | Gets the GroupQuotas enforcement settings for the ResourceProvider/location. The locations, where GroupQuota enforcement is not enabled will return Not Found. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId, resourceProviderName" /> | Returns only the list of the Azure regions settings, where the GroupQuotas enforcement is enabled. The locations not included in GroupQuota Enforcement will not be listed, the regions in failed status with listed as status Failed. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupQuotaName, location, managementGroupId, resourceProviderName" /> | Enables the GroupQuotas enforcement for the resource provider and the location specified. The resource provider will start using the group quotas as the overall quota for the subscriptions included in the GroupQuota. The subscriptions cannot request quota at subscription level.<br />The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource - provider/location/resource.<br />Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To disable GroupQuota Enforcement -<br /> 1. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions (Check the example - GroupQuotaSubscriptions_Delete).<br /> 2. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete). |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="groupQuotaName, location, managementGroupId, resourceProviderName" /> | Enables the GroupQuotas enforcement for the resource provider and the location specified. The resource provider will start using the group quotas as the overall quota for the subscriptions included in the GroupQuota. The subscriptions cannot request quota at subscription level.<br />The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource - provider/location/resource.<br />Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To disable GroupQuota Enforcement -<br /> 1. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions (Check the example - GroupQuotaSubscriptions_Delete).<br /> 2. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete). |

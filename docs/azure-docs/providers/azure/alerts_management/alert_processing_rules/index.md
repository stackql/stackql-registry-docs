---
title: alert_processing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_processing_rules
  - alerts_management
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
<tr><td><b>Name</b></td><td><code>alert_processing_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.alert_processing_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Alert processing rule properties defining scopes, conditions and scheduling logic for alert processing rule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all alert processing rules in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all alert processing rules in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="alertProcessingRuleName, resourceGroupName, subscriptionId" /> | Create or update an alert processing rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="alertProcessingRuleName, resourceGroupName, subscriptionId" /> | Delete an alert processing rule. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all alert processing rules in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all alert processing rules in a subscription. |
| <CopyableCode code="get_by_name" /> | `EXEC` | <CopyableCode code="alertProcessingRuleName, resourceGroupName, subscriptionId" /> | Get an alert processing rule by name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="alertProcessingRuleName, resourceGroupName, subscriptionId" /> | Enable, disable, or update tags for an alert processing rule. |

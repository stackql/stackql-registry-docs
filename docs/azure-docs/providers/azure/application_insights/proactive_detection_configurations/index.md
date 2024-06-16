---
title: proactive_detection_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - proactive_detection_configurations
  - application_insights
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
<tr><td><b>Name</b></td><td><code>proactive_detection_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.proactive_detection_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="CustomEmails" /> | `array` | Custom email addresses for this rule notifications |
| <CopyableCode code="Enabled" /> | `boolean` | A flag that indicates whether this rule is enabled by the user |
| <CopyableCode code="LastUpdatedTime" /> | `string` | The last time this rule was updated |
| <CopyableCode code="Name" /> | `string` | The rule name |
| <CopyableCode code="RuleDefinitions" /> | `object` | Static definitions of the ProactiveDetection configuration rule (same values for all components). |
| <CopyableCode code="SendEmailsToSubscriptionOwners" /> | `boolean` | A flag that indicated whether notifications on this rule should be sent to subscription owners |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ConfigurationId, resourceGroupName, resourceName, subscriptionId" /> | Get the ProactiveDetection configuration for this configuration id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of ProactiveDetection configurations of an Application Insights component. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="ConfigurationId, resourceGroupName, resourceName, subscriptionId" /> | Update the ProactiveDetection configuration for this configuration id. |

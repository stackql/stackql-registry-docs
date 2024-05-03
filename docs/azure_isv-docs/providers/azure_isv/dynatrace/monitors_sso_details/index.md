---
title: monitors_sso_details
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_sso_details
  - dynatrace
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors_sso_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_sso_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aadDomains" /> | `array` | array of Aad(azure active directory) domains |
| <CopyableCode code="adminUsers" /> | `array` | Array of admin user emails. |
| <CopyableCode code="isSsoEnabled" /> | `string` | Indicates whether SSO is enabled or not |
| <CopyableCode code="metadataUrl" /> | `string` | URL for Azure AD metadata |
| <CopyableCode code="singleSignOnUrl" /> | `string` | The login URL specific to this Dynatrace Environment |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__userPrincipal" /> |

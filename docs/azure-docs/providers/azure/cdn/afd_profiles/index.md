---
title: afd_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_profiles
  - cdn
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
<tr><td><b>Name</b></td><td><code>afd_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_profiles" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_endpoint_name_availability" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId, data__name, data__type" /> | Check the availability of an afdx endpoint name, and return the globally unique endpoint host name. |
| <CopyableCode code="check_host_name_availability" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId, data__hostName" /> | Validates the custom domain mapping to ensure it maps to the correct Azure Front Door endpoint in DNS. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId, data__wafMappingList" /> | Upgrade a profile from Standard_AzureFrontDoor to Premium_AzureFrontDoor. |
| <CopyableCode code="validate_secret" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId, data__secretSource, data__secretType" /> | Validate a Secret in the profile. |

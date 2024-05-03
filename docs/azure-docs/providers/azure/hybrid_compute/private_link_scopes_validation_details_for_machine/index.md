---
title: private_link_scopes_validation_details_for_machine
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scopes_validation_details_for_machine
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>private_link_scopes_validation_details_for_machine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.private_link_scopes_validation_details_for_machine" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="connectionDetails" /> | `array` | List of Private Endpoint Connection details. |
| <CopyableCode code="publicNetworkAccess" /> | `string` | The network access policy to determine if Azure Arc agents can use public Azure Arc service endpoints. Defaults to disabled (access to Azure Arc services only via private link). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> |

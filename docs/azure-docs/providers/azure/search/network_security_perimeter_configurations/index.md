---
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - search
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
<tr><td><b>Name</b></td><td><code>network_security_perimeter_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.network_security_perimeter_configurations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="nspConfigName, resourceGroupName, searchServiceName, subscriptionId" /> | Gets a network security perimeter configuration. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Gets a list of network security perimeter configurations for a search service. |
| <CopyableCode code="reconcile" /> | `EXEC` | <CopyableCode code="nspConfigName, resourceGroupName, searchServiceName, subscriptionId" /> | Reconcile network security perimeter configuration for the Azure AI Search resource provider. This triggers a manual resync with network security perimeter configurations by ensuring the search service carries the latest configuration. |

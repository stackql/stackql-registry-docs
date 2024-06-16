---
title: registry_environment_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_environment_versions
  - ml_services
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
<tr><td><b>Name</b></td><td><code>registry_environment_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.registry_environment_versions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, registryName, resourceGroupName, subscriptionId, version" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, registryName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, registryName, resourceGroupName, subscriptionId, version, data__properties" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, registryName, resourceGroupName, subscriptionId, version" /> |

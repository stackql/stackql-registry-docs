---
title: cluster_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_versions
  - service_fabric
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
<tr><td><b>Name</b></td><td><code>cluster_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric.cluster_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identification of the result |
| <CopyableCode code="name" /> | `string` | The name of the result |
| <CopyableCode code="properties" /> | `object` | The detail of the Service Fabric runtime version result |
| <CopyableCode code="type" /> | `string` | The result resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, clusterVersion, location, subscriptionId" /> | Gets information about an available Service Fabric cluster code version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, location, subscriptionId" /> | Gets all available code versions for Service Fabric cluster resources by location. |
| <CopyableCode code="list_by_environment" /> | `SELECT` | <CopyableCode code="api-version, environment, location, subscriptionId" /> | Gets all available code versions for Service Fabric cluster resources by environment. |
| <CopyableCode code="get_by_environment" /> | `EXEC` | <CopyableCode code="api-version, clusterVersion, environment, location, subscriptionId" /> | Gets information about an available Service Fabric cluster code version by environment. |

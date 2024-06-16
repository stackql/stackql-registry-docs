---
title: build_service_build
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_build
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>build_service_build</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_build" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Get a KPack build. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Create or update a KPack build. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | delete a KPack build. |

---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
  - hdinsight
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.configurations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets all configuration information for an HDI cluster. |
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="clusterName, configurationName, resourceGroupName, subscriptionId" /> | The configuration object for the specified cluster. This API is not recommended and might be removed in the future. Please consider using List configurations API instead. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, configurationName, resourceGroupName, subscriptionId" /> | Configures the HTTP settings on the specified cluster. This API is deprecated, please use UpdateGatewaySettings in cluster endpoint instead. |

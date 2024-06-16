---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - mongocluster
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.mongocluster.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mongoClusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Get a specific private connection |
| <CopyableCode code="list_by_mongo_cluster" /> | `SELECT` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | List existing private connections |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="mongoClusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Create a Private endpoint connection |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mongoClusterName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Delete the private endpoint connection |

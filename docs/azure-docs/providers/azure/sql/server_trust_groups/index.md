---
title: server_trust_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - server_trust_groups
  - sql
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
<tr><td><b>Name</b></td><td><code>server_trust_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_trust_groups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, serverTrustGroupName, subscriptionId" /> | Gets a server trust group. |
| <CopyableCode code="list_by_instance" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a server trust groups by instance name. |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists a server trust group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="locationName, resourceGroupName, serverTrustGroupName, subscriptionId" /> | Creates or updates a server trust group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationName, resourceGroupName, serverTrustGroupName, subscriptionId" /> | Deletes a server trust group. |
| <CopyableCode code="_list_by_instance" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Gets a server trust groups by instance name. |
| <CopyableCode code="_list_by_location" /> | `EXEC` | <CopyableCode code="locationName, resourceGroupName, subscriptionId" /> | Lists a server trust group. |

---
title: workload_networks_dns_service
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_networks_dns_service
  - vmware
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
<tr><td><b>Name</b></td><td><code>workload_networks_dns_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.workload_networks_dns_service" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsServiceId, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dnsServiceId, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsServiceId, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dnsServiceId, privateCloudName, resourceGroupName, subscriptionId" /> |

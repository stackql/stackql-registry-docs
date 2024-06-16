---
title: cloud_vm_clusters_private_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_vm_clusters_private_ip_addresses
  - oracle
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
<tr><td><b>Name</b></td><td><code>cloud_vm_clusters_private_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.cloud_vm_clusters_private_ip_addresses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="displayName" /> | `string` | PrivateIpAddresses displayName |
| <CopyableCode code="hostnameLabel" /> | `string` | PrivateIpAddresses hostnameLabel |
| <CopyableCode code="ipAddress" /> | `string` | PrivateIpAddresses ipAddress |
| <CopyableCode code="ocid" /> | `string` | The [OCID](/Content/General/Concepts/identifiers.htm) of the resource. |
| <CopyableCode code="subnetId" /> | `string` | The [OCID](/Content/General/Concepts/identifiers.htm) of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, data__subnetId, data__vnicId" /> |

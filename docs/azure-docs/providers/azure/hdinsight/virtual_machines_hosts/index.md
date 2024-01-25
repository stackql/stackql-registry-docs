---
title: virtual_machines_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines_hosts
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machines_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.virtual_machines_hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The host name |
| `effectiveDiskEncryptionKeyUrl` | `string` | The effective disk encryption key URL used by the host |
| `fqdn` | `string` | The Fully Qualified Domain Name of host |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` |

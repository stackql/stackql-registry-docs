---
title: l2_isolation_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - l2_isolation_domains
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>l2_isolation_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.l2_isolation_domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | L2Isolation Domain Properties defines the properties of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `l2IsolationDomainName, resourceGroupName, subscriptionId` | Implements L2 Isolation Domain GET method. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Displays L2IsolationDomains list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Displays L2IsolationDomains list by subscription GET method. |
| `create` | `INSERT` | `l2IsolationDomainName, resourceGroupName, subscriptionId, data__properties` | Creates layer 2 network connectivity between compute nodes within a rack and across racks.The configuration is applied on the devices only after the isolation domain is enabled. |
| `delete` | `DELETE` | `l2IsolationDomainName, resourceGroupName, subscriptionId` | Deletes layer 2 connectivity between compute nodes by managed by named L2 Isolation name. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Displays L2IsolationDomains list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Displays L2IsolationDomains list by subscription GET method. |
| `commit_configuration` | `EXEC` | `l2IsolationDomainName, resourceGroupName, subscriptionId` | Commits the configuration of the given resources. |
| `update` | `EXEC` | `l2IsolationDomainName, resourceGroupName, subscriptionId` | API to update certain properties of the L2 Isolation Domain resource. |
| `validate_configuration` | `EXEC` | `l2IsolationDomainName, resourceGroupName, subscriptionId` | Validates the configuration of the resources. |

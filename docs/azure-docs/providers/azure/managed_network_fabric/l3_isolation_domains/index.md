---
title: l3_isolation_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - l3_isolation_domains
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>l3_isolation_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.l3_isolation_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | L3 Isolation Domain Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Retrieves details of this L3 Isolation Domain. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays L3IsolationDomains list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays L3IsolationDomains list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId, data__properties" /> | Create isolation domain resources for layer 3 connectivity between compute nodes and for communication with external services .This configuration is applied on the devices only after the creation of networks is completed and isolation domain is enabled.  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Deletes layer 3 connectivity between compute nodes by managed by named L3 Isolation name. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays L3IsolationDomains list by resource group GET method. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Displays L3IsolationDomains list by subscription GET method. |
| <CopyableCode code="commit_configuration" /> | `EXEC` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Commits the configuration of the given resources. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | API to update certain properties of the L3 Isolation Domain resource. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Validates the configuration of the resources. |

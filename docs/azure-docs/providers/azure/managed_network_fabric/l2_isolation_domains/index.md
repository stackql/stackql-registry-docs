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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>l2_isolation_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.l2_isolation_domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | L2Isolation Domain Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements L2 Isolation Domain GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays L2IsolationDomains list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays L2IsolationDomains list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId, data__properties" /> | Creates layer 2 network connectivity between compute nodes within a rack and across racks.The configuration is applied on the devices only after the isolation domain is enabled. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | Deletes layer 2 connectivity between compute nodes by managed by named L2 Isolation name. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays L2IsolationDomains list by resource group GET method. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Displays L2IsolationDomains list by subscription GET method. |
| <CopyableCode code="commit_configuration" /> | `EXEC` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | Commits the configuration of the given resources. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | API to update certain properties of the L2 Isolation Domain resource. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="l2IsolationDomainName, resourceGroupName, subscriptionId" /> | Validates the configuration of the resources. |

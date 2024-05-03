---
title: cloud_service_role_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_role_instances
  - compute
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
<tr><td><b>Name</b></td><td><code>cloud_service_role_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_service_role_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Role instance properties. |
| <CopyableCode code="sku" /> | `object` | The role instance SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource Type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | Gets a role instance from a cloud service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Gets the list of all role instances in a cloud service. Use nextLink property in the response to get the next page of role instances. Do this till nextLink is null to fetch all the role instances. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | Deletes a role instance from a cloud service. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Gets the list of all role instances in a cloud service. Use nextLink property in the response to get the next page of role instances. Do this till nextLink is null to fetch all the role instances. |
| <CopyableCode code="rebuild" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | The Rebuild Role Instance asynchronous operation reinstalls the operating system on instances of web roles or worker roles and initializes the storage resources that are used by them. If you do not want to initialize storage resources, you can use Reimage Role Instance. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | The Reimage Role Instance asynchronous operation reinstalls the operating system on instances of web roles or worker roles. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | The Reboot Role Instance asynchronous operation requests a reboot of a role instance in the cloud service. |

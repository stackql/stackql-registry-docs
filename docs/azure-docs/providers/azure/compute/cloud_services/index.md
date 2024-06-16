---
title: cloud_services
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services
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
<tr><td><b>Name</b></td><td><code>cloud_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Cloud service properties |
| <CopyableCode code="systemData" /> | `object` | The system meta data relating to this resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | List of logical availability zone of the resource. List should contain only 1 zone where cloud service should be provisioned. This field is optional. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Display information about a cloud service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of all cloud services under a resource group. Use nextLink property in the response to get the next page of Cloud Services. Do this till nextLink is null to fetch all the Cloud Services. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, data__location" /> | Create or update a cloud service. Please note some properties can be set only during cloud service creation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Deletes a cloud service. |
| <CopyableCode code="power_off" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Power off the cloud service. Note that resources are still attached and you are getting charged for the resources. |
| <CopyableCode code="rebuild" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances" /> | Rebuild Role Instances reinstalls the operating system on instances of web roles or worker roles and initializes the storage resources that are used by them. If you do not want to initialize storage resources, you can use Reimage Role Instances. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances" /> | Reimage asynchronous operation reinstalls the operating system on instances of web roles or worker roles. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId, data__roleInstances" /> | Restarts one or more role instances in a cloud service. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Starts the cloud service. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Update a cloud service. |

---
title: service_endpoint_policy_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - service_endpoint_policy_definitions
  - network
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
<tr><td><b>Name</b></td><td><code>service_endpoint_policy_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.service_endpoint_policy_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Service Endpoint policy definition resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceEndpointPolicyDefinitionName, serviceEndpointPolicyName, subscriptionId" /> | Get the specified service endpoint policy definitions from service endpoint policy. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceEndpointPolicyName, subscriptionId" /> | Gets all service endpoint policy definitions in a service end point policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceEndpointPolicyDefinitionName, serviceEndpointPolicyName, subscriptionId" /> | Creates or updates a service endpoint policy definition in the specified service endpoint policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serviceEndpointPolicyDefinitionName, serviceEndpointPolicyName, subscriptionId" /> | Deletes the specified ServiceEndpoint policy definitions. |

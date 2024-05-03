---
title: service_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_configurations
  - hybrid_connectivity
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
<tr><td><b>Name</b></td><td><code>service_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.service_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Service configuration details |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, resourceUri, serviceConfigurationName" /> | Gets the details about the service to the resource. |
| <CopyableCode code="list_by_endpoint_resource" /> | `SELECT` | <CopyableCode code="endpointName, resourceUri" /> | API to enumerate registered services in service configurations under a Endpoint Resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, resourceUri, serviceConfigurationName" /> | Deletes the service details to the target resource. |
| <CopyableCode code="_list_by_endpoint_resource" /> | `EXEC` | <CopyableCode code="endpointName, resourceUri" /> | API to enumerate registered services in service configurations under a Endpoint Resource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="endpointName, resourceUri, serviceConfigurationName" /> | Update the service details in the service configurations of the target resource. |

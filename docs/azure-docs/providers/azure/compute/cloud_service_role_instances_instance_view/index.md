---
title: cloud_service_role_instances_instance_view
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_role_instances_instance_view
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_service_role_instances_instance_view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.cloud_service_role_instances_instance_view</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `platformFaultDomain` | `integer` | The Fault Domain. |
| `platformUpdateDomain` | `integer` | The Update Domain. |
| `privateId` | `string` | Specifies a unique identifier generated internally for the cloud service associated with this role instance. &lt;br /&gt;&lt;br /&gt; NOTE: If you are using Azure Diagnostics extension, this property can be used as 'DeploymentId' for querying details. |
| `statuses` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId` |

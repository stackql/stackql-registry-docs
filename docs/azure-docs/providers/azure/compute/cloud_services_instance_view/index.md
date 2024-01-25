---
title: cloud_services_instance_view
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_services_instance_view
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
<tr><td><b>Name</b></td><td><code>cloud_services_instance_view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.cloud_services_instance_view</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `privateIds` | `array` | Specifies a list of unique identifiers generated internally for the cloud service. &lt;br /&gt;&lt;br /&gt; NOTE: If you are using Azure Diagnostics extension, this property can be used as 'DeploymentId' for querying details. |
| `roleInstance` | `object` | Instance view statuses. |
| `sdkVersion` | `string` | The version of the SDK that was used to generate the package for the cloud service. |
| `statuses` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `cloudServiceName, resourceGroupName, subscriptionId` |

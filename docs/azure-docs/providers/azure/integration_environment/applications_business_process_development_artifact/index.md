---
title: applications_business_process_development_artifact
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_business_process_development_artifact
  - integration_environment
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
<tr><td><b>Name</b></td><td><code>applications_business_process_development_artifact</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.integration_environment.applications_business_process_development_artifact</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the business process development artifact. |
| `properties` | `object` | The properties of business process development artifact. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `applicationName, resourceGroupName, spaceName, subscriptionId, data__name` | The get business process development artifact action. |
| `delete` | `DELETE` | `applicationName, resourceGroupName, spaceName, subscriptionId, data__name` | The delete business process development artifact action. |

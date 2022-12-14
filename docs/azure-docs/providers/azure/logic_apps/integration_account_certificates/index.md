---
title: integration_account_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_certificates
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>integration_account_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_account_certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `properties` | `object` | The integration account certificate properties. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
| `location` | `string` | The resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationAccountCertificates_Get` | `SELECT` | `api-version, certificateName, integrationAccountName, resourceGroupName, subscriptionId` | Gets an integration account certificate. |
| `IntegrationAccountCertificates_List` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets a list of integration account certificates. |
| `IntegrationAccountCertificates_CreateOrUpdate` | `INSERT` | `api-version, certificateName, integrationAccountName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an integration account certificate. |
| `IntegrationAccountCertificates_Delete` | `DELETE` | `api-version, certificateName, integrationAccountName, resourceGroupName, subscriptionId` | Deletes an integration account certificate. |

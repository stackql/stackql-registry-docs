---
title: private_link_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resource
  - migrate
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>private_link_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.private_link_resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Path reference to this private link resource. /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Migrate/assessmentProjects/&#123;projectName&#125;/privateLinkResources/&#123;privateLinkResourceName&#125; |
| `name` | `string` | Name of the private link resource. |
| `properties` | `object` | Properties of a private link resource. |
| `type` | `string` | Type of the object = [Microsoft.Migrate/assessmentProjects/privateLinkResources]. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateLinkResource_Get` | `SELECT` | `api-version, privateLinkResourceName, projectName, resourceGroupName, subscriptionId` | Get information related to a specific private Link Resource in the project. Returns a json object of type 'privateLinkResources' as specified in the models section. |
| `PrivateLinkResource_ListByProject` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get all private link resources created in the project. Returns a json array of objects of type 'privateLinkResources' as specified in the Models section. |

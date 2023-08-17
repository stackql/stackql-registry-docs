---
title: sfdc_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sfdc_instances
  - integrations
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sfdc_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.integrations.sfdc_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the SFDC instance projects/&#123;project&#125;/locations/&#123;location&#125;/sfdcInstances/&#123;sfdcInstance&#125;. |
| `description` | `string` | A description of the sfdc instance. |
| `displayName` | `string` | User selected unique name/alias to easily reference an instance. |
| `deleteTime` | `string` | Output only. Time when the instance was deleted. Empty if not deleted. |
| `createTime` | `string` | Output only. Time when the instance is created |
| `authConfigId` | `array` | A list of AuthConfigs that can be tried to open the channel to SFDC |
| `serviceAuthority` | `string` | URL used for API calls after authentication (the login authority is configured within the referenced AuthConfig). |
| `sfdcOrgId` | `string` | The SFDC Org Id. This is defined in salesforce. |
| `updateTime` | `string` | Output only. Time when the instance was last updated |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_products_sfdc_instances_get` | `SELECT` | `locationsId, productsId, projectsId, sfdcInstancesId` | Gets an sfdc instance. If the instance doesn't exist, Code.NOT_FOUND exception will be thrown. |
| `projects_locations_products_sfdc_instances_list` | `SELECT` | `locationsId, productsId, projectsId` | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| `projects_locations_sfdc_instances_get` | `SELECT` | `locationsId, projectsId, sfdcInstancesId` | Gets an sfdc instance. If the instance doesn't exist, Code.NOT_FOUND exception will be thrown. |
| `projects_locations_sfdc_instances_list` | `SELECT` | `locationsId, projectsId` | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| `projects_locations_products_sfdc_instances_create` | `INSERT` | `locationsId, productsId, projectsId` | Creates an sfdc instance record. Store the sfdc instance in Spanner. Returns the sfdc instance. |
| `projects_locations_sfdc_instances_create` | `INSERT` | `locationsId, projectsId` | Creates an sfdc instance record. Store the sfdc instance in Spanner. Returns the sfdc instance. |
| `projects_locations_products_sfdc_instances_delete` | `DELETE` | `locationsId, productsId, projectsId, sfdcInstancesId` | Deletes an sfdc instance. |
| `projects_locations_sfdc_instances_delete` | `DELETE` | `locationsId, projectsId, sfdcInstancesId` | Deletes an sfdc instance. |
| `_projects_locations_products_sfdc_instances_list` | `EXEC` | `locationsId, productsId, projectsId` | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| `_projects_locations_sfdc_instances_list` | `EXEC` | `locationsId, projectsId` | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| `projects_locations_products_sfdc_instances_patch` | `EXEC` | `locationsId, productsId, projectsId, sfdcInstancesId` | Updates an sfdc instance. Updates the sfdc instance in spanner. Returns the sfdc instance. |
| `projects_locations_sfdc_instances_patch` | `EXEC` | `locationsId, projectsId, sfdcInstancesId` | Updates an sfdc instance. Updates the sfdc instance in spanner. Returns the sfdc instance. |

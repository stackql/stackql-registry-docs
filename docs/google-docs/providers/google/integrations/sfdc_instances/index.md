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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sfdc_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="integrations.sfdc_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the SFDC instance projects/&#123;project&#125;/locations/&#123;location&#125;/sfdcInstances/&#123;sfdcInstance&#125;. |
| <CopyableCode code="description" /> | `string` | A description of the sfdc instance. |
| <CopyableCode code="authConfigId" /> | `array` | A list of AuthConfigs that can be tried to open the channel to SFDC |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the instance is created |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Time when the instance was deleted. Empty if not deleted. |
| <CopyableCode code="displayName" /> | `string` | User selected unique name/alias to easily reference an instance. |
| <CopyableCode code="serviceAuthority" /> | `string` | URL used for API calls after authentication (the login authority is configured within the referenced AuthConfig). |
| <CopyableCode code="sfdcOrgId" /> | `string` | The SFDC Org Id. This is defined in salesforce. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the instance was last updated |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_products_sfdc_instances_get" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId, sfdcInstancesId" /> | Gets an sfdc instance. If the instance doesn't exist, Code.NOT_FOUND exception will be thrown. |
| <CopyableCode code="projects_locations_products_sfdc_instances_list" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| <CopyableCode code="projects_locations_sfdc_instances_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sfdcInstancesId" /> | Gets an sfdc instance. If the instance doesn't exist, Code.NOT_FOUND exception will be thrown. |
| <CopyableCode code="projects_locations_sfdc_instances_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| <CopyableCode code="projects_locations_products_sfdc_instances_create" /> | `INSERT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Creates an sfdc instance record. Store the sfdc instance in Spanner. Returns the sfdc instance. |
| <CopyableCode code="projects_locations_sfdc_instances_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an sfdc instance record. Store the sfdc instance in Spanner. Returns the sfdc instance. |
| <CopyableCode code="projects_locations_products_sfdc_instances_delete" /> | `DELETE` | <CopyableCode code="locationsId, productsId, projectsId, sfdcInstancesId" /> | Deletes an sfdc instance. |
| <CopyableCode code="projects_locations_sfdc_instances_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sfdcInstancesId" /> | Deletes an sfdc instance. |
| <CopyableCode code="_projects_locations_products_sfdc_instances_list" /> | `EXEC` | <CopyableCode code="locationsId, productsId, projectsId" /> | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| <CopyableCode code="_projects_locations_sfdc_instances_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| <CopyableCode code="projects_locations_products_sfdc_instances_patch" /> | `EXEC` | <CopyableCode code="locationsId, productsId, projectsId, sfdcInstancesId" /> | Updates an sfdc instance. Updates the sfdc instance in spanner. Returns the sfdc instance. |
| <CopyableCode code="projects_locations_sfdc_instances_patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, sfdcInstancesId" /> | Updates an sfdc instance. Updates the sfdc instance in spanner. Returns the sfdc instance. |

---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - visual_studio
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.visual_studio.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Key/value pair of resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, rootResourceName, subscriptionId" /> | Gets the details of a Team Services project resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, rootResourceName, subscriptionId" /> | Gets all Visual Studio Team Services project resources created in the specified Team Services account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, rootResourceName, subscriptionId" /> | Creates a Team Services project in the collection with the specified name. 'VersionControlOption' and 'ProcessTemplateId' must be specified in the resource properties. Valid values for VersionControlOption: Git, Tfvc. Valid values for ProcessTemplateId: 6B724908-EF14-45CF-84F8-768B5384DA45, ADCC42AB-9882-485E-A3ED-7678F01F66BC, 27450541-8E31-4150-9947-DC59F998FC01 (these IDs correspond to Scrum, Agile, and CMMI process templates). |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, rootResourceName, subscriptionId" /> | Gets all Visual Studio Team Services project resources created in the specified Team Services account. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, rootResourceName, subscriptionId" /> | Updates the tags of the specified Team Services project. |

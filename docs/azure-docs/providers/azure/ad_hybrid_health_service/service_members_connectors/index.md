---
title: service_members_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_connectors
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>service_members_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.service_members_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The connector Id. |
| `name` | `string` | The connector name. |
| `description` | `string` | The connector description. |
| `attributesIncluded` | `array` | The attribute inclusion list of the connector. |
| `classesIncluded` | `array` | The class inclusion list of the connector. |
| `connectorId` | `string` | The connector Id. |
| `partitions` | `array` | The partitions of the connector. |
| `passwordHashSyncConfiguration` | `object` | The password hash synchronization configuration of the connector. |
| `passwordManagementSettings` | `object` | The password management settings of the connector. |
| `runProfiles` | `array` | The run profiles of the connector. |
| `schemaXml` | `string` | The schema xml for the connector. |
| `timeCreated` | `string` | The date and time when this connector was created. |
| `timeLastModified` | `string` | The date and time when this connector was last modified. |
| `type` | `string` | The connector type. |
| `version` | `integer` | The connector version |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceMemberId, serviceName` |
| `_list` | `EXEC` | `serviceMemberId, serviceName` |

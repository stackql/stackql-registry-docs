---
title: resource_value_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_value_configs
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>resource_value_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.resource_value_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is empty, there are no subsequent pages. |
| `resourceValueConfigs` | `array` | The resource value configs from the specified parent. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_resource_value_configs_list` | `SELECT` | `organizationsId` | Lists all ResourceValueConfigs. |
| `organizations_resource_value_configs_delete` | `DELETE` | `organizationsId, resourceValueConfigsId` | Deletes a ResourceValueConfig. |
| `organizations_resource_value_configs_batch_create` | `EXEC` | `organizationsId` | Creates a ResourceValueConfig for an organization. Maps user's tags to difference resource values for use by the attack path simulation. |
| `organizations_resource_value_configs_get` | `EXEC` | `organizationsId, resourceValueConfigsId` | Gets a ResourceValueConfig. |
| `organizations_resource_value_configs_patch` | `EXEC` | `organizationsId, resourceValueConfigsId` | Updates an existing ResourceValueConfigs with new rules. |

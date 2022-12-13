---
title: service_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - service_tags
  - network
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
<tr><td><b>Name</b></td><td><code>service_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.service_tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the cloud. |
| `name` | `string` | The name of the cloud. |
| `nextLink` | `string` | The URL to get next page of service tag information resources. |
| `type` | `string` | The azure resource type. |
| `values` | `array` | The list of service tag information resources. |
| `changeNumber` | `string` | The iteration number. |
| `cloud` | `string` | The name of the cloud. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ServiceTags_List` | `SELECT` | `location, subscriptionId` |

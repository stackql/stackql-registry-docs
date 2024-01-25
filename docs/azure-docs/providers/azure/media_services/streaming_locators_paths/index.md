---
title: streaming_locators_paths
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_locators_paths
  - media_services
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
<tr><td><b>Name</b></td><td><code>streaming_locators_paths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.media_services.streaming_locators_paths</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `downloadPaths` | `array` | Download Paths supported by current Streaming Locator |
| `streamingPaths` | `array` | Streaming Paths supported by current Streaming Locator |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, api-version, resourceGroupName, streamingLocatorName, subscriptionId` |

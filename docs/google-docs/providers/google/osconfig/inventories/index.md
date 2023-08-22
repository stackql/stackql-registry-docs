---
title: inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - inventories
  - osconfig
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
<tr><td><b>Name</b></td><td><code>inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.osconfig.inventories</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The `Inventory` API resource name. Format: `projects/&#123;project_number&#125;/locations/&#123;location&#125;/instances/&#123;instance_id&#125;/inventory` |
| `updateTime` | `string` | Output only. Timestamp of the last reported inventory for the VM. |
| `items` | `object` | Inventory items related to the VM keyed by an opaque unique identifier for each inventory item. The identifier is unique to each distinct and addressable inventory item and will change, when there is a new package version. |
| `osInfo` | `object` | Operating system information for the VM. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `instancesId, locationsId, projectsId` |
| `_list` | `EXEC` | `instancesId, locationsId, projectsId` |

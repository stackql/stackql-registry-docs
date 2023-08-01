---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - iot_security
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_security.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | IoT site properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Sites_List` | `SELECT` | `scope` | List IoT sites |
| `Sites_CreateOrUpdate` | `INSERT` | `scope` | Create or update IoT site |
| `Sites_Delete` | `DELETE` | `scope` | Delete IoT site |
| `Sites_Get` | `EXEC` | `scope` | Get IoT site |

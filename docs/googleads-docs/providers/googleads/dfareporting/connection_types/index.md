---
title: connection_types
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_types
  - dfareporting
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.connection_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this connection type. |
| `name` | `string` | Name of this connection type. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#connectionType". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `connectionTypes_get` | `SELECT` | `id, profileId` | Gets one connection type by ID. |
| `connectionTypes_list` | `SELECT` | `profileId` | Retrieves a list of connection types. |

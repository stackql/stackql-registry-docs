---
title: flighting_rings
hide_title: false
hide_table_of_contents: false
keywords:
  - flighting_rings
  - test_base
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>flighting_rings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.flighting_rings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | The Flighting Ring properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FlightingRings_Get` | `SELECT` | `flightingRingResourceName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets a flighting ring of a Test Base Account. |
| `FlightingRings_List` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the flighting rings of a Test Base Account. |

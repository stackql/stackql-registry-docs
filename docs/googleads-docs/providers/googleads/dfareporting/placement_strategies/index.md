---
title: placement_strategies
hide_title: false
hide_table_of_contents: false
keywords:
  - placement_strategies
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
<tr><td><b>Name</b></td><td><code>placement_strategies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.placement_strategies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this placement strategy. This is a read-only, auto-generated field. |
| `name` | `string` | Name of this placement strategy. This is a required field. It must be less than 256 characters long and unique among placement strategies of the same account. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#placementStrategy". |
| `accountId` | `string` | Account ID of this placement strategy.This is a read-only field that can be left blank. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `placementStrategies_get` | `SELECT` | `id, profileId` | Gets one placement strategy by ID. |
| `placementStrategies_list` | `SELECT` | `profileId` | Retrieves a list of placement strategies, possibly filtered. This method supports paging. |
| `placementStrategies_delete` | `DELETE` | `id, profileId` | Deletes an existing placement strategy. |
| `placementStrategies_insert` | `EXEC` | `profileId` | Inserts a new placement strategy. |
| `placementStrategies_patch` | `EXEC` | `id, profileId` | Updates an existing placement strategy. This method supports patch semantics. |
| `placementStrategies_update` | `EXEC` | `profileId` | Updates an existing placement strategy. |

---
title: creative_field_values
hide_title: false
hide_table_of_contents: false
keywords:
  - creative_field_values
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
<tr><td><b>Name</b></td><td><code>creative_field_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.dfareporting.creative_field_values</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of this creative field value. This is a read-only, auto-generated field. |
| `value` | `string` | Value of this creative field value. It needs to be less than 256 characters in length and unique per creative field. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "dfareporting#creativeFieldValue". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `creativeFieldValues_get` | `SELECT` | `creativeFieldId, id, profileId` | Gets one creative field value by ID. |
| `creativeFieldValues_list` | `SELECT` | `creativeFieldId, profileId` | Retrieves a list of creative field values, possibly filtered. This method supports paging. |
| `creativeFieldValues_delete` | `DELETE` | `creativeFieldId, id, profileId` | Deletes an existing creative field value. |
| `creativeFieldValues_insert` | `EXEC` | `creativeFieldId, profileId` | Inserts a new creative field value. |
| `creativeFieldValues_patch` | `EXEC` | `creativeFieldId, id, profileId` | Updates an existing creative field value. This method supports patch semantics. |
| `creativeFieldValues_update` | `EXEC` | `creativeFieldId, profileId` | Updates an existing creative field value. |

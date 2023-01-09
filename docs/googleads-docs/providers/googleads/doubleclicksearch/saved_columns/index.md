---
title: saved_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_columns
  - doubleclicksearch
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
<tr><td><b>Name</b></td><td><code>saved_columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.doubleclicksearch.saved_columns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies this as a SavedColumn resource. Value: the fixed string doubleclicksearch#savedColumn. |
| `savedColumnName` | `string` | The name of the saved column. |
| `type` | `string` | The type of data this saved column will produce. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `savedColumns_list` | `SELECT` | `advertiserId, agencyId` |

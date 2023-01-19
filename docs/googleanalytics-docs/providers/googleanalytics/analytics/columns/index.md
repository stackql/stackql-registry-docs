---
title: columns
hide_title: false
hide_table_of_contents: false
keywords:
  - columns
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.columns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Column id. |
| `attributes` | `object` | Map of attribute name and value for this column. |
| `kind` | `string` | Resource type for Analytics column. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `metadata_columns_list` | `SELECT` | `reportType` |

---
title: properties__metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - properties__metadata
  - analyticsdata
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
<tr><td><b>Name</b></td><td><code>properties__metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsdata.properties__metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of this metadata. |
| `dimensions` | `array` | The dimension descriptions. |
| `metrics` | `array` | The metric descriptions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `properties_getMetadata` | `SELECT` | `propertiesId` |

---
title: instances_screenshot
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_screenshot
  - compute
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
<tr><td><b>Name</b></td><td><code>instances_screenshot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instances_screenshot</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `contents` | `string` | [Output Only] The Base64-encoded screenshot data. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#screenshot for the screenshots. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_screenshot` | `SELECT` | `instance, project, zone` |

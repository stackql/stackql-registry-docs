---
title: instances_guest_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_guest_attributes
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_guest_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instances_guest_attributes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `variableValue` | `string` | [Output Only] The value found for the requested key. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#guestAttributes for guest attributes entry. |
| `queryPath` | `string` | The path to be queried. This can be the default namespace ('') or a nested namespace ('\/') or a specified key ('\/\'). |
| `queryValue` | `object` | Array of guest attribute namespace/key/value tuples. |
| `selfLink` | `string` | [Output Only] Server-defined URL for this resource. |
| `variableKey` | `string` | The key to search for. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instances_getGuestAttributes` | `SELECT` | `instance, project, zone` |

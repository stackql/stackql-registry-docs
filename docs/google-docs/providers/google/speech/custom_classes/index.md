---
title: custom_classes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_classes
  - speech
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
<tr><td><b>Name</b></td><td><code>custom_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.speech.custom_classes</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customClassesId, locationsId, projectsId` | Get a custom class. |
| `list` | `SELECT` | `locationsId, projectsId` | List custom classes. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a custom class. |
| `delete` | `DELETE` | `customClassesId, locationsId, projectsId` | Delete a custom class. |
| `patch` | `EXEC` | `customClassesId, locationsId, projectsId` | Update a custom class. |

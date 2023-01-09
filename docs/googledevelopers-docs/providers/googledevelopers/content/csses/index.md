---
title: csses
hide_title: false
hide_table_of_contents: false
keywords:
  - csses
  - content
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>csses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.csses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `labelIds` | `array` | A list of label IDs that are assigned to this CSS domain by its CSS group. Only populated for CSS group users. |
| `cssDomainId` | `string` | Output only. Immutable. The CSS domain ID. |
| `cssGroupId` | `string` | Output only. Immutable. The ID of the CSS group this CSS domain is affiliated with. Only populated for CSS group users. |
| `displayName` | `string` | Output only. Immutable. The CSS domain's display name, used when space is constrained. |
| `fullName` | `string` | Output only. Immutable. The CSS domain's full name. |
| `homepageUri` | `string` | Output only. Immutable. The CSS domain's homepage. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cssDomainId, cssGroupId` | Retrieves a single CSS domain by ID. |
| `list` | `SELECT` | `cssGroupId` | Lists CSS domains affiliated with a CSS group. |
| `updatelabels` | `EXEC` | `cssDomainId, cssGroupId` | Updates labels that are assigned to a CSS domain by its CSS group. |

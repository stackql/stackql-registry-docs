---
title: changes_start_page_token
hide_title: false
hide_table_of_contents: false
keywords:
  - changes_start_page_token
  - drive
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>changes_start_page_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drive.changes_start_page_token</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#startPageToken". |
| `startPageToken` | `string` | The starting page token for listing changes. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `changes_getStartPageToken` | `SELECT` |  |

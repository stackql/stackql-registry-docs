---
title: scanned_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - scanned_resources
  - workloadmanager
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
<tr><td><b>Name</b></td><td><code>scanned_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workloadmanager.scanned_resources</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `evaluationsId, executionsId, locationsId, projectsId` |
| `_list` | `EXEC` | `evaluationsId, executionsId, locationsId, projectsId` |

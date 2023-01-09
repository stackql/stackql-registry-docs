---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - adexperiencereport
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexperiencereport.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `mobileSummary` | `object` | A site's Ad Experience Report summary on a single platform. |
| `reviewedSite` | `string` | The name of the reviewed site, e.g. `google.com`. |
| `desktopSummary` | `object` | A site's Ad Experience Report summary on a single platform. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `sitesId` |

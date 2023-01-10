---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - abusiveexperiencereport
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
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.abusiveexperiencereport.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `reportUrl` | `string` | A link to the full Abusive Experience Report for the site. Not set in ViolatingSitesResponse. Note that you must complete the [Search Console verification process](https://support.google.com/webmasters/answer/9008080) for the site before you can access the full report. |
| `reviewedSite` | `string` | The name of the reviewed site, e.g. `google.com`. |
| `underReview` | `boolean` | Whether the site is currently under review. |
| `abusiveStatus` | `string` | The site's Abusive Experience Report status. |
| `enforcementTime` | `string` | The time at which [enforcement](https://support.google.com/webtools/answer/7538608) against the site began or will begin. Not set when the filter_status is OFF. |
| `filterStatus` | `string` | The site's [enforcement status](https://support.google.com/webtools/answer/7538608). |
| `lastChangeTime` | `string` | The time at which the site's status last changed. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `sitesId` |

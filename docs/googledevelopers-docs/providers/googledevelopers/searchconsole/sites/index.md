---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - searchconsole
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
<tr><td><b>Id</b></td><td><code>googledevelopers.searchconsole.sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `permissionLevel` | `string` | The user's permission level for the site. |
| `siteUrl` | `string` | The URL of the site. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `webmasters_sites_get` | `SELECT` | `siteUrl` |  Retrieves information about specific site. |
| `webmasters_sites_list` | `SELECT` |  |  Lists the user's Search Console sites. |
| `webmasters_sites_delete` | `DELETE` | `siteUrl` |  Removes a site from the set of the user's Search Console sites. |
| `webmasters_sites_add` | `EXEC` | `siteUrl` |  Adds a site to the set of the user's sites in Search Console. |

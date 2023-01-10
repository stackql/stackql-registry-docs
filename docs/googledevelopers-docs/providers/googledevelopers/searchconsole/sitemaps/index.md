---
title: sitemaps
hide_title: false
hide_table_of_contents: false
keywords:
  - sitemaps
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
<tr><td><b>Name</b></td><td><code>sitemaps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.searchconsole.sitemaps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `lastSubmitted` | `string` | Date & time in which this sitemap was submitted. Date format is in RFC 3339 format (yyyy-mm-dd). |
| `path` | `string` | The url of the sitemap. |
| `type` | `string` | The type of the sitemap. For example: `rssFeed`. |
| `lastDownloaded` | `string` | Date & time in which this sitemap was last downloaded. Date format is in RFC 3339 format (yyyy-mm-dd). |
| `isSitemapsIndex` | `boolean` | If true, the sitemap is a collection of sitemaps. |
| `isPending` | `boolean` | If true, the sitemap has not been processed. |
| `errors` | `string` | Number of errors in the sitemap. These are issues with the sitemap itself that need to be fixed before it can be processed correctly. |
| `contents` | `array` | The various content types in the sitemap. |
| `warnings` | `string` | Number of warnings for the sitemap. These are generally non-critical issues with URLs in the sitemaps. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `webmasters_sitemaps_get` | `SELECT` | `feedpath, siteUrl` | Retrieves information about a specific sitemap. |
| `webmasters_sitemaps_list` | `SELECT` | `siteUrl` |  Lists the [sitemaps-entries](/webmaster-tools/v3/sitemaps) submitted for this site, or included in the sitemap index file (if `sitemapIndex` is specified in the request). |
| `webmasters_sitemaps_delete` | `DELETE` | `feedpath, siteUrl` | Deletes a sitemap from the Sitemaps report. Does not stop Google from crawling this sitemap or the URLs that were previously crawled in the deleted sitemap. |
| `webmasters_sitemaps_submit` | `EXEC` | `feedpath, siteUrl` | Submits a sitemap for a site. |

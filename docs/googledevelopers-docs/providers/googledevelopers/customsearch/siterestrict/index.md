---
title: siterestrict
hide_title: false
hide_table_of_contents: false
keywords:
  - siterestrict
  - customsearch
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
<tr><td><b>Name</b></td><td><code>siterestrict</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.customsearch.siterestrict</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `mime` | `string` | The MIME type of the search result. |
| `image` | `object` | Image belonging to a custom search result. |
| `formattedUrl` | `string` | The URL displayed after the snippet for each search result. |
| `htmlTitle` | `string` | The title of the search result, in HTML. |
| `kind` | `string` | A unique identifier for the type of current object. For this API, it is `customsearch#result.` |
| `title` | `string` | The title of the search result, in plain text. |
| `labels` | `array` | Encapsulates all information about refinement labels. |
| `link` | `string` | The full URL to which the search result is pointing, e.g. http://www.example.com/foo/bar. |
| `pagemap` | `object` | Contains [PageMap](https://developers.google.com/custom-search/docs/structured_data#pagemaps) information for this search result. |
| `displayLink` | `string` | An abridged version of this search result’s URL, e.g. www.example.com. |
| `htmlSnippet` | `string` | The snippet of the search result, in HTML. |
| `cacheId` | `string` | Indicates the ID of Google's cached version of the search result. |
| `snippet` | `string` | The snippet of the search result, in plain text. |
| `htmlFormattedUrl` | `string` | The HTML-formatted URL displayed after the snippet for each search result. |
| `fileFormat` | `string` | The file format of the search result. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `search_cse_siterestrict_list` | `SELECT` |  |

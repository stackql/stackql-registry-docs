---
title: cse
hide_title: false
hide_table_of_contents: false
keywords:
  - cse
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
<tr><td><b>Name</b></td><td><code>cse</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.customsearch.cse</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cacheId` | `string` | Indicates the ID of Google's cached version of the search result. |
| `htmlFormattedUrl` | `string` | The HTML-formatted URL displayed after the snippet for each search result. |
| `snippet` | `string` | The snippet of the search result, in plain text. |
| `labels` | `array` | Encapsulates all information about refinement labels. |
| `image` | `object` | Image belonging to a custom search result. |
| `mime` | `string` | The MIME type of the search result. |
| `fileFormat` | `string` | The file format of the search result. |
| `htmlTitle` | `string` | The title of the search result, in HTML. |
| `title` | `string` | The title of the search result, in plain text. |
| `formattedUrl` | `string` | The URL displayed after the snippet for each search result. |
| `pagemap` | `object` | Contains [PageMap](https://developers.google.com/custom-search/docs/structured_data#pagemaps) information for this search result. |
| `link` | `string` | The full URL to which the search result is pointing, e.g. http://www.example.com/foo/bar. |
| `htmlSnippet` | `string` | The snippet of the search result, in HTML. |
| `displayLink` | `string` | An abridged version of this search result’s URL, e.g. www.example.com. |
| `kind` | `string` | A unique identifier for the type of current object. For this API, it is `customsearch#result.` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `search_cse_list` | `SELECT` |  |

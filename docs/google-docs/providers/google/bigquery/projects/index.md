---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - bigquery
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `projects` | `array` | Projects to which you have at least READ access. |
| `totalItems` | `integer` | The total number of projects in the list. |
| `etag` | `string` | A hash of the page of results |
| `kind` | `string` | The type of list. |
| `nextPageToken` | `string` | A token to request the next page of results. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |

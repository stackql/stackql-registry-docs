---
title: saved_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_queries
  - cloudasset
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
<tr><td><b>Name</b></td><td><code>saved_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudasset.saved_queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the saved query. The format must be: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id |
| `description` | `string` | The description of this saved query. This value should be fewer than 255 characters. |
| `content` | `object` | The query content. |
| `createTime` | `string` | Output only. The create time of this saved query. |
| `creator` | `string` | Output only. The account's email address who has created this saved query. |
| `labels` | `object` | Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters. |
| `lastUpdateTime` | `string` | Output only. The last update time of this saved query. |
| `lastUpdater` | `string` | Output only. The account's email address who has updated this saved query most recently. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `savedQueries_list` | `SELECT` | `parent` | Lists all saved queries in a parent project/folder/organization. |
| `savedQueries_create` | `INSERT` | `parent` | Creates a saved query in a parent project/folder/organization. |

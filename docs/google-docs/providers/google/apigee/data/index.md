---
title: data
hide_title: false
hide_table_of_contents: false
keywords:
  - data
  - apigee
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
<tr><td><b>Name</b></td><td><code>data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.data</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `completed` | `boolean` | Flag indicating whether a transaction is completed or not |
| `point` | `array` | List of debug data collected by runtime plane at various defined points in the flow. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_environments_apis_revisions_debugsessions_data_get` | `SELECT` | `apisId, dataId, debugsessionsId, environmentsId, organizationsId, revisionsId` |

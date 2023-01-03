---
title: admin_schemav2
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_schemav2
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
<tr><td><b>Name</b></td><td><code>admin_schemav2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.admin_schemav2</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `meta` | `array` | Additional metadata associated with schema. This is a legacy field and usually consists of an empty array of strings. |
| `metrics` | `array` | List of schema fields grouped as dimensions that can be used with an aggregate function such as `sum`, `avg`, `min`, and `max`. |
| `dimensions` | `array` | List of schema fields grouped as dimensions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_environments_analytics_admin_getSchemav2` | `SELECT` | `environmentsId, organizationsId` |

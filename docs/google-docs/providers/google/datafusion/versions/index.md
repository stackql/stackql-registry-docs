---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - datafusion
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
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datafusion.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `availableFeatures` | `array` | Represents a list of available feature names for a given version. |
| `defaultVersion` | `boolean` | Whether this is currently the default version for Cloud Data Fusion |
| `type` | `string` | Type represents the release availability of the version |
| `versionNumber` | `string` | The version number of the Data Fusion instance, such as '6.0.1.0'. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_versions_list` | `SELECT` | `locationsId, projectsId` |

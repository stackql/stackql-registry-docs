---
title: zones_serverconfig
hide_title: false
hide_table_of_contents: false
keywords:
  - zones_serverconfig
  - container
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>zones_serverconfig</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.zones_serverconfig</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `validNodeVersions` | `array` | List of valid node upgrade target versions, in descending order. |
| `channels` | `array` | List of release channel configurations. |
| `defaultClusterVersion` | `string` | Version of Kubernetes the service deploys by default. |
| `defaultImageType` | `string` | Default image type. |
| `validImageTypes` | `array` | List of valid image types. |
| `validMasterVersions` | `array` | List of valid master versions, in descending order. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_zones_get_serverconfig` | `SELECT` | `projectId, zone` |

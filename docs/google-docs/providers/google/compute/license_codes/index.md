---
title: license_codes
hide_title: false
hide_table_of_contents: false
keywords:
  - license_codes
  - compute
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
<tr><td><b>Name</b></td><td><code>license_codes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.license_codes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. The name is 1-20 characters long and must be a valid 64 bit integer. |
| `description` | `string` | [Output Only] Description of this License Code. |
| `transferable` | `boolean` | [Output Only] If true, the license will remain attached when creating images or snapshots from disks. Otherwise, the license is not transferred. |
| `state` | `string` | [Output Only] Current state of this License Code. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `kind` | `string` | [Output Only] Type of resource. Always compute#licenseCode for licenses. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `licenseAlias` | `array` | [Output Only] URL and description aliases of Licenses with the same License Code. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `licenseCodes_get` | `SELECT` | `licenseCode, project` |

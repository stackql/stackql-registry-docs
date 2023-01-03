---
title: scans
hide_title: false
hide_table_of_contents: false
keywords:
  - scans
  - spanner
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
<tr><td><b>Name</b></td><td><code>scans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.spanner.scans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique name of the scan, specific to the Database service implementing this interface. |
| `scanData` | `object` | ScanData contains Cloud Key Visualizer scan data used by the caller to construct a visualization. |
| `startTime` | `string` | A range of time (inclusive) for when the scan is defined. The lower bound for when the scan is defined. |
| `details` | `object` | Additional information provided by the implementer. |
| `endTime` | `string` | The upper bound for when the scan is defined. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |

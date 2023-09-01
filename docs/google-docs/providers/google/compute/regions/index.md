---
title: regions
hide_title: false
hide_table_of_contents: false
keywords:
  - regions
  - compute
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
<tr><td><b>Name</b></td><td><code>regions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.regions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. |
| `description` | `string` | [Output Only] Textual description of the resource. |
| `status` | `string` | [Output Only] Status of the region, either UP or DOWN. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `quotas` | `array` | [Output Only] Quotas assigned to this region. |
| `deprecated` | `object` | Deprecation status for a public resource. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#region for regions. |
| `supportsPzs` | `boolean` | [Output Only] Reserved for future use. |
| `zones` | `array` | [Output Only] A list of zones available in this region, in the form of resource URLs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `project, region` | Returns the specified Region resource. To decrease latency for this method, you can optionally omit any unneeded information from the response by using a field mask. This practice is especially recommended for unused quota information (the `quotas` field). To exclude one or more fields, set your request's `fields` query parameter to only include the fields you need. For example, to only include the `id` and `selfLink` fields, add the query parameter `?fields=id,selfLink` to your request. |
| `list` | `SELECT` | `project` | Retrieves the list of region resources available to the specified project. To decrease latency for this method, you can optionally omit any unneeded information from the response by using a field mask. This practice is especially recommended for unused quota information (the `items.quotas` field). To exclude one or more fields, set your request's `fields` query parameter to only include the fields you need. For example, to only include the `id` and `selfLink` fields, add the query parameter `?fields=id,selfLink` to your request. |

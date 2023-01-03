---
title: environments_trace_config
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_trace_config
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
<tr><td><b>Name</b></td><td><code>environments_trace_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.environments_trace_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `samplingConfig` | `object` | TraceSamplingConfig represents the detail settings of distributed tracing. Only the fields that are defined in the distributed trace configuration can be overridden using the distribute trace configuration override APIs. |
| `endpoint` | `string` | Required. Endpoint of the exporter. |
| `exporter` | `string` | Required. Exporter that is used to view the distributed trace captured using OpenCensus. An exporter sends traces to any backend that is capable of consuming them. Recorded spans can be exported by registered exporters. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_environments_getTraceConfig` | `SELECT` | `environmentsId, organizationsId` |

---
title: instances_serial_port_output
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_serial_port_output
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
<tr><td><b>Name</b></td><td><code>instances_serial_port_output</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instances_serial_port_output</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `next` | `string` | [Output Only] The position of the next byte of content, regardless of whether the content exists, following the output returned in the `contents` property. Use this value in the next request as the start parameter. |
| `selfLink` | `string` | [Output Only] Server-defined URL for this resource. |
| `start` | `string` | The starting byte position of the output that was returned. This should match the start parameter sent with the request. If the serial console output exceeds the size of the buffer (1 MB), older output is overwritten by newer content. The output start value will indicate the byte position of the output that was returned, which might be different than the `start` value that was specified in the request. |
| `contents` | `string` | [Output Only] The contents of the console output. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#serialPortOutput for serial port output. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instances_getSerialPortOutput` | `SELECT` | `instance, project, zone` |

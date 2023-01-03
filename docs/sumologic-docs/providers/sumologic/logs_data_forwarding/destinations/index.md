---
title: destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - destinations
  - logs_data_forwarding
  - sumologic    
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
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.logs_data_forwarding.destinations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the data forwarding destination. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `invalidatedBySystem` | `boolean` | True if invalidated by the system. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getDataForwardingBuckets` | `SELECT` |  | Get a list of all Amazon S3 data forwarding destinations. |
| `getDataForwardingDestination` | `SELECT` | `id` | Get an S3 data forwarding destination by the given identifier. |
| `createDataForwardingBucket` | `INSERT` |  | Create a new Amazon S3 data forwarding destination. |
| `deleteDataForwardingBucket` | `DELETE` | `id` | Delete an existing Amazon S3 data forwarding destination with the given identifier. |
| `UpdateDataForwardingBucket` | `EXEC` | `id, data__authenticationMode` | Update an S3 data forwarding destination by the given identifier. |

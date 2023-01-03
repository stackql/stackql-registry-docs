---
title: datastores
hide_title: false
hide_table_of_contents: false
keywords:
  - datastores
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
<tr><td><b>Name</b></td><td><code>datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.datastores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `self` | `string` | Output only. Resource link of Datastore. Example: `/organizations/{org}/analytics/datastores/{uuid}` |
| `targetType` | `string` | Destination storage type. Supported types `gcs` or `bigquery`. |
| `createTime` | `string` | Output only. Datastore create time, in milliseconds since the epoch of 1970-01-01T00:00:00Z |
| `datastoreConfig` | `object` | Configuration detail for datastore |
| `displayName` | `string` | Required. Display name in UI |
| `lastUpdateTime` | `string` | Output only. Datastore last update time, in milliseconds since the epoch of 1970-01-01T00:00:00Z |
| `org` | `string` | Output only. Organization that the datastore belongs to |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_analytics_datastores_get` | `SELECT` | `datastoresId, organizationsId` | Get a Datastore |
| `organizations_analytics_datastores_list` | `SELECT` | `organizationsId` | List Datastores |
| `organizations_analytics_datastores_create` | `INSERT` | `organizationsId` | Create a Datastore for an org |
| `organizations_analytics_datastores_delete` | `DELETE` | `datastoresId, organizationsId` | Delete a Datastore from an org. |
| `organizations_analytics_datastores_test` | `EXEC` | `organizationsId` | Test if Datastore configuration is correct. This includes checking if credentials provided by customer have required permissions in target destination storage |
| `organizations_analytics_datastores_update` | `EXEC` | `datastoresId, organizationsId` | Update a Datastore |

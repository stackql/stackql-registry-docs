---
title: saved_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_queries
  - vault
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saved_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.vault.saved_queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `createTime` | `string` | Output only. The server-generated timestamp when the saved query was created. |
| `displayName` | `string` | The name of the saved query. |
| `matterId` | `string` | Output only. The matter ID of the matter the saved query is saved in. The server does not use this field during create and always uses matter ID in the URL. |
| `query` | `object` | The query definition used for search and export. |
| `savedQueryId` | `string` | A unique identifier for the saved query. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `matters_savedQueries_get` | `SELECT` | `matterId, savedQueryId` | Retrieves the specified saved query. |
| `matters_savedQueries_list` | `SELECT` | `matterId` | Lists the saved queries in a matter. |
| `matters_savedQueries_create` | `INSERT` | `matterId` | Creates a saved query. |
| `matters_savedQueries_delete` | `DELETE` | `matterId, savedQueryId` | Deletes the specified saved query. |

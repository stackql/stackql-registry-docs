---
title: metadata_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_stores
  - aiplatform
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
<tr><td><b>Name</b></td><td><code>metadata_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.metadata_stores</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the MetadataStore instance. |
| `description` | `string` | Description of the MetadataStore. |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `state` | `object` | Represents state information for a MetadataStore. |
| `updateTime` | `string` | Output only. Timestamp when this MetadataStore was last updated. |
| `createTime` | `string` | Output only. Timestamp when this MetadataStore was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, metadataStoresId, projectsId` | Retrieves a specific MetadataStore. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists MetadataStores for a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Initializes a MetadataStore, including allocation of resources. |
| `delete` | `DELETE` | `locationsId, metadataStoresId, projectsId` | Deletes a single MetadataStore and all its child resources (Artifacts, Executions, and Contexts). |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists MetadataStores for a Location. |

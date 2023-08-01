---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
  - contentwarehouse
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
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contentwarehouse.documents</code></td></tr>
</tbody></table>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `documentsId, locationsId, projectsId` | Gets a document. Returns NOT_FOUND if the document does not exist. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a document. |
| `delete` | `DELETE` | `documentsId, locationsId, projectsId` | Deletes a document. Returns NOT_FOUND if the document does not exist. |
| `linked_sources` | `EXEC` | `documentsId, locationsId, projectsId` | Return all source document-links from the document. |
| `linked_targets` | `EXEC` | `documentsId, locationsId, projectsId` | Return all target document-links from the document. |
| `lock` | `EXEC` | `documentsId, locationsId, projectsId` | Lock the document so the document cannot be updated by other users. |
| `patch` | `EXEC` | `documentsId, locationsId, projectsId` | Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name. |
| `search` | `EXEC` | `locationsId, projectsId` | Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against. |
| `set_acl` | `EXEC` | `documentsId, locationsId, projectsId` | Sets the access control policy for a resource. Replaces any existing policy. |

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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contentwarehouse.documents" /></td></tr>
</tbody></table>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Gets a document. Returns NOT_FOUND if the document does not exist. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a document. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Deletes a document. Returns NOT_FOUND if the document does not exist. |
| <CopyableCode code="linked_sources" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Return all source document-links from the document. |
| <CopyableCode code="linked_targets" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Return all target document-links from the document. |
| <CopyableCode code="lock" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Lock the document so the document cannot be updated by other users. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name. |
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against. |
| <CopyableCode code="set_acl" /> | `EXEC` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Sets the access control policy for a resource. Replaces any existing policy. |

---
title: documents_collection_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - documents_collection_ids
  - firestore
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>documents_collection_ids</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documents_collection_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.firestore.documents_collection_ids" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="collectionIds" /> | `array` | The collection ids. |
| <CopyableCode code="nextPageToken" /> | `string` | A page token that may be used to continue the list. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_collection_ids" /> | `SELECT` | <CopyableCode code="databasesId, documentsId, documentsId1, projectsId" /> | Lists all the collection IDs underneath a document. |

## `SELECT` examples

Lists all the collection IDs underneath a document.

```sql
SELECT
collectionIds,
nextPageToken
FROM google.firestore.documents_collection_ids
WHERE databasesId = '{{ databasesId }}'
AND documentsId = '{{ documentsId }}'
AND documentsId1 = '{{ documentsId1 }}'
AND projectsId = '{{ projectsId }}'; 
```

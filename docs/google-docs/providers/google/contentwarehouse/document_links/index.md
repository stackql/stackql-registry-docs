---
title: document_links
hide_title: false
hide_table_of_contents: false
keywords:
  - document_links
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>document_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contentwarehouse.document_links" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="documentsId, locationsId, projectsId" /> | Create a link between a source document and a target document. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="documentLinksId, documentsId, locationsId, projectsId" /> | Remove the link between the source and target documents. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>document_links</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.contentwarehouse.document_links (
documentsId,
locationsId,
projectsId,
documentLink,
requestMetadata
)
SELECT 
'{{ documentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ documentLink }}',
'{{ requestMetadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: documentLink
      value:
        - name: name
          value: '{{ name }}'
        - name: sourceDocumentReference
          value:
            - name: documentIsFolder
              value: '{{ documentIsFolder }}'
            - name: documentIsLegalHoldFolder
              value: '{{ documentIsLegalHoldFolder }}'
            - name: documentName
              value: '{{ documentName }}'
            - name: snippet
              value: '{{ snippet }}'
            - name: documentIsRetentionFolder
              value: '{{ documentIsRetentionFolder }}'
            - name: displayName
              value: '{{ displayName }}'
        - name: state
          value: '{{ state }}'
        - name: description
          value: '{{ description }}'
    - name: requestMetadata
      value:
        - name: userInfo
          value:
            - name: groupIds
              value:
                - name: type
                  value: '{{ type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>document_links</code> resource.

```sql
/*+ delete */
DELETE FROM google.contentwarehouse.document_links
WHERE documentLinksId = '{{ documentLinksId }}'
AND documentsId = '{{ documentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

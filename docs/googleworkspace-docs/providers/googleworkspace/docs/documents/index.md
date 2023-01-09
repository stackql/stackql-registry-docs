---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
  - docs
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
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.docs.documents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `inlineObjects` | `object` | Output only. The inline objects in the document, keyed by object ID. |
| `headers` | `object` | Output only. The headers in the document, keyed by header ID. |
| `documentId` | `string` | Output only. The ID of the document. |
| `namedStyles` | `object` | The named styles. Paragraphs in the document can inherit their TextStyle and ParagraphStyle from these named styles. |
| `namedRanges` | `object` | Output only. The named ranges in the document, keyed by name. |
| `positionedObjects` | `object` | Output only. The positioned objects in the document, keyed by object ID. |
| `footnotes` | `object` | Output only. The footnotes in the document, keyed by footnote ID. |
| `body` | `object` | The document body. The body typically contains the full document contents except for headers, footers, and footnotes. |
| `suggestionsViewMode` | `string` | Output only. The suggestions view mode applied to the document. Note: When editing a document, changes must be based on a document with SUGGESTIONS_INLINE. |
| `suggestedDocumentStyleChanges` | `object` | Output only. The suggested changes to the style of the document, keyed by suggestion ID. |
| `suggestedNamedStylesChanges` | `object` | Output only. The suggested changes to the named styles of the document, keyed by suggestion ID. |
| `title` | `string` | The title of the document. |
| `footers` | `object` | Output only. The footers in the document, keyed by footer ID. |
| `documentStyle` | `object` | The style of the document. |
| `revisionId` | `string` | Output only. The revision ID of the document. Can be used in update requests to specify which revision of a document to apply updates to and how the request should behave if the document has been edited since that revision. Only populated if the user has edit access to the document. The revision ID is not a sequential number but an opaque string. The format of the revision ID might change over time. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across users. If the revision ID is unchanged between calls, then the document has not changed. Conversely, a changed ID (for the same document and user) usually means the document has been updated. However, a changed ID can also be due to internal factors such as ID format changes. |
| `lists` | `object` | Output only. The lists in the document, keyed by list ID. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `documentId` | Gets the latest version of the specified document. |
| `create` | `INSERT` |  | Creates a blank document using the title given in the request. Other fields in the request, including any provided content, are ignored. Returns the created document. |
| `batchUpdate` | `EXEC` | `documentId` | Applies one or more updates to the document. Each request is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests. For example, suppose you call batchUpdate with four updates, and only the third one returns information. The response would have two empty replies, the reply to the third request, and another empty reply, in that order. Because other users may be editing the document, the document might not exactly reflect your changes: your changes may be altered with respect to collaborator changes. If there are no collaborators, the document should reflect your changes. In any case, the updates in your request are guaranteed to be applied together atomically. |

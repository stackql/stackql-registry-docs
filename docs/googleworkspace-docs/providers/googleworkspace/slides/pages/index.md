---
title: pages
hide_title: false
hide_table_of_contents: false
keywords:
  - pages
  - slides
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
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.slides.pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `pageType` | `string` | The type of the page. |
| `objectId` | `string` | The object ID for this page. Object IDs used by Page and PageElement share the same namespace. |
| `pageProperties` | `object` | The properties of the Page. The page will inherit properties from the parent page. Depending on the page type the hierarchy is defined in either SlideProperties or LayoutProperties. |
| `pageElements` | `array` | The page elements rendered on the page. |
| `slideProperties` | `object` | The properties of Page that are only relevant for pages with page_type SLIDE. |
| `revisionId` | `string` | Output only. The revision ID of the presentation. Can be used in update requests to assert the presentation revision hasn't changed since the last read operation. Only populated if the user has edit access to the presentation. The revision ID is not a sequential number but an opaque string. The format of the revision ID might change over time. A returned revision ID is only guaranteed to be valid for 24 hours after it has been returned and cannot be shared across users. If the revision ID is unchanged between calls, then the presentation has not changed. Conversely, a changed ID (for the same presentation and user) usually means the presentation has been updated. However, a changed ID can also be due to internal factors such as ID format changes. |
| `notesProperties` | `object` | The properties of Page that are only relevant for pages with page_type NOTES. |
| `layoutProperties` | `object` | The properties of Page are only relevant for pages with page_type LAYOUT. |
| `masterProperties` | `object` | The properties of Page that are only relevant for pages with page_type MASTER. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `presentations_pages_get` | `SELECT` | `pageObjectId, presentationId` |

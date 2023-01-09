---
title: forms
hide_title: false
hide_table_of_contents: false
keywords:
  - forms
  - forms
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
<tr><td><b>Name</b></td><td><code>forms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.forms.forms</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the item. |
| `textItem` | `object` | A text item. |
| `imageItem` | `object` | An item containing an image. |
| `questionItem` | `object` | A form item containing a single question. |
| `pageBreakItem` | `object` | A page break. The title and description of this item are shown at the top of the new page. |
| `itemId` | `string` | The item ID. On creation, it can be provided but the ID must not be already used in the form. If not provided, a new ID is assigned. |
| `questionGroupItem` | `object` | Defines a question that comprises multiple questions grouped together. |
| `title` | `string` | The title of the item. |
| `videoItem` | `object` | An item containing a video. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `formId` | Get a form. |
| `create` | `INSERT` |  | Create a new form using the title given in the provided form message in the request. *Important:* Only the form.info.title and form.info.document_title fields are copied to the new form. All other fields including the form description, items and settings are disallowed. To create a new form and add items, you must first call forms.create to create an empty form with a title and (optional) document title, and then call forms.update to add the items. |
| `batchUpdate` | `EXEC` | `formId` | Change the form with a batch of updates. |

---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
  - content
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `accountLabels` | `array` | The labels from the specified account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_labels_list` | `SELECT` | `accountId` | Lists the labels assigned to an account. |
| `accounts_labels_create` | `INSERT` | `accountId` | Creates a new label, not assigned to any account. |
| `orderreturns_labels_create` | `INSERT` | `merchantId, returnId` | Links a return shipping label to a return id. You can only create one return label per return id. Since the label is sent to the buyer, the linked return label cannot be updated or deleted. If you try to create multiple return shipping labels for a single return id, every create request except the first will fail. |
| `accounts_labels_delete` | `DELETE` | `accountId, labelId` | Deletes a label and removes it from all accounts to which it was assigned. |
| `accounts_labels_patch` | `EXEC` | `accountId, labelId` | Updates a label. |

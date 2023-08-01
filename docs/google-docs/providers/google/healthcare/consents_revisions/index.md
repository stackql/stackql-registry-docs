---
title: consents_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - consents_revisions
  - healthcare
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
<tr><td><b>Name</b></td><td><code>consents_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.consents_revisions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `consents` | `array` | The returned Consent revisions. The maximum number of revisions returned is determined by the value of `page_size` in the ListConsentRevisionsRequest. |
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_revisions` | `SELECT` | `consentStoresId, consentsId, datasetsId, locationsId, projectsId` |

---
title: details
hide_title: false
hide_table_of_contents: false
keywords:
  - details
  - androidpublisher
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
<tr><td><b>Name</b></td><td><code>details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `contactWebsite` | `string` | The user-visible website for this app. |
| `defaultLanguage` | `string` | Default language code, in BCP 47 format (eg "en-US"). |
| `contactEmail` | `string` | The user-visible support email for this app. |
| `contactPhone` | `string` | The user-visible support telephone number for this app. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `edits_details_get` | `SELECT` | `editId, packageName` | Gets details of an app. |
| `edits_details_patch` | `EXEC` | `editId, packageName` | Patches details of an app. |
| `edits_details_update` | `EXEC` | `editId, packageName` | Updates details of an app. |

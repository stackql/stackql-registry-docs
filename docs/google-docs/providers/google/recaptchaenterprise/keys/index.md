---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
  - recaptchaenterprise
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recaptchaenterprise.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `keys` | `array` | Key details. |
| `nextPageToken` | `string` | Token to retrieve the next page of results. It is set to empty if no keys remain in results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `keysId, projectsId` | Returns the specified key. |
| `list` | `SELECT` | `projectsId` | Returns the list of all keys that belong to a project. |
| `create` | `INSERT` | `projectsId` | Creates a new reCAPTCHA Enterprise key. |
| `delete` | `DELETE` | `keysId, projectsId` | Deletes the specified key. |
| `migrate` | `EXEC` | `keysId, projectsId` | Migrates an existing key from reCAPTCHA to reCAPTCHA Enterprise. Once a key is migrated, it can be used from either product. SiteVerify requests are billed as CreateAssessment calls. You must be authenticated as one of the current owners of the reCAPTCHA Key, and your user must have the reCAPTCHA Enterprise Admin IAM role in the destination project. |
| `patch` | `EXEC` | `keysId, projectsId` | Updates the specified key. |

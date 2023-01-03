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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The resource name for the Key in the format "projects/{project}/keys/{key}". |
| `iosSettings` | `object` | Settings specific to keys that can be used by iOS apps. |
| `displayName` | `string` | Human-readable display name of this key. Modifiable by user. |
| `wafSettings` | `object` | Settings specific to keys that can be used for WAF (Web Application Firewall). |
| `labels` | `object` | See Creating and managing labels. |
| `webSettings` | `object` | Settings specific to keys that can be used by websites. |
| `androidSettings` | `object` | Settings specific to keys that can be used by Android apps. |
| `createTime` | `string` | The timestamp corresponding to the creation of this Key. |
| `testingOptions` | `object` | Options for user acceptance testing. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_keys_get` | `SELECT` | `keysId, projectsId` | Returns the specified key. |
| `projects_keys_list` | `SELECT` | `projectsId` | Returns the list of all keys that belong to a project. |
| `projects_keys_create` | `INSERT` | `projectsId` | Creates a new reCAPTCHA Enterprise key. |
| `projects_keys_delete` | `DELETE` | `keysId, projectsId` | Deletes the specified key. |
| `projects_keys_migrate` | `EXEC` | `keysId, projectsId` | Migrates an existing key from reCAPTCHA to reCAPTCHA Enterprise. Once a key is migrated, it can be used from either product. SiteVerify requests are billed as CreateAssessment calls. You must be authenticated as one of the current owners of the reCAPTCHA Site Key, and your user must have the reCAPTCHA Enterprise Admin IAM role in the destination project. |
| `projects_keys_patch` | `EXEC` | `keysId, projectsId` | Updates the specified key. |

---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - translate
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.translate.projects</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_detect_language` | `EXEC` | `projectsId` | Detects the language of text within a request. |
| `projects_romanize_text` | `EXEC` | `projectsId` | Romanize input text written in non-Latin scripts to Latin text. |
| `projects_translate_text` | `EXEC` | `projectsId` | Translates input text and returns translated text. |

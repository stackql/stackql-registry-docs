---
title: projects_config
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_config
  - sourcerepo
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
<tr><td><b>Name</b></td><td><code>projects_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sourcerepo.projects_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the project. Values are of the form `projects/`. |
| `pubsubConfigs` | `object` | How this project publishes a change in the repositories through Cloud Pub/Sub. Keyed by the topic names. |
| `enablePrivateKeyCheck` | `boolean` | Reject a Git push that contains a private key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_getConfig` | `SELECT` | `projectsId` |
